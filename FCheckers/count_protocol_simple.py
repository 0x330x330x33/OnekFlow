#!/usr/bin/env python
#-*- coding:utf-8 -*- 
# 作者: cc
# 邮箱: cc@qq.com
# 时间: 2023-04-05 21:30:27
# 描述: one checker
import pandas as pd

name = "count_protocol_simple"

def check(packet):
    try:
        protocol1 = packet.highest_layer
        length = packet.length
        return protocol1,length
    except AttributeError:
        pass
    except Exception as e:
        raise e
    return None


def report(datas):
    protocol1_list = []
    protocol2_list = []
    length_list = []
    for data in datas:
        protocol1_list.append(data[0])
        length_list.append(data[1])
    df_protocol = pd.DataFrame({'Protocol1': protocol1_list,'Length': length_list})
    df_protocol_static = df_protocol.groupby(['Protocol1']).size().reset_index(name='Count')
    df_protocol_top10 = df_protocol.groupby(['Protocol1', 'Length']).size().reset_index(name='Count').nlargest(20, 'Count')
    markdown_text = f"""
## 协议分析(简)

{df_protocol_static.to_markdown(index=True)}

## TOP10 协议包(简)

{df_protocol_top10.to_markdown(index=False)}

"""
    return markdown_text


