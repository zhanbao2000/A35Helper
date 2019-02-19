#!/usr/bin/python
# coding:utf-8
# ver 1.1.0

import os, codecs

def gettime(char):
#获取歌词行所在时间轴坐标（单位：秒）
	try:
		result = int(char[1:3])*60 + float(char[4:9])
	except:
		result = -1
	return result

def rebuild(file_path):
	fr = codecs.open(file_path, "r", "utf-8")
	try:
		#读取歌词行到列表
		lrcs = [line.strip() for line in fr] 
	except UnicodeDecodeError :
		#防止奇奇怪怪的歌名不能被UnicodeDecoder解码，抛错误直接return
		return
	fr.close()
	
	#列表内部调整
	i = 0
	while i < len(lrcs)-1:
		if gettime(lrcs[i]) > gettime(lrcs[i+1]):
			temp = lrcs.pop(i+1)
			j = 0
			while gettime(temp) > gettime(lrcs[j]): j += 1
			lrcs.insert(j, temp)
			i = 0
			continue
		i += 1
	
	#在写文件的同时，pop掉空行
	fo = codecs.open(file_path, "w", "utf-8")
	i = 0
	while i < len(lrcs):
		if lrcs[i] == u"":
			lrcs.pop(i)
			i += 1
			continue
		fo.writelines(lrcs[i] + "\n")
		i += 1


print ("English path ONLY!!")
lrc_path = raw_input("Please enter LRC path: ")
os.chdir(lrc_path)
lrc_files = os.listdir(os.getcwdu())

for i in range(0, len(lrc_files)):
	#确保只对LRC文件进行操作
	if lrc_files[i][-4:] != ".lrc":continue
	rebuild(lrc_files[i])