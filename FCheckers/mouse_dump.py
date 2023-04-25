#!/usr/bin/env python
#-*- coding:utf-8 -*- 
# 作者: cc
# 邮箱: cc@qq.com
# 时间: 2023-04-05 21:30:27
# 描述: one checker
import matplotlib.pyplot as plt
from Config import G_TMP_DIR
from FUtils import mkdir
name = "mouse_dump"

def check(packet):
    try:
        urb_type = packet.usb.transfer_type
        datas = packet.DATA.usb_capdata
        if urb_type=="0x00000001":
            return datas
    except AttributeError:
        pass
    except Exception as e:
        raise e
    return None

def draw_pic(X,Y,imgfile):
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.scatter(X, Y, c='r', marker='o')
    plt.savefig(imgfile)

def draw_mouse(datas,action="ALL"):
    mousePositionX = 0
    mousePositionY = 0
    X = []
    Y = []
    for i in datas:
        if len(i) == 8:
            i = re.sub(r"(?<=\w)(?=(?:\w\w)+$)", ":", i)  
        Bytes = i.split(":")
        if len(Bytes) == 8:
            horizontal = 2  # -
            vertical = 4  # |
        elif len(Bytes) == 4:
            horizontal = 1  # -
            vertical = 2  # |
        else:
            continue
        offsetX = int(Bytes[horizontal], 16)
        offsetY = int(Bytes[vertical], 16)
        if offsetX > 127:
            offsetX -= 256
        if offsetY > 127:
            offsetY -= 256
        mousePositionX += offsetX
        mousePositionY += offsetY
        if Bytes[0] == "01":
            # print "[+] Left butten."
            if action == "LEFT":
                # draw point to the image panel
                X.append(mousePositionX)
                Y.append(-mousePositionY)
        elif Bytes[0] == "02":
            # print "[+] Right Butten."
            if action == "RIGHT":
                # draw point to the image panel
                X.append(mousePositionX)
                Y.append(-mousePositionY)
        elif Bytes[0] == "00":
            # print "[+] Move."
            if action == "MOVE":
                # draw point to the image panel
                X.append(mousePositionX)
                Y.append(-mousePositionY)
        else:
            # print "[-] Known operate."
            pass
        if action == "ALL":
            # draw point to the image panel
            X.append(mousePositionX)
            Y.append(-mousePositionY)
    return X,Y

def report(datas):
    tmp_path = G_TMP_DIR
    mkdir(tmp_path)
    X,Y = draw_mouse(datas,action='LEFT')
    draw_pic(X,Y,tmp_path+"/"+'mouse_left.jpg')
    X,Y = draw_mouse(datas,action='RIGHT')
    draw_pic(X,Y,tmp_path+"/"+'mouse_right.jpg')
    X,Y = draw_mouse(datas,action='MOVE')
    draw_pic(X,Y,tmp_path+"/"+'mouse_move.jpg')
    X,Y = draw_mouse(datas,action='ALL')
    draw_pic(X,Y,tmp_path+"/"+'mouse_all.jpg')
    markdown_text = f"""
## 鼠标路径分析

![鼠标left]({tmp_path+"/"}mouse_left.jpg)
![鼠标right]({tmp_path+"/"}mouse_right.jpg)
![鼠标move]({tmp_path+"/"}mouse_move.jpg)
![鼠标all]({tmp_path+"/"}mouse_all.jpg)

"""
    return markdown_text


