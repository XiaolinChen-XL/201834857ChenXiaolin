# coding: utf-8
import os
import re
import nltk
import math
import json
from nltk.stem.lancaster import LancasterStemmer
from nltk.corpus import stopwords as pw
from collections import defaultdict
lancaster_stemmer = LancasterStemmer()
LanStem = nltk.LancasterStemmer
cacheStopWords = pw.words("english")
path1 = "DataSet/20news-18828"
# path1 = "./DataSet/playground"
path2 = "./DataSet/preserve"
path3 = "./DataSet/vector_train"
path3 = "./DataSet/vector_test"
# vocab = []
IDF1 = defaultdict(int)
dict_all = defaultdict(int)
dict_all3 = defaultdict(int)
IDF_word = defaultdict(int)
TF_word = defaultdict(int)


def filtWords(word):  # 过滤单词
    new_word = []
    word = re.sub(r'[^\w\s]', " ", word)  # 去标点符号
    word = re.sub(r'\s{2,}', '', word)  # 去除两个以上空格
    if word not in cacheStopWords and word != ' ':  # 去停用词
        new_word.append(lancaster_stemmer.stem(word))  # 寻找词根
        # new_word.append(word)
    # print(new_word)
    return new_word


def getVocab(path3):
    vocab = []
    with open(path3, 'r', encoding='UTF-8', errors='ignore') as f:
        for line in f:
            sents = nltk.sent_tokenize(line)  # 分句
            for sent in sents:
                words = nltk.wordpunct_tokenize(sent)  # 分词
                for word in words:
                    word2 = filtWords(word)  # 对单词进行过滤
                    if word2 != ' ':
                        vocab.extend(word2)
        for word in vocab:
            if word != ' ':
                dict_all[word] += 1  # 所有的单词


def getWords(path3):  # 对一个文件进行分句分词，统计词频（TF），构建词库
    vocab = []
    word_freq = defaultdict(int)
    with open(path3, 'r', encoding='UTF-8', errors='ignore') as f:
        word_idf = defaultdict(int)
        for line in f.readlines():
            line = line.lstrip()  # 去掉左边空格
            if line == '\n':
                line = line.strip("\n")
            else:
                sents = nltk.sent_tokenize(line)  # 分句
                # print(sents)
                for sent in sents:
                    # print('sent', sent)
                    words = nltk.wordpunct_tokenize(sent)
                    # print('words', words)
                    for word in words:
                        # print(word)
                        word2 = filtWords(word)  # 对单词进行过滤
                        # print(word2)
                        if word2 != ' ' and word2 != 'com1' and word2 != 'com2' and word2 != 'com3':
                            vocab.extend(word2)
        # for line in f:
        #     sents = nltk.sent_tokenize(line)  # 分句
        #     for sent in sents:
        #         words = nltk.wordpunct_tokenize(sent)  # 分词
        #         for word in words:
        #             # print(word)
        #             word2 = filtWords(word)  # 对单词进行过滤
        #             # print(word2)
        #             if word2 != ' ' and word2 != 'com1' and word2 != 'com2'and word2 != 'com3':
        #                 vocab.extend(word2)        # 构建一个文件中的词库
    # print('---vocab---', vocab)
    for word in vocab:
        if word != ' ':
            dict_all[word] += 1
            # print('----dict_all----, path3', dict_all, path3)
            # word_freq[word] += 1  # 统计词频(TF)
            # if word not in word_idf:
            #     word_idf[word] += 1

    # for k in word_idf.keys():
    #     IDF1[k] += 1  # 包含该词组的文章个数


def getWords2(path3):  # 对一个文件进行分句分词，统计词频（TF），构建词库
    vocab = []
    word_freq = defaultdict(int)
    with open(path3, 'r', encoding='UTF-8', errors='ignore') as f:
        word_idf = defaultdict(int)
        for line in f.readlines():
            line = line.lstrip()  # 去掉左边空格
            if line == '\n':
                line = line.strip("\n")
            else:
                sents = nltk.sent_tokenize(line)  # 分句
                # print(sents)
                for sent in sents:
                    # print('sent', sent)
                    words = nltk.wordpunct_tokenize(sent)
                    # print('words', words)
                    for word in words:
                        # print(word)
                        word2 = filtWords(word)  # 对单词进行过滤
                        # print(word2)
                        if word2 != ' ' and word2 != 'com1' and word2 != 'com2' and word2 != 'com3':
                            vocab.extend(word2)
        # for line in f:
        #     sents = nltk.sent_tokenize(line)  # 分句
        #     for sent in sents:
        #         words = nltk.wordpunct_tokenize(sent)  # 分词
        #         for word in words:
        #             # print(word)
        #             word2 = filtWords(word)  # 对单词进行过滤
        #             # print(word2)
        #             if word2 != ' ' and word2 != 'com1' and word2 != 'com2'and word2 != 'com3':
        #                 vocab.extend(word2)        # 构建一个文件中的词库
    # print('---vocab---', vocab)
    for word in vocab:
        if word != ' ':
            # dict_all[word] += 1
            # print('----dict_all----, path3', dict_all, path3)
            word_freq[word] += 1  # 统计词频(TF)
            if word not in word_idf:
                word_idf[word] += 1

    for k in word_idf.keys():
        IDF1[k] += 1  # 包含该词组的文章个数
    return word_freq, IDF1


