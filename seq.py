# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 22:00:18 2013

@author: longqi
"""

# Filename: seq.py
shoplist = ['apple', 'mango', 'carrot', 'banana']
# Indexing or 'Subscription' operation
print 'Item 0 is', shoplist[0]
print 'Item 1 is', shoplist[1]
print 'Item 2 is', shoplist[2]
print 'Item 3 is', shoplist[3]
print 'Item -1 is', shoplist[-1]
print 'Item -2 is', shoplist[-2]
# Slicing on a list
print 'Item 1 to 3 is', shoplist[1:3]
print 'Item 2 to end is', shoplist[2:]
print 'Item 1 to -1 is', shoplist[1:-1]
print 'Item start to end is', shoplist[:]
# Slicing on a string
name = 'swaroop'
print 'characters 1 to 3 is', name[1:3]
print 'characters 2 to end is', name[2:]
print 'characters 1 to -1 is', name[1:-1]
print 'characters start to end is', name[:]

for x in [1, 2, 3, 4]:
    print x

for x in (1, 2, 3, 4):
    print x

name2 = None

print name2
print [1, 2, 3] * 3
print (1, 2, 3) * 3

x = object()
y = object()

# change this code
x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print "x_list contains %d objects" % len(x_list)
print "y_list contains %d objects" % len(y_list)
print "big_list contains %d objects" % len(big_list)

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print "Almost there..."
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print "Great!"

s = "Strings are awesome!"

# Length should be 20
print "Length of s = %d" % len(s)

# First occurrence of "a" should be at index 8
print "The first occurrence of the letter a = %d" % s.index("a")

# Number of a's should be 2
print "a occurs %d times" % s.count("a")

# Slicing the string into bits
print "The first five characters are '%s'" % s[:5]  # Start to 5
print "The next five characters are '%s'" % s[5:10]  # 5 to 10
print "The twelfth character is '%s'" % s[12]  # Just number 12

print "The last five characters are '%s'" % s[-5:]  # 5th-from-last to end

# Convert everything to uppercase
print "String in uppercase: %s" % s.upper()

# Convert everything to lowercase
print "String in lowercase: %s" % s.lower()

# Check how a string starts
if s.startswith("Str"):
    print "String starts with 'Str'. Good!"

# Check how a string ends
if s.endswith("ome!"):
    print "String ends with 'ome!'. Good!"

# Split the string into three separate strings,
# each containing only a word
print "Split the words of the string: %s" % s.split(" ")

# change this code
number = 20
second_number = False
first_array = [True, True, True]
second_array = [1, 2]

if number > 15:
    print "1"

if first_array:
    print "2"

if len(second_array) == 2:
    print "3"

if len(first_array) + len(second_array) == 5:
    print "4"

if first_array and first_array[0] == 1:
    print "5"

if not second_number:
    print "6"

numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
]

for x in numbers:
    # Check if x is even
    if x % 2 == 0:
        print x
    if x == 980:
        break
import sys

print sys.version_info
print "系统API版本：", sys.api_version
print "----------------------"

print "current variables: "
#pprint.pprint(locals())
print "----------------------"
e

