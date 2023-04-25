#!/usr/bin/env python
#-*- coding:utf-8 -*- 
# 作者: cc
# 邮箱: cc@qq.com
# 时间: 2023-04-05 21:30:27
# 描述: one checker
import pandas as pd

name = "s7comm_static"

def check(packet):
    try:
        header_rosctr = packet.s7comm.header_rosctr
        try:
            param_func = packet.s7comm.param_func
        except AttributeError:
            param_func = "NaN"
        except Exception as e:
            raise e
        length = packet.length
        return header_rosctr,param_func,length
    except AttributeError:
        pass
    except Exception as e:
        raise e
    return None



def report(datas):
    header_rosctr_list = []
    param_func_list = []
    length_list = []
    for data in datas:
        header_rosctr_list.append(data[0])
        param_func_list.append(data[1])
        length_list.append(data[2])
    df_protocol = pd.DataFrame({'ROSCTR': header_rosctr_list,'FUNC': param_func_list,'Length': length_list})
    df_protocol_len = df_protocol.groupby(['ROSCTR','FUNC','Length']).size().reset_index(name='Count')
    markdown_text = f"""
## S7COMM 协议分析

{df_protocol_len.to_markdown(index=True)}


"""
    return markdown_text


