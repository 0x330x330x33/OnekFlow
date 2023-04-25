#!/usr/bin/env python
#-*- coding:utf-8 -*- 
# 作者: cc
# 邮箱: cc@qq.com
# 时间: 2023-04-05 21:30:27
# 描述: 整理url，输出使用量

import pandas as pd
from Config import G_KEYWORDS
from FUtils import printable_str,mk_hexkeys
import re
name = "find_key"

def check(packet):
    try:
        payload = packet.tcp.payload.raw_value
        key_list = ""
        keycontent_list = ""
        keys = mk_hexkeys(G_KEYWORDS)
        for key,keyhex in keys.items():
            if keyhex in payload:
                key_list += key + " "
                #print(key,keyhex)
                #print(payload)
                rex = r'.{0,20}%s.{0,20}'%keyhex
                #print(rex)
                finded = re.findall(rex,payload)
                #print(finded)
                keycontent_list += printable_str(bytes.fromhex(finded[0]))
                #print("Packet number:", packet.number, "contains keyword:", key)
        if len(key_list)>0:
            return key_list,keycontent_list,int(packet.number)
    except AttributeError:
        pass
    except Exception as e:
        raise e
    return None

def report(datas):
    list_keywords = []
    list_keycontent = []
    list_steam_id = []
    for data in datas:
        keyword = data[0]
        content = data[1]
        steam_id = data[2]
        #print("find key: %s in %d"%(keyword,steam_id))
        list_keywords.append(keyword)
        list_keycontent.append(content)
        list_steam_id.append(steam_id)
    df_keywords = pd.DataFrame({'key': list_keywords,'content':list_keycontent,'frame.number': list_steam_id})
    markdown_text = f"""
## 发现关键字

{df_keywords.to_markdown(index=True)}

"""
    return markdown_text


