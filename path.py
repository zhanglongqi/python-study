# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 16:39:28 2013

@author: longqi
"""
import os

print "current running file:", os.path.realpath(__file__)
print "current running file's size:", os.path.getsize(os.path.realpath(__file__)),"bytes"
print __file__
print os.__file__,'\n',os.__doc__

import inspect, os
print inspect.getfile(inspect.currentframe()) # script filename (usually with path)
print os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) # script directory
print inspect.getfile(os)