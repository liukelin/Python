#!/usr/bin/env python
# coding=utf-8
import os
import sys
import subprocess


QRImagePath = os.path.join(os.getcwd(), 'image.jpg')
# os.startfile(QRImagePath)
weichatPath = '/Applications/微信.app'

#各种操作系统打开图片窗口
if sys.platform.find('darwin') >= 0:
    # subprocess.call(['open', QRImagePath])
    subprocess.call(['open', weichatPath])

    print('1')
elif sys.platform.find('linux') >= 0:
    subprocess.call(['xdg-open', QRImagePath])
    print('2')
else:
    os.startfile(QRImagePath)

print('请使用微信扫描二维码以登录')

