__author__ = 'longqi'

l1 = [2,6,20,4]
print l1

l1.insert(3,9)
print l1


#using lists as stacks
l1.append(87)
print l1
print l1.__len__()
print l1.pop()
print l1
print l1.__len__()

#using lists as queues
#l1.popleft()

"""
Slicing
Just as you use indexing to access individual elements, you can use slicingto access rangesof
elements.
The firstindex is the number of the first element you want to include.
However, the lastindex is the number of the first element afteryour slice.
"""

l1.append('ab')
l1.append('xyz')
print l1
print l1[3:100], l1[1:4]
print l1[-3:-1]
print l1[3:],l1[:3]