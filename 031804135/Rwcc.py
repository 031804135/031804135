import numpy as np
import os
import jieba
def read_txt(path):#文本读取
    files = os.listdir(path)  # 得到文件夹下的所有文件名称
    list_txt = []  # 存放文本
    for file in files:  # 遍历文件夹
        if not os.path.isdir(file):  # 判断是否是文件夹，不是文件夹才打开
            f = open(path + "\\" + file, encoding='UTF-8')  # 打开文件
            iter_f = iter(f)  # 创建迭代器
            str = ''
            for line in iter_f:  # 遍历文件，一行行遍历，读取文本
                str = str + line
            list_txt.append(str)  # 每个文件的文本存到list中
    return list_txt

def cos_sim(str1: str, str2: str) -> float:
    stopwords = {":", "的", "，", "’", '\n', ' ', '、', '。', '：', '“'}  # 停用词表
    str1_cut = [word for word in jieba.cut(str1) if word not in stopwords]#分词
    str2_cut = [word for word in jieba.cut(str2) if word not in stopwords]
    word_list = list(set([word for word in str1_cut + str2_cut]))#建立词库
    vec_1 = []
    vec_2 = []
    for word in word_list:
        vec_1.append(str1_cut.count(word))#文本1统计在词典里出现词的次数
        vec_2.append(str2_cut.count(word))

    vec_1 = np.array(vec_1)#建立稀疏矩阵
    vec_2 = np.array(vec_2)

    #余弦公式
    num = vec_1.dot(vec_2.T)
    denom = np.linalg.norm(vec_1) * np.linalg.norm(vec_2)
    cos = num / denom
    sim = 0.5 + 0.5 * cos
    return sim

def main():
    path = 'C:\\Users\\Administrator\\Desktop\\sim_0.8'  # 文件夹路径
    list_doc = read_txt(path)#读取文本
    str1 = list_doc[0]#原文本
    t = 0
    for str in list_doc :#循环对比
        if t != 0:
            sim = cos_sim(str1, str)
            print("sim ：{0:.2f}".format(sim))
        else:
            t+=1

main()
