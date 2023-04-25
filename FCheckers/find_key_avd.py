#!/usr/bin/env python
#-*- coding:utf-8 -*- 
# 作者: cc
# 邮箱: cc@qq.com
# 时间: 2023-04-05 21:30:27
# 描述: 尝试找出间隔 flag形式

import pandas as pd
from Config import G_KEYWORDS
from FUtils import printable_str,mk_hexkeys
import re

name = "find_key_avd"

def check(packet):
    try:
        payload = packet.tcp.payload.raw_value
        key_list = ""
        keycontent_list = ""
        keywords_hex = mk_hexkeys(G_KEYWORDS)
        for key,keyhex in keywords_hex.items():
            keyhex_av = ""
            for i in range(0,len(keyhex),2):
                keyhex_av += keyhex[i:i+2] + ".."
            keyhex_av = keyhex_av[:-2]
            #print(keyhex_av)
            finded = re.findall(keyhex_av,payload)
            #print("finded")
            if len(finded)>0:
                key_list += key
                #print(key,keyhex)
                #print(payload)
                rex = r'.{0,20}%s.{0,20}'%keyhex_av
                #print(rex)
                finded = re.findall(rex,payload)
                keycontent_list += printable_str(bytes.fromhex(finded[0]))
        if len(key_list)>0:
            #return key_list,int(packet.number)
            return key_list,keycontent_list,packet.number
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
        list_keywords.append(keyword)
        list_keycontent.append(content)
        list_steam_id.append(steam_id)
    #df_keywords = pd.DataFrame({'key': list_keywords,'frame.number': list_steam_id})
    df_keywords = pd.DataFrame({'key': list_keywords,'content':list_keycontent,'frame.number': list_steam_id})
    markdown_text = f"""
## 高阶关键字

{df_keywords.to_markdown(index=True)}

"""
    return markdown_text


