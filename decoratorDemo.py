# coding:GB2312
# װ�������Զ�һ��������������������мӹ���
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
# ���ڣ�����ʹ��װ������ʵ�������޸ģ�
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

# ���ε�װ����=================================================
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
# �����pre_str�����������װ��������ʵ�����Ƕ�ԭ��װ������һ��������װ��������һ��װ���������ǿ��Խ������Ϊһ�����л��������ıհ���������ʹ��@pre_str('^_^')���õ�ʱ��Python�ܹ�������һ��ķ�װ�����Ѳ������ݵ�װ�����Ļ����С�
# װ����===============================================================
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