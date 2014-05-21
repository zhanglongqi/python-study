# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 14:58:08 2013

@author: longqi
"""

#unpacking arguments to viriables
#script, first, second, third = argv
#print "The script is called:", script
#print "Your first variable is:", first
#print "Your second variable is:", second
#print "Your third variable is:", third
print range(3, 7)
args = [3, 6, 12]
print range(*args)  # call with arguments unpacked from a list
print """
talking more
talking more line 2
talking more line 3
"""
print args