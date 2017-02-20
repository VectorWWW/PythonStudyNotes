# coding:GB2312
# filter函数的第一个参数也是一个函数对象。它也是将作为参数的函数对象作用于多个元素。如果函数对象返回的是True，则该次的元素被储存于返回的表中。 filter通过读入的函数来筛选数据。同样，在Python 3.X中，filter返回的不是表，而是循环对象。

def func(a):
    if a > 100:
        return True
    else:
        return False
print filter(func,[10,56,101,500])
