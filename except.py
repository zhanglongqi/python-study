# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 14:16:32 2013

@author: longqi
"""
import sys

try:
    s = raw_input('Enter something --> ')
    print "you have type ", s
except EOFError:
    print '\nWhy did you do an EOF on me?'
    sys.exit()  # exit the program
except:
    print '\nSome error/exception occurred.'
# here, we are not exiting the program
print 'Done'

