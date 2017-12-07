#-*-coding:utf8-*-
#########################################################################
#   Copyright (C) 2017 All rights reserved.
# 
#   FileName:SVM.py
#   Creator: yuliu1@microsoft.com
#   Time:12/06/2017
#   Description:
#
#   Updates:
#
#########################################################################
#!/usr/bin/python
# please add your code here!
import math;
import numpy as np;
import sys;
from sklearn.neighbors import KNeighborsClassifier

def GetLabelById(itsId):
    if (itsId==0):
        return "S";
    elif (itsId==1):
        return "B";
    elif (itsId==2):
        return "M";
    else:
        return "E";

def FormatVector(line):
    col = line.split("\t");
    intcol = [int(float(elem)) for elem in col];
    x = intcol[:-1];
    y = intcol[-1];
    return x, y;


def LoadTrainFile(filename):
    m = 4;
    n = 100;
    XList=[];
    YList=[];
    linecount = 0;
    with open(filename,"r") as f:
        for line in f:
            line = line.strip();
            if line=="":
                continue;
            col = line.split("\t");
            if (len(col) == 1):
                continue;
            linesegment = "\t".join(col[:n+1]); 
            x,y = FormatVector(linesegment);
            XList.append(x);
            YList.append(y);
    X=np.array(XList);
    Y=np.array(YList); 
    return X,Y;
     
def Train(X,Y):
    clf=KNeighborsClassifier(n_neighbors=5);
    clf.fit(X, Y);
    return clf;

def Predict(clf,Xtest):
    y=clf.predict(Xtest);
    return GetLabelById(y[0]); 

def Run(clf, infilename,outfilename):
    linecount = 0;
    m = 4;
    n = 100;
    fout = open(outfilename,"w");
    with open(infilename,"r") as f:
        for line in f:
            line = line.strip();
            col = line.split("\t");
            if (len(col) == 1):
                fout.write("\n");
                continue;
            linesegment = "\t".join(col[:n+1]); 
            x,y = FormatVector(linesegment);
            x2=[];
            x2.append(x);
            x_test = np.array(x2);
            label = Predict(clf,x_test);
            newcol = col[-1].split("#");
            newline = "\t".join(newcol);
            fout.write("%s\t%s\n"%(newline,label));
            linecount+=1;
            if(linecount%5 == 0):
                sys.stderr.write("linecount=%d\n"%linecount);


if __name__=="__main__":
    if (len(sys.argv)!=4):
        sys.stderr.write("no enough params\n");
        sys.exit(1);
    X,Y=LoadTrainFile(sys.argv[1]);  
    clf = Train(X,Y);
    Run(clf,sys.argv[2],sys.argv[3]);
     
