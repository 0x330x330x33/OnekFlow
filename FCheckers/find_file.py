#!/usr/bin/env python
#-*- coding:utf-8 -*- 
# 作者: cc
# 邮箱: cc@qq.com
# 时间: 2023-04-05 21:30:27
# 描述: ...

import pandas as pd
from Config import keyfile_signatures

name = "find_file"

def check(packet):
    try:
        payload = packet.tcp.payload.raw_value
        file_list = ""
        for key in keyfile_signatures.keys():
            for sign in keyfile_signatures[key]:
                if sign in payload:
                    file_list += "%s[sing: %s]"%(key,sign)
                    #print("find file: %s"%key)
                    break
        if len(file_list)>0:
            return file_list,int(packet.number)
    except AttributeError:
        pass
    except Exception as e:
        raise e
    return None

def report(datas):
    list_files = []
    list_steam_id = []
    for data in datas:
        files = data[0]
        steam_id = data[1]
        #print("find files: %s in %d"%(files,steam_id))
        list_files.append(files)
        list_steam_id.append(steam_id)
    df_files = pd.DataFrame({'files': list_files,'frame.number': list_steam_id})
    markdown_text = f"""
## 发现文件类型

{df_files.to_markdown(index=True)}

"""
    return markdown_text


