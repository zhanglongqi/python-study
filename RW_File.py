# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
/home/longqi/.spyder2/.temp.py
"""


def change(line):
    newLine = ''
    if 'RA' in line:
        newLine = line[0:line.find('RA\t[x]')]
    else:
        newLine = line

    return newLine


output = open('Animation_Raw_LUT_2.dat', 'w')
with open("Animation_Raw_LUT.dat") as infile:
    for line in infile:
        output.write(change(line) + '\n')

output.close()