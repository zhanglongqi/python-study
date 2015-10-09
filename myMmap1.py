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

f = open("in_copy.txt", "r+")
mmapData = mmap.mmap(f.fileno(), 0)
count = 0
with open('in_copy.txt', 'r+') as f:
    with contextlib.closing(mmap.mmap(f.fileno(), 0)) as m:
        time1 = time.time()
        while True:
            #            print 'Before:'
            #            print m.readline().rstrip()
            m.seek(0)  # rewind

            loc = 1
            m[loc:loc + 3] = 'abc'
            #            m.flush()

            m.seek(0)  # rewind
            #            print 'After :'
            #            print m.readline().rstrip()

            loc = 1
            m[loc:loc + 3] = 'XYZ'
            #            m.flush()
            m.seek(0)
            count += 1
            if count == 1000:
                time2 = time.time()
                break

print(time2 - time1)
