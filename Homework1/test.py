# import nltk
# from nltk.stem.lancaster import LancasterStemmer
# lancaster_stemmer = LancasterStemmer()
# LanStem = nltk.LancasterStemmer
# from nltk.corpus import stopwords as pw
# # def getNgrams(input, n): N-gram
# #     input = input.split(' ')
# #     output = []
# #     for i in range(len(input)-n+1):
# #         output.append(input[i:i+n])
# #     return output
#
#
# # s = lancaster_stemmer.stem('maximum')
# # print(s)
# # line = 'Are we good friends? Yes, we are good friends.'
# # sents = nltk.sent_tokenize(line)
# # for sent in sents:
# #     words_token = nltk.word_tokenize(sent)  # 分词
# #     print(words_token)
# # for word in words_token:
# #     print(word)
# #     words_stem = lancaster_stemmer.stem(word)
# #     print(words_stem)
# # # words_stem =lancaster_stemmer.stem('maximum')
# # # print(words_stem)
# # # print(words_stem)
#
# def stopWords(filePath):
#     with open(filePath) as text:
#         text = text.readlines()
#     for j in range(len(text)):
#         text1 = text[j]
#         # text1 = ''.join([word + " " for word in text1.split() if word not in cacheStopWords])
#         # with open(stop_word_all[i], 'r+', encoding='utf-8') as f:
#         #     f.read()
#         #     f.write('\n'+text1)
#
#
# path3 = 'test.text'
# with open(path3, 'r', encoding='UTF-8', errors='ignore') as f:
#     print('************-----' + path3 + '-----************')
#     for line in f:
#         # ff = str(line).split(' ')
#         print(line)
#         sents = nltk.sent_tokenize(line)  # 分句
#         for sent in sents:
#             words_token = nltk.word_tokenize(sent)  # 分词
#             print(words_token)
#         for word in words_token:
#             words_stem = lancaster_stemmer.stem(str(words_token))  # stem操作
#             print(words_stem)
#
#
#         # ff = str(line).split(' ')
#
#     #
#     # def getSentences():
#     #
#     #         # print('************-----'+path3+'-----************')
#     #         # print(path3.length)
#     #         for line in f:
#     #             # ff = str(line).split(' ')
#     #         for sent in sents:
#     #             words_token = nltk.word_tokenize(sent)  # 分词
#     #         # for word in words_token:
#     #         #     words_stem = lancaster_stemmer.stem(words_token)  # stem操作
#             # stopWords(path3)
#
#
import re
s ="string. With. Punctuation?"
print(s)
s = re.sub(r'[^\w\s]','',s)
print(s)
