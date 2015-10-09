'''
import mmap
import contextlib

with open('in.txt', 'r') as f:
    with contextlib.closing(mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)) as m:
        print 'First 10 bytes via read :', m.read(10)
        print 'First 10 bytes via slice:', m[:10]
        print '2nd   10 bytes via read :', m.read(10)
'''

import mmap
import shutil

# Copy the example file
shutil.copyfile('in.txt', 'in_copy.txt')

f = open("in_copy.txt", "r+")
mmapData = mmap.mmap(f.fileno(), 0)


def delete_from_mmap(start, end):
    global mmapData
    length = end - start
    size = len(mmapData)
    newsize = size - length

    mmapData.move(start, end, size - end)
    mmapData.flush()
    mmapData.close()
    f.truncate(newsize)
    mmapData = mmap.mmap(f.fileno(), 0)


def insert_into_mmap(offset, data):
    global mmapData
    length = len(data)
    size = len(mmapData)
    newsize = size + length

    mmapData.flush()
    mmapData.close()
    f.seek(size)
    f.write("A" * length)
    f.flush()
    mmapData = mmap.mmap(f.fileno(), 0)

    mmapData.move(offset + length, offset, size - offset)
    mmapData.seek(offset)
    mmapData.write(data)
    mmapData.flush()


def replace_in_mmap(offset, olddata, newdata):
    global mmapData
    insert_into_mmap(offset, newdata)
    delete_from_mmap(offset + len(newdata), offset + len(newdata) + len(olddata))


insert_into_mmap(4, "AAAA")

replace_in_mmap(2, 'i', 'zhang')
