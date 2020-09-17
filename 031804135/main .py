import numpy as np
import jieba
import sys
import  time
#t = time.time()

def cos_sim(str1, str2) -> float:
    stopwords = {',', ' '}  # 停用词表
    str1_cut = [word for word in jieba.cut(str1) if word not in stopwords]  # 分词
    str2_cut = [word for word in jieba.cut(str2) if word not in stopwords]
    word_list = list(set([word for word in str1_cut + str2_cut]))  # 建立词库
    vec_1 = []
    vec_2 = []
    for word in word_list:
        vec_1.append(str1_cut.count(word))  # 文本1统计在词典里出现词的次数
        vec_2.append(str2_cut.count(word))

    vec_1 = np.array(vec_1)  # 建立稀疏矩阵
    vec_2 = np.array(vec_2)

    # 余弦公式
    num = vec_1.dot(vec_2.T)
    denom = np.linalg.norm(vec_1) * np.linalg.norm(vec_2)
    cos = num / denom
    sim = 0.5 + 0.5 * cos
    return sim

f=open(sys.argv[1],"r",encoding="UTF-8")
s1=f.read()#输入s1
f=open(sys.argv[2],"r",encoding="UTF-8")
s2=f.read()#输入s2
f.close()

f=open(sys.argv[3],"w",encoding="UTF-8")
f.write( str(cos_sim(s1, s2))[0:4] )
f.close()