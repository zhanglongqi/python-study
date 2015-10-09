# -*- coding: utf-8 -*-
"""
Created by longqi on 8/19/14
"""
__author__ = 'longqi'


class Parent(object):
    def __init__(self):
        print('parent __init__  ...')


class Son(Parent):
    def __init__(self):
        Parent.__init__(self)
        print('son')


son1 = Son()


class class1(object):
    def __init__(self, var1):
        self.v1 = var1

    def print2(self):
        class2().printokay(self.v1)


import logging


class class2(object):
    def __init__(self):
        self.v2 = 'dd'
        self.db_logger = logging.getLogger('db_logger')

    def printokay(self, p1):
        self.db_logger.info('test')
        print("this is text")
        print(self.v2 + p1)


a = class1("jumbo bitch")
a.print2()
