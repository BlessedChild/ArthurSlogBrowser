#!/usr/bin/python
# -*- coding: UTF-8 -*-

f = open("index.html", "rt") # 搜索并打开当前路径下的 index.html 文件

fr = f.read() # 读取 index.html 文件

restr = fr.split('<div>', 2 ) # 解析 index.html 文件，这里把 <div> 给去掉

print restr[1]