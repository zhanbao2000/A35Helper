#!/usr/bin/python
# -*- coding: utf-8 -*- 
# ver 1.0.3

import os
import codecs

# 使用os.getcwdu()摆脱烦人的编码问题
# 获取到两个目录下的所有文件
print ("English path ONLY!!")
path1 = raw_input("Please enter path 1: ")
os.chdir(path1)
songs1 = os.listdir(os.getcwdu())
print ("Load %d files" % len(songs1))
path2 = raw_input("Please enter path 2: ")
os.chdir(path2)
songs2 = os.listdir(os.getcwdu())
print ("Load %d files" % len(songs2))

fo = codecs.open("same.txt", "w", "utf-8")

# 逐个对照，发现重复的就输出
for i in range(0, len(songs1)):
	for j in range(0, len(songs2)):
		if songs1[i] == songs2[j]:
			fo.writelines(songs1[i] + "\n")
			
fo.close()
