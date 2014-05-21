# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 15:27:35 2013

@author: longqi
"""
import re


def printRes(res):
    print "res           ", res
    print "res.re        ", res.re
    print "res.group     ", res.group()
    print "res.groups    ", res.groups
    print "res.span      ", res.span()
    print "res.pos       ", res.pos
    print "res.endpos    ", res.endpos
    print "res.lastindex ", res.lastindex
    print "res.lastgroup ", res.lastgroup


str1 = "I'm a little bird,My name is 110:110:111:12 汉字\
test will match the string test exactly. (You can enable a\
 case-insensitive mode that would let this RE match Test or\
 TEST as well; more about this later./usr/bin/qmake)\
	/opt/Qt/qt5/qmake"

patterns = [re.compile(r'litt\w+\W', re.I), re.compile(r'\w+'), re.compile(r'/usr.+qmake')]

print str1
for x in patterns:
    #	match = x.match(str1)
    match = re.search(x, str1)
    if match:
        printRes(match)
    else:
        print match
    print "*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*"
