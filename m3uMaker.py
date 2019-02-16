#!/usr/bin/python
# coding:utf-8

import os, codecs

songs = os.listdir(os.getcwdu())
fo = codecs.open("1.m3u", "w", "utf-8")

fo.writelines("#EXTM3U\n")

for i in range(0,len(songs)):
	if songs[i][-4:] == ".mp3":
		fo.writelines("#EXTINF:,\n")
		fo.writelines(songs[i] + "\n")

fo.close()

