#-*-coding:utf-8-*-
from sklearn.cluster import KMeans, AffinityPropagation, MeanShift, SpectralClustering, AgglomerativeClustering, estimate_bandwidth
from sklearn.mixture import GaussianMixture
from sklearn import metrics
import json
import data_pre
path = './Tweets.txt'
text = []
label = []
k = 10


def kmeans( text, label):
    y_pred = KMeans(float(k), random_state=9).fit_predict(text)
    # score = metrics.calinski_harabaz_score(train_label, y_pred)
    score_kmeans = metrics.calinski_harabaz_score(label, y_pred)
    return score_kmeans


def AffinityPropagation(X, Y):
    print('AffinityPropagation')
    y_pred = AffinityPropagation().fit_predict(X)
    score_AffinityPropagation = metrics.calinski_harabaz_score(label, y_pred)
    return score_AffinityPropagation

def MeanShift(X, Y):
    print('MeanShift')
    bandwidth = estimate_bandwidth(X, quantile=0.2, n_samples=500)
    y_pred = MeanShift(bandwidth=bandwidth, bin_seeding=True).fit_predict(X)
    score_MeanShift = metrics.calinski_harabaz_score(label, y_pred)


def SpectralClustering(X, Y, gamma):
    print('spectral_clustering')
    K = len(set(Y))
    y_pred = SpectralClustering(n_clusters=K, gamma=gamma).fit_predict(X)
    score_SpectralClustering = metrics.calinski_harabaz_score(label, y_pred)
    return score_SpectralClustering



def AgglomerativeClustering(X, Y, linkage):
    print('AgglomerativeClustering: ' + linkage)
    K = len(set(Y))
    y_pred = AgglomerativeClustering(n_clusters=K, linkage=linkage).fit_predict(X)
    score_AgglomerativeClustering = metrics.calinski_harabaz_score(label, y_pred)
    return score_AgglomerativeClustering


def DBSCAN(X, Y, eps, min_samples):
    print('DBSCAN')
    y_pred = DBSCAN(eps=eps, min_samples=min_samples).fit_predict(X)
    score_DBSCAN = metrics.calinski_harabaz_score(label, y_pred)
    return score_DBSCAN


def GaussianMixture(X, Y, cov_type):
    print('GaussianMixture: ' + cov_type)
    K = len(set(Y))
    gmm = GaussianMixture(n_components=K, covariance_type=cov_type).fit(X)
    y_pred = gmm.predict(X)
    score_GaussianMixture = metrics.calinski_harabaz_score(label, y_pred)
    return score_GaussianMixture

if __name__ == '__main__':
    with open(path, 'r',  encoding='utf-8') as json_file:
        for line in json_file.readlines():  # 提取数据
            line_json = json.loads(str(line))
            # print(line_json)
            text.append(line_json['text'])
            label.append(line_json['cluster'])
        # 数据以9比1分开
        train_data = text[0:int(0.9*len(text)+1)]
        train_label = label[0:int(0.9*len(text)+1)]
        test_data = text[int(0.9*len(text)+1):-1]
        test_label = label[int(0.9*len(text)):-1]
        dictionary = data_pre.getWords(text, 'data/cluster-out/dictionary.csv', 0)
        X = data_pre.getVSM(text, dictionary)
        # y_pred = KMeans(k, random_state=9).fit_predict(train_data)
        score1 = kmeans(X, label)
        score2 = AffinityPropagation(X, label)
        score3 = MeanShift(X, label)
        score4 = SpectralClustering(X, label)
        score5 = AgglomerativeClustering(X, label)
        score6 = DBSCAN(X, label)
        score7 = GaussianMixture(X,label)
        # print(score_kmeans)
    #     print(len(train_data))
    #     print(len(test_data))
    #     print(len(train_label))
    #     print(len(test_label))
    #     print(len(text))
    #     print(len(label))
    # # print(text)