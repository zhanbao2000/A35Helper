#!/usr/bin/python
# -*- coding: utf-8 -*- 

import os, codecs

#使用os.getcwdu()摆脱烦人的编码问题
#获取到两个目录下的所有文件
path1 = raw_input("Please enter path 1: ")
os.chdir(path1)
songs1 = os.listdir(os.getcwdu())
path2 = raw_input("Please enter path 2: ")
os.chdir(path2)
songs2 = os.listdir(os.getcwdu())

fo = codecs.open("same.txt", "w", "utf-8")

fo.writelines(path1 + "\n")
fo.writelines(path2 + "\n\n")

#逐个对照，发现重复的就输出
for i in range(0,len(songs1)):
	for j in range(0,len(songs2)):
		if songs1[i] == songs2[j]:
			fo.writelines(songs1[i] + "\n")
			
fo.close()