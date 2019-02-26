#!/usr/bin/python
# coding:utf-8

import os
import codecs

# 使用os.getcwdu()摆脱烦人的编码问题
songs = os.listdir(os.getcwdu())
fo = codecs.open("1.m3u", "w", "utf-8")

fo.writelines("#EXTM3U\n")

for i in range(0, len(songs)):
	# 检查是不是mp3文件
	if songs[i][-4:] == ".mp3":
		# 写入列表
		fo.writelines("#EXTINF:,\n")
		fo.writelines(songs[i] + "\n")

fo.close()
