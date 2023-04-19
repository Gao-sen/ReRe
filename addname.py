#!/usr/local/bin/python  # 声明所用的Python解释器路径
#coding:utf-8  # 声明且编码格式必须为UTF-8
import os, sys  # 导入os和sys模块

docunames=os.listdir('./all')  # 获取'./all'目录下的所有文件名，存储在docunames列表中，all 可替换

for i in range(len(docunames)):  # 循环遍历docunames列表中的文件名
    with open('all/' + docunames[i], 'r') as f:  # 以只读模式打开'./all'目录下的文件
        data_lines = f.read()  # 读取文件内容并存储在data_lines变量中
        data_lines = data_lines.replace(">",'>'+ docunames[i] + '_')  # 将文件内容中所有的">"查找替换为">—+所属文件名+_"的形式，可根据自己需求更改替换方案
        data_lines = data_lines.replace(".fasta","")  # 将文件名中的".fasta"替换为空字符串，除去文件后缀格式
        
    with open(docunames[i], mode="w") as f:  # 以写入模式打开与原文件同名的新文件
        f.write(data_lines)  # 将修改后的文件内容写入新文件中，输出位置与'./all'路径同源