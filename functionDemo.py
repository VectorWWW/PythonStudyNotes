# coding:GB2312
# def square_sum(a,b):
#     c = a**2 + b**2
#     return c
# return可以返回多个值，以逗号分隔。相当于返回一个tuple(定值表)。
a = 1

def change_integer(a):
    a = a + 1
    return a
# 值传递
print change_integer(a)    #注意观察结果
print a   #注意观察结果

b = [1,2,3]
# 指针传递
def change_list(b):
    b[0] = b[0] + 1
    return b

print change_list(b)
print b
