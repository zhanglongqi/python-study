# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 19:44:57 2013
@brief 制作简单的http服务器
@author: longqi
"""
import BaseHTTPServer

class WebRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':      # 匹配 url ：/ 根目录的请求
            self.send_response(200)
            print self.client_address
            self.do_something()
        else:
            self.send_error(404) # 对于错误的请求，返回 404 错误
           
    def do_something(self):
        print 'hello world'
       
server = BaseHTTPServer.HTTPServer(('172.21.72.27',8080), WebRequestHandler)    # 创建 HTTPSever 服务器，绑定地址：http://127.0.0.1:8080
server.serve_forever()   # 启动 HTTPServer 服务器 
