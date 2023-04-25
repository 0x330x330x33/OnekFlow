#!/usr/bin/env python
#-*- coding:utf-8 -*- 
# 作者: cc
# 邮箱: cc@qq.com
# 时间: 2023-04-07 23:09:12
# 描述: todo ...

import pyshark
from tqdm import tqdm


def load_flow(filename,filter=None):
    traffic_data = []
    if filter:
        cap = pyshark.FileCapture(filename, keep_packets=False,display_filter=filter)
    else:
        cap = pyshark.FileCapture(filename, keep_packets=False)
    total_packets = len(cap)
    for packet in tqdm(cap, total=total_packets, desc="Loading packets"):
        # Append the packet to the traffic_data list
        traffic_data.append(packet)
    return traffic_data


filename = "sql.pcapng"

#traffic_data = load_flow(filename,filter="modbus")
#for packet in traffic_data:
for packet in pyshark.FileCapture(filename,display_filter=''):
    try:
        print(packet.http.file_data)
        #print(dir(packet.length))
        #print(packet.DATA.usb_capdata)
        #print(dir(packet.DATA))
        #print(packet.usb.capdata)
        # #print(packet.s7comm.data_item)
        # print(packet.s7comm.param_func)
        # #print(packet.s7comm.resp_data.raw_value)
        # #print(dir(packet.s7comm.data_item))
        # # print(packet.s7comm.param_func)
        # #print(packet.s7comm.data.Data)
        # #print(packet.s7comm.func_code)
        # #print(packet.s7comm.field_names)
    except AttributeError:
        pass
    except Exception as e:
        raise e
    