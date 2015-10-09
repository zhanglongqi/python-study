# -*-coding:utf-8 -*-
__author__ = 'longqi'
print('中国人')
print(input('输入：'))

import urllib.request, urllib.error, urllib.parse

print(urllib.parse.unquote('/?name=Mr.%E4%B8%AD%E5%9B%BD%E4%BA%BA'), urllib.parse.quote('中国人'))

import time

for i in range(1, 100):
    time.sleep(1)
    print('progress: ' + str(i) + "%", end='\r')
