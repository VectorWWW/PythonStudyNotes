# coding:GB2312
class superList(list):
    def __sub__(self, b):
        a = self[:] # ���self��supeList�Ķ�������superList�̳���list�����������ú�list[:]��ͬ�����÷�������ʾ��������
        b = b[:]
        while len(b) > 0:
            element_b = b.pop()
            if element_b in a:
                a.remove(element_b)
        return a

print superList([1,2,3]) - superList([3,4])