# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 10:55:12 2013

@author: longqi
"""
# old formating
formatter = "%r %r %r %d"
print(formatter % (1, 2, 3, 4))
print(formatter % ("one", "two", False, True))
for i in ["/", "-", "|", "\\", "|"]:
    print("%s\t" % i)
# ==============================================================================
# age = raw_input("How old are you? ")
# height = raw_input("How tall are you? ")
# weight = raw_input("How much do you weigh? ")
#
# print "So, you're %s old, %s tall and %s heavy." % (
#     age, height, weight)
# ==============================================================================

d = "Hello \n World!!!"
print("%%r/repr():%r \n%%s/str():%s" % (d, d), '\n')

print("%10d" % (111 * 111), 'end3')
print(repr(-111 ** (-80)))

# new formatting
print(1.0 / 7, repr(1.0 / 7), str(1.0 / 7))

for x in range(1, 11):
    print(repr(x).rjust(2), repr(x * x).rjust(3), end=' ')
    # Note trailing comma on previous line
    print(repr(x ** 3).rjust(4))

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x * x, x ** 3))

print(repr(111 ** 3).rjust(10), "end")
print("{0:10d}".format(-111 * 111), 'end2')
