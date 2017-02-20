# coding:GB2312
# 装饰器可以对一个函数、方法或者类进行加工。
# # get square sum
# def square_sum(a, b):
#     print("input:", a, b)
#     return a**2 + b**2
# # get aquare diff
# def square_diff( a, b):
#     print('input:', a, b)
#     return a**2 - b**2

# print(square_sum(3,4))
# print(square_diff(3,4))
# 现在，我们使用装饰器来实现上述修改：
# def decorator(F):
#     def new_F(a, b):
#         print("input", a, b)
#         return F(a, b)
#     return new_F

# # get square sum
# @decorator
# def square_sum(a, b):
#     return a**2 + b**2

# # get square diff
# @decorator
# def square_diff(a, b):
#     return a**2 - b**2

# print(square_sum(3, 4))
# print(square_diff(3, 4))

# 含参的装饰器=================================================
# a new wrapper layer
# def pre_str(pre=''):
#     # old decorator
#     def decorator(F):
#         def new_F(a, b):
#             print(pre + "input", a, b)
#             return F(a, b)
#         return new_F
#     return decorator

# # get square sum
# @pre_str('^_^')
# def square_sum(a, b):
#     return a**2 + b**2

# # get square diff
# @pre_str('T_T')
# def square_diff(a, b):
#     return a**2 - b**2

# print(square_sum(3, 4))
# print(square_diff(3, 4))
# 上面的pre_str是允许参数的装饰器。它实际上是对原有装饰器的一个函数封装，并返回一个装饰器。我们可以将它理解为一个含有环境参量的闭包。当我们使用@pre_str('^_^')调用的时候，Python能够发现这一层的封装，并把参数传递到装饰器的环境中。
# 装饰类===============================================================
def decorator(aClass):
    class newClass:
        def __init__(self, age):
            self.total_display   = 0
            self.wrapped         = aClass(age)
        def display(self):
            self.total_display += 1
            print("total display", self.total_display)
            self.wrapped.display()
    return newClass

@decorator
class Bird:
    def __init__(self, age):
        self.age = age
    def display(self):
        print("My age is",self.age)

eagleLord = Bird(5)
for i in range(3):
    eagleLord.display()