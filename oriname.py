# 导入需要的模块
import os
import re

if __name__=='__main__':
    # 定义原始数据集目录路径和处理后数据集目录路径
    Raw_data_set = './a/'
    Processing_data_set = './b/'

    # 获取原始数据集目录下所有文件名，并生成文件路径列表
    Raw_all_files = os.listdir(Raw_data_set)
    Raw_all_files_path = [os.path.join(Raw_data_set, _path) for _path in Raw_all_files]

    # 循环处理每个原始文件
    for index,path in enumerate(Raw_all_files_path):
        # 打开原始文件
        f = open(path)
        # 创建一个新文件，用于写入修改后的内容
        file = open(Processing_data_set+Raw_all_files[index].strip('.fasta') + '.fasta', 'w')

        # 处理原始文件中的每一行
        for line in f:
            # 去除行首行尾空格
            line = line.strip()
            # 搜索行中是否包含">xxx_1_xxx"格式的字符串
            query_res = re.search('>(.*)_1_', line)
            # 如果行中不包含">xxx_1_xxx"格式的字符串，则直接写入新文件
            if query_res is None:
                file.write(line+ '\n')
                continue;
            # 如果行中包含">xxx_1_xxx"格式的字符串，则将"xxx"替换为"NODE"后写入新文件
            else:
                new_line = line.replace(str(query_res.group(1)),"NODE")
                file.write(new_line+ '\n')
        
        # 关闭原始文件和新文件
        f.close()
        file.close()
