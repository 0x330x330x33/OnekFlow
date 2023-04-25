#!/usr/bin/env python
#-*- coding:utf-8 -*- 
# 作者: cc
# 邮箱: cc@qq.com
# 时间: 2023-04-05 21:30:27
# 描述: 整理url，输出使用量

import pandas as pd
from urllib.parse import urlparse

name = "count_url"

def check(packet):
    try:
        url = packet.http.response_for_uri
        code = packet.http.response_code
        length = int(packet.http.content_length)
        return url,code,length
    except AttributeError:
        pass
    except Exception as e:
        raise e
    return None

def report(datas):
    response_url_list = []
    response_code_list = []
    response_length_list = []
    for data in datas:
        response_url_list.append(data[0])
        response_code_list.append(data[1])
        response_length_list.append(data[2])
    df_response = pd.DataFrame({'URL': response_url_list,'Status': response_code_list, 'Length': response_length_list})
    df_response['URL without Params'] = df_response['URL'].apply(lambda x: urlparse(x)._replace(query=None).geturl())
    df_url_top10 = df_response.groupby(['URL without Params']).size().reset_index(name='Count').nlargest(10, 'Count')
    df_url_len_top10 = df_response.groupby(['URL without Params','Status', 'Length']).size().reset_index(name='Count').nlargest(20, 'Count')
    df_url_list = df_response.groupby(['URL','Status', 'Length']).size().reset_index(name='Count')
    markdown_text = f"""
## URL TOP10 统计

{df_url_top10.to_markdown(index=False)}

## URL&长度 TOP20 统计

{df_url_len_top10.to_markdown(index=False)}

## URL清单

{df_url_list.to_markdown(index=True)}

"""
    return markdown_text


