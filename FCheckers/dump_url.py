#!/usr/bin/env python
#-*- coding:utf-8 -*- 
# 作者: cc
# 邮箱: cc@qq.com
# 时间: 2023-04-05 21:30:27
# 描述: 整理url，输出使用量

import pandas as pd
from urllib.parse import urlparse

name = "check_sql"

def check_byurl(packet,dump_url):
    try:
        url = packet.http.response_for_uri
        code = packet.http.response_code
        length = int(packet.length)
        if dump_url in url:
            iurl = url.replace(dump_url,"")
            return url,iurl,code,length
    except AttributeError:
        pass
    except Exception as e:
        raise e
    return None

def check_bykey(packet,key):
    try:
        url = packet.http.response_for_uri
        code = packet.http.response_code
        length = int(packet.length)
        content = packet.http.file_data
        #keyhex = key.encode('utf-8').hex()
        if key in content:
            urlq = urlparse(url).query
            return url,urlq,code,length
    except AttributeError:
        pass
    except Exception as e:
        raise e
    return None

def check_bylen(packet,pkt_length):
    try:
        url = packet.http.response_for_uri
        code = packet.http.response_code
        length = int(packet.length)
        if pkt_length == length:
            urlq = urlparse(url).query
            return url,urlq,code,length
    except AttributeError:
        pass
    except Exception as e:
        raise e
    return None

def report(datas,savefile):
    response_url_list = []
    response_iurl_list = []
    response_code_list = []
    response_length_list = []
    for data in datas:
        response_url_list.append(data[0])
        response_iurl_list.append(data[1])
        response_code_list.append(data[2])
        response_length_list.append(data[3])
    df_response = pd.DataFrame({'URL': response_url_list,'URL inject': response_iurl_list,'Status': response_code_list, 'frame.len': response_length_list})
    df_response.to_csv(savefile)



