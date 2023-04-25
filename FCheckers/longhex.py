#!/usr/bin/env python
#-*- coding:utf-8 -*- 
# 作者: cc
# 邮箱: cc@qq.com
# 时间: 2023-04-05 21:30:27
# 描述: 尝试找出间隔 flag形式

import pandas as pd
import re

name = "longhex"

def check(packet):
    try:
        payload = packet.tcp.payload.raw_value
        return payload
        # key_list = ""
        # finded = re.findall("[0-9a-fA-F]{64}",payload)
        # if len(finded)>0: 
    except AttributeError:
        pass
    except Exception as e:
        raise e
    return None



def report(datas):
    raw_data = ""
    for data in datas:
        raw_data += data
    text_data = bytes.fromhex(raw_data)
    finded = re.findall(b"[0-9a-fA-F]{32,100}",text_data)
    hexlong_list = []
    for f in finded:
        hexlong_list.append(f)
    df_hexlong = pd.DataFrame({'data': hexlong_list})
    markdown_text = f"""
## 长16进制字符串搜索
位置自己去wireshark找吧

{df_hexlong.to_markdown(index=False)}

"""
    return markdown_text


