#!/usr/bin/python
# -*- coding: utf-8 -*- 
# ver 1.0.0

import os
import codecs

list_file = raw_input("Please enter list file: ")
rm_path = raw_input("Please enter remove path: ")

fr = codecs.open(list_file, "r", "utf-8")
# 逐行读取，形成一个列表，每一行是一个元素
lines = [line.strip() for line in fr] 
fr.close()

for i in range(0, len(lines)):
	os.remove(rm_path + "\\" + lines[i])
