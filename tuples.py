# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 11:25:33 2013

@author: longqi
"""

tuple = (1, 's', "zhang")
#tuple[1]="zhang1"
# NO, tuples cannot be changed
tuple = (1, 'zhang1', 'zhang')
# this works
tuple2 = (1,)
#To create a size-1 tuple, the lone element must
#be followed by a comma.
(x, y, z) = (10, 13, "like")


print ((tuple, x, y, z))
print ((x * 3, z * 3))
print ((x / 2, x / 3, x / 3.0, x // 3, x % 3))