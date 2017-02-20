# coding:GB2312
# 生成器(generator)的主要目的是构成一个用户自定义的循环对象。
# 生成器的编写方法和函数定义类似，只是在return的地方改为yield。生成器中可以有多个yield。当生成器遇到一个yield时，会暂停运行生成器，返回yield后面的值。当再次调用生成器的时候，会从刚才暂停的地方继续运行，直到下一个yield。生成器自身又构成一个循环器，每次循环使用一个yield返回的值。

def gen():
    a = 100
    yield a
    a = a*8
    yield a
    yield 1000

for i in gen():
    print i