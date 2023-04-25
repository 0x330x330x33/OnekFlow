#!/usr/bin/env python
#-*- coding:utf-8 -*- 
# 作者: cc
# 邮箱: cc@qq.com
# 时间: 2023-04-05 21:30:27
# 描述: one checker
import hexdump
from FUtils.FTools import printable_str,str_lines
name = "modbus_dump"


def check(packet):
    try:
        func_code = packet.modbus.func_code
        datas = packet.tcp.payload.raw_value
        if func_code=="16":
            return datas
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
    text_clear = printable_str(text_data)

    raw_dump = hexdump.hexdump(text_data,result='return')
    markdown_text = f"""
## Modbus 原始数据

```
{str_lines(text_clear,linesize=160)}
```

## Modbus hexdump

```
{raw_dump}
```

"""
    return markdown_text


