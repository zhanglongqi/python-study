# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 18:28:20 2013
@brief 制作http服务器 共享当前工作目录
@author: longqi
"""
import sys
import http.server
from http.server import SimpleHTTPRequestHandler

HandlerClass = SimpleHTTPRequestHandler
ServerClass = http.server.HTTPServer
Protocol = "HTTP/1.0"

if sys.argv[1:]:
    port = int(sys.argv[1])
else:
    port = 8080
# server_address = ('127.0.0.1', port)#only for localhost
server_address = ('172.21.72.27', port)  # only for localhost

HandlerClass.protocol_version = Protocol
httpd = ServerClass(server_address, HandlerClass)

sa = httpd.socket.getsockname()
print("Serving HTTP on", sa[0], "port", sa[1], "...")
httpd.serve_forever()
