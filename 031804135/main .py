import numpy as np
import os
import jieba
import sys
import psutil

arg0=sys.argv[0]# 传的是执行的py文件名
arg1=sys.argv[1]# 传的是命令行的第一个参数
arg2=sys.argv[2]# 传的是命令行的第二个参数
arg3=sys.argv[3]# 传的是命令行的第三个参数

def read(path):
    wds = []
    try:
        with open(path, 'r', encoding='utf-8') as f:
            wds = f.readlines()
            f.close()
    except Exception:
        with open(path, 'r', encoding='gbk') as f:
            wds = f.readlines()
            f.close()
    return wds

def cos_sim(str1, str2) -> float:
    str1 = read(str1)
    str2 = read(str2)
    stopwords = {',',' '}  # 停用词表
    str1_cut = [word for word in jieba.cut(str1) if word not in stopwords]# 分词
    str2_cut = [word for word in jieba.cut(str2) if word not in stopwords]
    word_list = list(set([word for word in str1_cut + str2_cut]))# 建立词库
    vec_1 = []
    vec_2 = []
    for word in word_list:
        vec_1.append(str1_cut.count(word))# 文本1统计在词典里出现词的次数
        vec_2.append(str2_cut.count(word))

    vec_1 = np.array(vec_1)# 建立稀疏矩阵
    vec_2 = np.array(vec_2)

    # 余弦公式
    num = vec_1.dot(vec_2.T)
    denom = np.linalg.norm(vec_1) * np.linalg.norm(vec_2)
    cos = num / denom
    sim = 0.5 + 0.5 * cos
    return sim

def Analyze():
    print(u'当前进程的内存使用：%.4f MB' % (psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024) )
    print(u'当前进程的使用的CPU时间：%.4f s' % (psutil.Process(os.getpid()).cpu_times().user) )

degree = cos_sim(arg1, arg2)
ans = open(arg3, 'w', encoding='utf-8')  # 覆盖添加答案文件
ans.write(str("%.2f%%" % (degree * 100)))
ans.close()  # 关闭文件

