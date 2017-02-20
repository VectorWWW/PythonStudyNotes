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
#     b = 15    # bΪline�Ļ�������
#     def line(x):
#         return 2*x+b    # line�����յ�bֵ�Ǻ���������ʱ�ɹ��ο���bֵ��������ʹ��ʱ��bֵ��
#     return line       # return a function object
# # һ�����������Ļ�����������һ�𣬾͹�����һ���հ�(closure)
# b = 5
# my_line = line_conf()
# print(my_line(5))
# ================================================================
# ��������ȡֵ�������ں��������__closure__�����С���������Ĵ��룺
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