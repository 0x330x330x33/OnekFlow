#!/usr/bin/env python
#-*- coding:utf-8 -*- 
# 作者: cc
# 邮箱: cc@qq.com
# 时间: 2023-04-08 22:29:33
# 描述: todo ...
import os
printable = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ '

def str_lines(s,linesize=80):
    out_str = ""
    count = 0
    for c in s:
        count += 1
        if count > linesize:
            out_str += "\n"
            count = 1
        out_str += c
    return out_str

def printable_str(s):
    out_str = ""
    for c in s:
        try:
            tmp_char = chr(c)
            if tmp_char in printable:
                out_str +=tmp_char
            else:
                out_str += '.'
        except Exception as e:
            print(e)
            out_str += '.'
    return out_str

def mk_hexkeys(keys):
    hex_keys = {}
    for k in keys:
        hex_keys[k] = k.encode('utf-8').hex()
        hex_keys[k.upper()] = k.upper().encode('utf-8').hex()
        hex_keys[k.lower()] = k.lower().encode('utf-8').hex()
    return hex_keys


def mkdir(path):
    folder = os.path.exists(path)
    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径

