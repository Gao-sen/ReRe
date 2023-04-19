#!/usr/local/bin/python # 声明所用的Python解释器路径
#coding:utf-8   # 声明且编码格式必须为UTF-8
import os,sys  # 导入os和sys模块
import csv # 导入csv模块，截取的序列的信息表为csv格式
import pprint

#打开csv文件
with open('catch.csv') as f:
    #检测csv文件总行数
    lineall = len(f.readlines())
    print('================================================')
    print('～～～ReRe正在启动，检测到csv文件共[{0}]行～～～'.format(lineall))
    print('================================================')
    
#打开fasta文件并读取所有行的列表,储存在内存中
print('～～～～～～ReRe正在读取fasta文件～～～～～～')
with open('cj.fasta') as f:
    all_lines = f.readlines()
#检测fasta文件的总行数   
num_lines = len(all_lines)
print(f'～～～ReRe检测到fasta文件一共{num_lines}行～～～')
print('================================================')

#打开csv文件
with open('catch.csv') as f:
    reader = csv.reader(f)
    #定义所有行
    l = [row for row in reader]
    #遍历csv文件的所有行，y是行序号
    check = 0
    for y in range(0,lineall):
        #读取B、G、H列。B为contig名称，G、H：待截取的目的序列在contig序列中的start、end位置
        A = (l[y][0])
        B = (l[y][1])
        G = (l[y][6])
        H = (l[y][7])
        #把读取的GH文字列转换为整数，后面要计算字符位置
        G = int(G)
        H = int(H)
        
        count = 1  # 计算行数
        linestart = 0  # 初始化序列所在行的下一行
        for i in all_lines:  # 遍历genome集文件的每一行，i表示文件的第i行字符串
            if B in i:  # 查看该行是否有csv中的B列字符串（查找contig名称）
                # 有：储存字符所在行count
                print('ReRe在文件cj.fasta的第{0}行找到了第{1}个序列'.format(count, (y+1)))
                count += 1
                linestart = count  # 获得序列所在行的下一行
                check += 1
            else:
        # 没有：继续搜索下一行
                count += 1

        # 切片，把序列的下一行开始，到fasta的最后一行截取出来，截取的数据类型为列表
        data = all_lines[(linestart - 1):(num_lines + 1)]
        # 将列表转换成文字列，并去掉一些列表转换为文字列产生的乱七八糟的符号
        data = "".join(data).replace("\n", "")
        # 再切片，截取GH
        cut = data[(G-1):H]
        #print(cut)

        #把结果写进results.fasta，可修改为.txt格式。输出的目的序列contig名称格式：“> + A列字符 + B列字符”
        with open('results.fasta','a+') as r:
            r.write('>')
            r.write(A)
            r.write(B)
            r.write('\r\n')
            r.write(cut)
            r.write('\r\n')
            print('ReRe在文件{0}中添加了第{1}个序列的结果'.format('results.fasta', (y+1)))
        #检查是否在cj.fasta中找到序列
        if check == (y+1):#找到了
            print('================================================')
        else:#没找到
            print('ReRe检查到在cj.fasta中未找到第{0}个序列并添加了空白的结果，或者找到了多个该序列'.format((y+1)))
            print('ReRe自闭了，所以自己关闭了自己，喵喵喵')
            #程序终止
            sys.exit()
        #检查找到的序列总数是否等于csv的行数
        if check == (lineall):
            print('～～～～～～～ReRe已经顺利完成任务～～～～～～～')
