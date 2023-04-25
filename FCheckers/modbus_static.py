#!/usr/bin/env python
#-*- coding:utf-8 -*- 
# 作者: cc
# 邮箱: cc@qq.com
# 时间: 2023-04-05 21:30:27
# 描述: one checker
import pandas as pd

name = "modbus_static"

def check(packet):
    try:
        func_code = packet.modbus.func_code
        length = packet.length
        return func_code,length
    except AttributeError:
        pass
    except Exception as e:
        raise e
    return None


def report(datas):
    func_code_list = []
    length_list = []
    for data in datas:
        func_code_list.append(data[0])
        length_list.append(data[1])
    df_protocol = pd.DataFrame({'Func Code': func_code_list,'Length': length_list})
    df_protocol_len = df_protocol.groupby(['Func Code','Length']).size().reset_index(name='Count')
    markdown_text = f"""
## ModBus 协议分析

{df_protocol_len.to_markdown(index=True)}


"""
    return markdown_text


