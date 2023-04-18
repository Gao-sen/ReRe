#!/usr/local/bin/python
#coding:utf-8
import os
import sys
import csv
import pprint
import time

with open('catch.csv') as f:
    #检测csv文件总行数
    lineall = len(f.readlines())
    print('～～～Rere正在启动，检测到csv文件共[{0}]行～～～'.format(lineall))
    print('================================================')
#打开fasta文件并读取所有行,储存在内存中
with open('cj.fasta') as f:
    all_lines = f.readlines()
#打开csv文件
with open('catch.csv') as f:
    reader = csv.reader(f)
    #定义所有行
    l = [row for row in reader]
    #遍历csv文件的所有行，y是行序号
    check = 0
    for y in range(0,lineall):
        #读取ABGH
        A = (l[y][0])
        B = (l[y][1])
        G = (l[y][6])
        H = (l[y][7])
        #把读取的GH文字列转换为整数，后面要计算
        G = int(G)
        H = int(H)
        
        count = 1  # 计算行数
        linestart = 0  # 初始化序列所在行的下一行
        for i in all_lines:  # 遍历文件每一行，i表示文件f的i行字符串
            if A in i:  # 查看该行是否有待查字符
                # 有：储存字符所在行count
                print('Rere在文件cj.fasta的第{0}行找到了第{1}个序列'.format(count, (y+1)))
                count += 1
                linestart = count  # 获得序列所在行的下一行
                check += 1
            else:
        # 没有：继续搜索下一行
                count += 1

        # 切片，把序列的下一行开始，到H/50+5行截取出来
        data = all_lines[(linestart - 1):(linestart + H//50 + 5)]
        # 转换成文字列，并去掉一些乱七八糟的符号
        data = "".join(data).replace("\n", "")
        # 再切片，截取GH
        cut = data[(G-1):H]
        #print(cut)

        #把结果写进results.txt
        with open('results.txt','a+') as r:
            r.write('>')
            r.write(A)
            r.write(B)
            r.write('\r\n')
            r.write(cut)
            r.write('\r\n')
            print('Rere在文件{0}中添加了第{1}个序列的结果'.format('results.txt', (y+1)))
        #检查是否在cj.fasta中找到序列
        if check == (y+1):#找到了
            print('================================================')
        else:#没找到
            print('Rere检查到在cj.fasta中未找到第{0}个序列，并添加了空白的结果'.format((y+1)))
            print('Rere自闭了，所以自己关闭了自己，喵喵喵')
            #程序终止
            sys.exit()
        #检查找到的序列总数是否等于csv的行数
        if check == (lineall):
            print('～～～～～～～Rere已经顺利完成任务～～～～～～～')