def getFileNum(dirs1):
    filenumber = 0
    for file in dirs1:
        path2 = path1 + '/' + file
        # print(path2)
        dirs2 = os.listdir(path2)
        filenumber += len(dirs2)
    # print(filenumber)
    return filenumber


def getIDF(Idf, filenumber):
    for word in Idf.keys():
        if word in dict_all3.keys():
            print(word)
            filenumber_word = Idf[word]  # 包含词组的文档总数
            fenmu = float(filenumber_word) + 1
            # dict1 = defaultdict(int)
            idf_word = math.log(float(filenumber)/fenmu)
            IDF_word[word] = idf_word
            path_preserve = path2 + '/' + word + '.json'
            try:
                with open(path_preserve, 'r') as f:
                    b = json.load(f)
                    b['IDF'] = idf_word
                    # f.write(str(dict1))  # 将IDF写入文档
                with open(path_preserve, 'w') as f1:
                    json.dump(b, f1, ensure_ascii=False)
            except (FileNotFoundError, PermissionError, OSError, json.decoder.JSONDecodeError) as e:
                print('except', e)


def getTF(vocab, number, path):  # 得到每个文件的TF
    for word in vocab.keys():
        num_word = float(vocab[word])
        TF = num_word/float(number)
        TF_word[word] = TF
        dict2 = defaultdict(int)
        dict2[path] = TF
        path_preserve = path2 + '/' + word + '.json'
        if os.path.exists(path_preserve):
            with open(path_preserve, 'r') as f:
                # for lines in f:
                # json.dump(TF, f, ensure_ascii=False)
                a = json.load(f)
                # print(a)
                # a[path]
                # dict3 = eval(a)
                a[path] = TF  # 为词典添加词
            with open(path_preserve, 'w') as f1:
                json.dump(a, f1, ensure_ascii=False)
                # f.write(a)  # 将TF写入文档
        else:
            try:
                with open(path_preserve, 'w', errors='ignore') as f:
                    json.dump(dict2, f, ensure_ascii=False)
            except (FileNotFoundError, PermissionError, OSError) as e:
                print('except', e)

            # if word != 'com3' and word != 'com2' and word != 'com1'and word != 'com1':
            #     with open(path_preserve, 'w', errors='ignore') as f:
            #         json.dump(dict2, f, ensure_ascii=False)
            #     # f.write(dict2)  # 将TF写入文档


def getVSM(dict_all3, dir):
    print("dict_all3", dict_all3)
    print("dir", dir)
    # for word in dict_all3.keys():
    # for i in range(0, int(0.8 * len(dir))):
    for file1 in dir:  # 读取20个文件夹
        path20 = path1 + '/' + file1
        dirs2 = os.listdir(path20)
        for i in range(0, int(0.8*len(dirs2))):
    # for i in range(0, int(0.8*len(dir))):  # 1.txt
        # path20_3 = path20 + '/' + dirs2[i
            vector = []
            for word in dict_all3.keys():
                path_preserve = path2 + '/' + word + '.json'
                with open(path_preserve, 'r') as f:
                    a = json.load(f)
                    print(dirs2[i])
                    if dirs2[i] in a.keys():
                        TF = a[dirs2[i]]
                    else:
                        TF = 0
                    IDF = a['IDF']
                TF_IDF = TF*IDF
                vector.append(TF_IDF)
            path_vector = path3 + '/' + dirs2[i] + '.json'
            with open(path_vector, 'w') as f:
                json.dump(vector, f, ensure_ascii=False)


def getFiles(path1, path):  # 读取文件
    number = 0
    number_word = 0
    number_paixun = 0
    dirs1 = os.listdir(path)
    FileNum = getFileNum(dirs1)  # 文档总数
    # for file1 in dirs1:  # 读取20个文件夹
    #     path20 = path1 + '/' + file1
    #     dirs2 = os.listdir(path20)
    #     for i in range(0, int(0.8*len(dirs2))):
    #         path20_3 = path20 + '/' + dirs2[i]  # 得到80%文件为训练
            # print(path20_3)
    getWords(path1)
    for word, freq in dict_all.items():
        if freq > 5:  # 只保留出现次数大于5的单词
            # vocab2[word] = freq
            dict_all3[word] = freq  # 过滤掉词典中不符合条件的词
            number_word += 1
    print('number_word', number_word)
    for file2 in dirs1:  # 读取20个文件夹
        path200 = path1 + '/' + file2
        dirs22 = os.listdir(path200)
        for i in range(0, int(0.8 * len(dirs22))):
            vocab2 = defaultdict(int)
            path20_3_2_2 = path200 + '/' + dirs22[i]  # 得到80%文件为训练
            print(path20_3_2_2)
            vocab1, IDF2 = getWords2(path20_3_2_2)
            for word in vocab1.keys():
                if word in dict_all3.keys():
                    number += vocab1[word]  # 文档中的总词组数IDF----
                    number_paixun += 1
                    vocab2[word] = vocab1[word]
            getTF(vocab2, number, dirs22[i])
    print('---number----', number_paixun)
    print('---开始计算IDF----')
    getIDF(IDF2, FileNum)
    print('--TF_IDF计算完成----')

    # print('dict_all3', dict_all3)
    getVSM(dict_all3, dirs1)


# if __name__ == '__main__':
#     getFiles(path1)