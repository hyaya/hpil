#!coding:utf8
# 2016年3月17日10:36:44
import Image
im = Image.open('l.jpg')
print "图片源格式：",im.format#图片源格式
print "图片大小：",im.size#图片大小(宽，高)
print "图片色彩模式：",im.mode#RGB，L,CMTK
print im.getcolors(im.size[0]*im.size[1])
