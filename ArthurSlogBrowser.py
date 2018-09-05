#!/usr/bin/python
# -*- coding: UTF-8 -*-
# ArthurSlog
# v0.0.1

import Tkinter as tk
master = tk.Tk()

arthurslogbrower_file = open("index.html", "rt") # 搜索并打开当前路径下的 index.html 文件

arthurslogbrower_file_f = arthurslogbrower_file.read() # 读取 html文件

rendering_file = arthurslogbrower_file_f.split('<div>', 2 ) # HTML解析器，解析html文件并分析数据结构, 这里把 <div> 给去掉

msg = tk.Message(master, text = rendering_file[1]) # 像素、图形渲染器，把解析好的数据显示在屏幕上

msg.pack()

tk.mainloop()