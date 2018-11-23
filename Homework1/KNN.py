import os
import numpy as np
import data_pre
from collections import Counter
from heapq import nlargest
from collections import defaultdict


def cos_compute(test_data,train_data):   # 余弦相似度
    upper = np.sum(test_data * train_data)
    under = np.sqrt(np.sum(np.square(test_data))) * np.sqrt(np.sum(np.square(train_data)))
    distance = upper/under
    return distance


def knn(k, path_train, path_test, train_label, test_label):
    train_data = []
    test_data = []
    with open(path_train, 'r', encoding='utf-8', errors='ignore') as f_train:  # 得到训练数据的向量表示
        for line in f_train:
            train_data.extend(line)
    with open(path_test, 'r', encoding='utf-8', errors='ignore') as f_test:  # 得到训练数据的向量表示
        for line in f_test:
            test_data.extend(line)
    index = 0
    accuracy = 0
    for test_file in test_data:
        distance = []
        print('%d file in testing data' % index)
        for train_file in train_data:
            distance.append(cos_compute(test_file, train_file))
        # 选取k个近邻
        kneighbor = map(distance.index, nlargest(k, distance))
        neighbor = list(kneighbor)
        print(neighbor)
        label_list = train_label[neighbor]
        result_predict = Counter(label_list).most_common(1)
        result_label = test_label[index]
        if result_predict == result_label:
            accuracy += 1
            print("The prediction is right")
        else:
            print("The prediction is false")
        index += 1
    accuracy = float(accuracy) / len(test_data)
    print(accuracy)


def main():
    path = "DataSet/20news-18828"
    dir = os.listdir(path)
    path_train_vector = "./DataSet/vector_train"
    path_test_vector = "./DataSet/vector_test"
    train_label = defaultdict(int)
    test_label = defaultdict(int)
    for file in dir:  # 读取20个文件夹
        path_2 = path + '/' + file
        dir1 = os.listdir(path_2)
        # dir2 = os.listdir(path2)
        for i in range(0, int(0.8*len(dir1))):  # 得到训练数据
            path_train = path_2 + '/' + dir1[i]
            train_label[dir[i]] = file
            with open(path_train, 'r', encoding='utf-8', errors='ignore'):  # 得到训练数据的向量表示
                data_pre.getFiles(path_train, path)
        for i in range(int(0.8*len(dir1))+1, len(dir1)):  # 得到测试数据
            path_test_every = path_2 + '/' + dir1[i]
            test_label[dir[i]] = file
            with open(path_test_every, 'r', encoding='utf-8', errors='ignore'):  # 得到测试数据的向量表示
                data_pre.getFiles(path_test_every, path)
        knn(5, path_train_vector, path_test_vector, train_label, test_label)


if __name__ == '__main__':
    main()



