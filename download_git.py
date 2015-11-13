#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
longqi 13/Nov/15 13:24

usage: put all your git url to excel,
 this app will download all the git repositories

"""

import subprocess

from openpyxl import load_workbook

git_file = 'git.xlsx'
col_name = 'A'
col_begin = 1
col_end = 40
TEST = True

wb = load_workbook(filename=git_file)
sheet_ranges = wb['Sheet1']
git_names = []

for i in range(col_begin, col_end):
    cell = col_name + str(i)
    git_names.append(sheet_ranges[cell].value)

for git_name in git_names:
    if TEST:
        subprocess.Popen('echo "%s"' % git_name, shell=True, )
    else:
        subprocess.Popen('git clone "%s"' % git_name, shell=True, )
