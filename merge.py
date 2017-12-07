#-*-coding:utf8-*-
#########################################################################
#   Copyright (C) 2017 All rights reserved.
# 
#   FileName:merge.py
#   Creator: yuliu1@microsoft.com
#   Time:11/15/2017
#   Description:
#
#   Updates:
#
#########################################################################
#!/usr/bin/python
# please add your code here!
import sys;
import re;
def Process(ifile,ofile):
    fout = open(ofile,"w");
    with open(ifile,"r") as f:
        newline="";
        str1="";
        str2="";
        str3="";
        str4="";
        for line in f:
            line = line.strip();
            col = line.split("\t");
            print len(col);
            if(len(col)==4):
                if (col[2]=="S"):
                    if (str1!=""):
                        str1+="#";
                    if (str2 != ""):
                        str2+="#";
                    if (str3 != ""):
                        str3 += "#";
                    if (str4 != ""):
                        str4 += "#"
                    str1+=col[0];
                    str2+=col[1];
                    str3+=col[2];
                    str4+=col[3];
                elif(col[2]=="B"):
                    if (str1!=""):
                        str1+="#";
                    if (str2 != ""):
                        str2+="#";
                    if (str3 != ""):
                        str3 += "#";
                    if (str4 != ""):
                        str4 += "#";
                    str1+=col[0];
                    str2+=col[1];
                    str3+=col[2];
                    str4+=col[3];
                else:
                    str1+=",";
                    str2+=",";
                    str3+=",";
                    str4+=",";
                    str1+=col[0];
                    str2+=col[1];
                    str3+=col[2];
                    str4+=col[3];
            else:
                newline="%s\t%s\t%s\t%s"%(str1,str2,str3,str4);
                fout.write("%s\n"%newline);
                newline="";
                str1="";
                str2="";
                str3="";
                str4="";
    fout.close();
if __name__=="__main__":
    if (len(sys.argv)!=3):
        sys.stderr.write("not enough params");
        sys.exit(1);
    Process(sys.argv[1],sys.argv[2]);

