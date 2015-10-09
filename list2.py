#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created by longqi on 8/20/14
"""
__author__ = 'longqi'
ip = ['default', 'via', '172.22.32.1', 'dev', 'wlan1', '\n172.22.32.0/20', 'dev', 'wlan1', '', 'proto', 'kernel', '',
      'scope', 'link', '', 'src', '172.22.33.12', '\n192.168.7.0/30', 'dev', 'usb0', '', 'proto', 'kernel', '', 'scope',
      'link', '', 'src', '192.168.7.2', '\n196.3.20.0/24', 'dev', 'eth0', '', 'proto', 'kernel', '', 'scope', 'link',
      '', 'src', '196.3.20.120', '\n']


def simplify_ip_info(source):
    temp = []
    target = ''
    # source = source.split(' ')

    print('source: ')
    print(source)
    for i in range(0, len(source)):
        if source[i] == 'src':
            temp.append(source[i + 1])

    for t1 in temp:
        target = target + t1 + ' ; '
    return target


print(simplify_ip_info(ip))
