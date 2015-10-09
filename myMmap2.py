__author__ = 'lq'

import mmap
import contextlib

'''
with open('in.txt', 'r') as f:
    with contextlib.closing(mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)) as m:
        print 'First 10 bytes via read :', m.read(10)
        print 'First 10 bytes via slice:', m[:10]
        print '2nd   10 bytes via read :', m.read(10)
'''

import mmap
import shutil
import time

# Copy the example file
# shutil.copyfile('in.txt', 'in_copy.txt')

with open('in_copy.txt', 'r+') as f:
    with contextlib.closing(mmap.mmap(f.fileno(), 0)) as m:
        while True:
            print(m.readline().rstrip())
            m.seek(0)  # rewind
            time.sleep(0.5)
