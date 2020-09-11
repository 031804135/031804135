import os
path = 'C:\\Users\\Administrator\\Desktop\\sim_0.8'#文件夹路径
files = os.listdir(path)  # 得到文件夹下的所有文件名称
list = [] #存放文本
for file in files:  # 遍历文件夹
    if not os.path.isdir(file):  # 判断是否是文件夹，不是文件夹才打开
        f = open(path + "\\" + file,encoding='UTF-8')  # 打开文件
        iter_f = iter(f) # 创建迭代器
        str = ''
        for line in iter_f:  # 遍历文件，一行行遍历，读取文本
            str = str + line
        list.append(str)  # 每个文件的文本存到list中
#print(list[4])#测试文本是否读入
