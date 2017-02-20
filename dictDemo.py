# coding:GB2312
dic = {'lilei':90, 'lily':100, 'sam':57, 'tom':90}
# for key in dic:
#     print dic[key]
print dic.keys()
print dic.values()
print dic.items()    # 返回dic所有的元素（键值对）
print len(dic)
del dic['tom']
print dic.keys()

dic.clear()
print dic.keys()