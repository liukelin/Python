#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PIL import Image,ImageEnhance,ImageFilter # Pillow
import pytesseract # 验证码识别库 依赖PIL、tesseract-ocr 库 （sudo apt-get install tesseract-ocr）(http://www.cnblogs.com/liuqing0328/p/5914074.html)

'''
 安装 pytesseract环境
 http://blog.csdn.net/a349458532/article/details/51490291
'''

# http://www.pythonclub.org/project/captcha/python-pil
image_name = "code/1.jpeg"

def test_1():
    # 1.验证码图片二值化，去噪
    im = Image.open(image_name)
    im = im.filter(ImageFilter.MedianFilter())
    enhancer = ImageEnhance.Contrast(im)
    im = enhancer.enhance(2)
    im = im.convert('1')
    im.show() # 预览图
    return

    # 2.验证码图片字模提取
    s = 12          #start postion of first number
    w = 10          #width of each number
    h = 15          #end postion from top
    t = 2           #start postion of top
     
    im_new = []
    #split four numbers in the picture
    for i in range(4):
        im1 = im.crop((s+w*i+i*2,t,s+w*(i+1)+i*2,h))
        im_new.append(im1)
     
    f = open("data.txt","a")
    for k in range(4):
        l = []
        #im_new[k].show()
        for i in range(13):
            for j in range(10):
                if (im_new[k].getpixel((j,i)) == 255):
                    l.append(0)
                else:
                    l.append(1)
     
        f.write("l=[")
     
        n = 0
        for i in l:
            if (n%10==0):
                f.write("\n")
            f.write(str(i)+",")
            n+=1
        f.write("]\n")

def check_code(image_name):
    im = Image.open(image_name)
    vcode = pytesseract.image_to_string(im)
    print ("=%s=" % vcode)


# 分割字符
def fenge(img):
    img = Image.open(img)
    j = 1
    for i in range(5): 
        x = 14 + i*18    # 起始X坐标 这里的数字参数需要自己
        y = 5           # 起始Y坐标 根据验证码图片的像素进行
        x_size = x+20    # 宽度
        y_size = y+60    # 长度
        img.crop((x, y, x_size, y_size)).save("code/%d.gif" % j)   #适当的修改
        j = j+1

if __name__=='__main__':
    # fenge(image_name)
    check_code('code/genimage.png')










