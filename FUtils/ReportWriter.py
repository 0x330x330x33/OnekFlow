#!/usr/bin/env python
#-*- coding:utf-8 -*- 
# 作者: cc
# 邮箱: cc@qq.com
# 时间: 2023-04-08 18:47:42
# 描述: todo ...
import markdown
# import markdown2
from Config import G_HTML_HEAD

#import pypandoc

def write_txt(filename,text):
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text)

def write_html(filename,text):
    html = markdown.markdown(text,extensions=['tables','codehilite','fenced_code','toc'])
    #content = pandoc.read(text) 
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(G_HTML_HEAD)
        f.write(html)

# def write_html2(filename,text):
#     html = markdown2.markdown(text, extras=["fenced-code-blocks","tables","toc"])
#     #content = pandoc.read(text)
#     with open(filename, 'w', encoding="utf-8") as f:
#         f.write(G_HTML_HEAD)
#         f.write(html)

# def write_pandoc_html(filename,text):
#     html = pypandoc.convert_text(text, 'html', format='md')
#     with open(filename, 'w', encoding="utf-8") as f:
#         f.write(html)