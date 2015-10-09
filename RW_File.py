#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created by longqi on 8/19/14
"""
__author__ = 'longqi'


def change(line):
    newLine = ''
    if 'RA' in line:
        newLine = line[0:line.find('RA\t[x]')]
    else:
        newLine = line

    return newLine


try:
    datFile = open('in.txt', 'r')
except IOError:
    print("open failed...")

if not datFile.closed:

    print('\n***********1***********')
    for line in datFile:
        # print(datFile.tell())
        print(line, end='')
    print('reading for the first time end\n')

    print('\n***********2***********')
    datFile.seek(2, 0)
    line = datFile.read(6)
    print(line, '\n', datFile.tell())

    print('\n***********3***********')
    datFile.seek(0, 0)
    l1 = list(datFile)
    print(l1)

    print('\n***********4***********')
    datFile.seek(0, 0)
    ll = datFile.readlines()
    print(l1)

datFile.close()
