#!/usr/bin/python
# coding:utf-8
# ver 0.0.10

import os, codecs

test_path = u"H:\\Developer\\Python\\A35Helper\\testfile\\Poppin'Party - 走り始めたばかりのキミに.lrc"

def gettime(char):
	try:
		result = int(char[1:3])*60 + float(char[4:9])
	except:
		result = -1
	return result

def rebuild(file_path):
	fr = codecs.open(file_path, "r", "utf-8")
	lrcs = [line.strip() for line in fr] 
	fr.close()
	
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

print lrc_files[0]

for i in range(0, len(lrc_files)):
	if lrc_files[i][-4:] != ".lrc": continue
	rebuild(lrc_files[i])