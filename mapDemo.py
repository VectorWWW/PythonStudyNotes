# coding:GB2312
# map()是Python的内置函数。它的第一个参数是一个函数对象。
# map()的功能是将函数对象依次作用于表的每一个元素

re = map((lambda x: x+3),[1,3,5,6])
print re
re = map((lambda x,y: x+y),[1,2,3],[6,7,9]) 
# map()将每次从两个表中分别取出一个元素，带入lambda所定义的函数。
print re