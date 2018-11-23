# 思路
    # 1. 每个测试样例属于某个类别的概率 = 某个类别中出现样例中词的概率 * 某个类别的概率
    # 2. 取最大的概率
import os
from collections import defaultdict
import nltk
import re
from nltk.stem.lancaster import LancasterStemmer
from nltk.corpus import stopwords as pw
import json
lancaster_stemmer = LancasterStemmer()
LanStem = nltk.LancasterStemmer
cacheStopWords = pw.words("english")



def get_Number(class_list):
    class_sum = 0
    for class_every in class_list:
        class_path = path1 + '/' + class_every
        file_list = os.listdir(class_path)
        # print(class_path)
        # for file in file_list:
        class_sum = class_sum + 0.8*len(file_list)
        # print('class_sum', class_sum)
    return class_sum


def getP_class(class_every, class_sum):
    file_list = os.listdir(class_every)
    class_num = 0.8*len(file_list)
    # print('class_num', class_num)
    P_class = float(class_num) / float(class_sum)
    return P_class


def filtWords(word):  # 过滤单词
    new_word = []
    word.lower()
    word = re.sub(r'[^\w\s]', " ", word)  # 去标点符号
    word = re.sub(r'\s{2,}', '', word)  # 去除两个以上空格
    if word not in cacheStopWords and word != ' ':  # 去停用词
        new_word.append(lancaster_stemmer.stem(word))  # 寻找词根
        # new_word.append(word)
    # print(new_word)
    return new_word


def get_word_freq(file_path, word_freq):
    with open(file_path, 'r', encoding='UTF-8', errors='ignore') as f:
        for line in f.readlines():
            line = line.strip()  # 去掉左边空格
            sents = nltk.sent_tokenize(line)  # 分句
            # print(sents)
            for sent in sents:
                words = nltk.wordpunct_tokenize(sent)
                for word in words:
                    word2 = filtWords(word)  # 对单词进行过滤
                    # print(word2)
                    # break
                    word3 = ''.join(word2)
                    word_freq[word3] += 1
    return word_freq


def get_Condition_P(class_path):
    file_list = os.listdir(class_path)
    word_num = 0
    word_freq = defaultdict(int)
    # for file in file_list:
    for i in range(0, int(0.8*len(file_list))):
        file_path = class_path + '/' + file_list[i]
        # print(file_path)
        get_word_freq(file_path, word_freq)
    return word_freq
    # print(word_freq)


path1 = "../DataSet/20news-18828"
path2 = "Bayes"
class_list = os.listdir(path1)

# print(class_list)
class_sum = get_Number(class_list)
# print('class_sum', class_sum)
for class_every in class_list:
    word_sum = 0
    class_path = path1 + '/' +class_every
    P_class = getP_class(class_path, class_sum)
    # print(class_every + ':' + str(P_class))
    word_freq = get_Condition_P(class_path)
    # break
    for i in word_freq.keys():
        word_sum += word_freq[i]
    del word_freq['']
    for i in word_freq.keys():
        word_freq[i] = word_freq[i]/word_sum
    word_freq['P_class'] = P_class
    # print(len(word_freq.keys()))
    # print(word_freq)
    # break
    path_preserve = path2 + '/' + class_every + '.json'
    #
    with open(path_preserve, 'w') as f2:
        json_str = json.dumps(word_freq)
        f2.write(json_str)
    # break
