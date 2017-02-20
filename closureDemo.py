# coding:GB2312
# def line_conf():
#     def line(x):
#         return 2*x + 1
#     print(line(5))

# line_conf()
# print(line(5))
# ===========================
# def line_conf():
#     def line(x):
#         return 2*x + 1
#     return line

# my_line = line_conf()
# print(my_line(5))
# ===============================
# def line_conf():
#     b = 15    # b为line的环境变量
#     def line(x):
#         return 2*x+b    # line所参照的b值是函数对象定义时可供参考的b值，而不是使用时的b值。
#     return line       # return a function object
# # 一个函数和它的环境变量合在一起，就构成了一个闭包(closure)
# b = 5
# my_line = line_conf()
# print(my_line(5))
# ================================================================
# 环境变量取值被保存在函数对象的__closure__属性中。比如下面的代码：
# def line_conf():
#     b = 15
#     def line(x):
#         return 2*x+b
#     return line       # return a function object

# b = 5
# my_line = line_conf()
# print(my_line.__closure__)
# print(my_line.__closure__[0].cell_contents)
# ====================================================================
def line_conf(a, b):
    def line(x):
        return a*x + b
    return line

line1 = line_conf(1, 1)
line2 = line_conf(4, 5)
print(line1(5), line2(5))