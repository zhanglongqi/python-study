# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 15:49:21 2013

@author: longqi
"""

import os
import time

source = ['~/dict', '~/w2.txt']  #source to backup
target_dir = '/tmp/'  # directory to backup
target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'
zip_command = "zip -qr '%s' %s" % (target, ' '.join(source))
print zip_command
#run the script
if (os.system(zip_command) == 0):
    print 'successfully backup', source, 'to', target
else:
    print 'backup failed'