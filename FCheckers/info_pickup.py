#!/usr/bin/env python
#-*- coding:utf-8 -*- 
# 作者: cc
# 邮箱: cc@qq.com
# 时间: 2023-04-05 21:30:27
# 描述: 整理url，输出使用量

import pandas as pd

name = "info_pickup"

def check(packet):
    try:
        #payload = packet.tcp.payload.raw_value
        # datas = packet.tcp.urgent_pointer.hex_value
        # datas = "%02x"%datas
        frame_len = packet.tcp.len
        if frame_len==106:
            return "1"
        #return datas
        return "0"
    except AttributeError:
        pass
    except Exception as e:
        raise e
    return None

def report(datas):
    keydata = ""
    for data in datas:
        keydata += data
    key_text = bytes.fromhex(keydata)
    key_text_clear = key_text.replace(b"\x00",b"..")
    print("pickup data: %s"%(keydata))
    # print("pickup data: %s"%(key_text))
    # print("pickup data: %s"%(key_text_clear))
    markdown_text = f"""
## 特殊位收集

{keydata}

"""
    return markdown_text
#     markdown_text = f"""
# ## 特殊位收集
# {keydata}
# ```
# {key_text}
# {key_text_clear}
# ```
#"""
    


