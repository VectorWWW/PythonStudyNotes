# coding:GB2312
# Python��һ����������(container)��������ʵ�ȣ����԰����������ʵ���ϣ����������а����Ĳ�����Ԫ�ض�������ָ�����Ԫ�ض�������á�
class from_obj(object):
    def __init__(self, to_obj):
        self.to_obj = to_obj

b = [1,2,3]
a = from_obj(b)
print(id(a.to_obj))
print(id(b))
