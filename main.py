#!/usr/bin/env python
#-*- coding:utf-8 -*- 
# 作者: cc
# 邮箱: cc@qq.com
# 时间: 2023-04-05 20:49:05
# 描述: start point

from FCore import analyse,dump_by_url,dump_by_keyword,dump_by_keylen
from FCheckers import count_protocol_simple,count_protocol,count_url,count_url_simple,find_key,find_file,find_key_avd, modbus_static,modbus_dump,longhex,s7comm_dump,s7comm_static,mouse_dump,keyboard_dump
import argparse

allcheckers = [
    count_protocol_simple,
    count_protocol,
    find_key,
    find_key_avd,
    find_file,
    modbus_static,
    modbus_dump,
    s7comm_static,
    s7comm_dump,
    longhex,
    mouse_dump,
    keyboard_dump,
    count_url,
]

simple_checkers = [
    count_protocol_simple,
    find_key,
    find_key_avd,
    find_file,
    # info_pickup,
    # check_sql,
    # check_sql_keyword,
    # modbus_static,
    # modbus_dump,
    # s7comm_static,
    # s7comm_dump,
    longhex,
    # mouse_dump,
    # keyboard_dump,
    count_url_simple,
]

def main(filename,filter,scanbin,isDev):
    analyse(filename,filter,simple_checkers,scanbin=scanbin,isDev=isDev)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='one key analyse pcap.')
    parser.add_argument('filename', type=str, help='filename')
    parser.add_argument('-q', dest='query', type=str, help='query is filter of wireshark')
    parser.add_argument('-a', dest='all', action="store_true", help='use all checkers')
    parser.add_argument('--url', dest='url', type=str, help='dump urls into a csv file')
    parser.add_argument('--sqlikey', dest='sqlikey', type=str, help='find sqli paquet by keyword')
    parser.add_argument('--sqlilen', dest='sqlilen', type=int, help='find sqli paquet by lenght')
    parser.add_argument('--dev', dest='dev', action="store_true", help='do dev mode, load less packets for save time')
    #parser.add_argument('--scanbin', dest='scanbin', action="store_true", help='do dev mode, load less packets for save time')
    parser.add_argument('--s7comm', dest='s7comm', action="store_true", help='for s7comm protocol')
    parser.add_argument('--modbus', dest='modbus', action="store_true", help='for modbus protocol')
    parser.add_argument('--usb', dest='usb', action="store_true", help='for usb protocol')
    args = parser.parse_args()
    if args.all:
        analyse(args.filename,None,allcheckers,scanbin=True)
    elif args.url:
        print("in url mode, url: %s"%args.url)
        dump_by_url(args.filename,args.url)
    elif args.sqlikey:
        dump_by_keyword(args.filename,args.sqlikey)
    elif args.sqlilen:
        dump_by_keylen(args.filename,args.sqlilen)
    elif args.s7comm:
        analyse(args.filename,'s7comm',[s7comm_static,longhex,s7comm_dump])
    elif args.modbus:
        analyse(args.filename,'modbus',[modbus_static,longhex,modbus_dump])
    elif args.usb:
        analyse(args.filename,'usb',[mouse_dump,keyboard_dump])
    elif args.dev:
        analyse(args.filename,None,allcheckers,scanbin=True,isDev=True)
    else:
        analyse(args.filename,args.query,simple_checkers,scanbin=False)
        #main(args.filename,filter=args.query,scanbin=True,isDev=args.dev)




