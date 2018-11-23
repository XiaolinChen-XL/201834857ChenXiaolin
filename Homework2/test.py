import os
import nltk
from collections import defaultdict
import json
from nltk.stem.lancaster import LancasterStemmer
from nltk.corpus import stopwords as pw
import re
lancaster_stemmer = LancasterStemmer()
LanStem = nltk.LancasterStemmer
cacheStopWords = pw.words("english")

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

path1 = "../DataSet/20news-18828"
path2 = "Bayes"
acc = 0
class_list = os.listdir(path1)
json_list1 = os.listdir(path2)
json_list = []
print(json_list1)
for json_every in json_list1:
    json_every = json_every[0:-5]
    json_list.append(json_every)
print(json_list)

test_data = defaultdict(int)
P = defaultdict(float)
count = 1
for class_every in class_list:
    glist = []
    class_path = path1 + '/' +class_every
    # print(class_path)
    file_list = os.listdir(class_path)
    # for i in random.randint(int(0.8*len(file_list)), -1):
    for i in range(int(0.8*len(file_list)), int(0.8*len(file_list))+10):
        # print(file_list[i])
        # glist.append(file_list[i])
        test_data[str(file_list[i])] = class_every
    # print(test_data)
    # random.shuffle(glist)
with open('SaveAddr.txt', 'w') as f:
    # for i in range(10):
    #     f.write(glist[i]+'\n')
    json_str = json.dumps(test_data)
    f.write(json_str)
# print(len(test_data.values()))
for i in test_data.keys():
    # print(test_data[i])
    # break
    word_freq = defaultdict(int)
    path3 = path1 + '/' + str(test_data[i]) + '/' + str(i)
    # print(path3)
    with open(path3, 'r') as f2:
        word_freq = get_word_freq(path3, word_freq)
        del word_freq['']
    for num_class in json_list:
        P[num_class] = 0.0
        path4 = path2 + '/' + str(num_class) +'.json'
        # print(path4)
        with open(path4, 'r') as f3:
            class_word_dict = json.load(f3)
            P_class = class_word_dict['P_class']
        for word in word_freq.keys():
            if word in class_word_dict:
            # print(class_word_dict[word])
                P[num_class] += class_word_dict[word]
        P[num_class] = P[num_class] * P_class
        # print(P)
        # print(num_class)
    list_final = sorted(P.items(), key=lambda item: item[1], reverse=True)
    print(list_final)
    for key, item in list_final:
        count += 1
        # print(key, item)
        p_final = key
        with open('result.txt', 'a') as f4:
            f4.write(i + ' predict: ' + key + ' Groundtruth: ' + test_data[i] + '\n')
        if count >= 2:
            break
    if p_final == test_data[i]:
        acc += 1
    else:
        acc += 0
acc = float(acc)/float(len(test_data.items()))
print(acc)
            # print(P_class)
    #     break
    # break
        # for word in word_freq
    # print(word_freq)
    # break