# coding:GB2312
# �鿴ĳ����������ü���
# ��Ҫע����ǣ���ʹ��ĳ��������Ϊ���������ݸ�getrefcount()ʱ������ʵ���ϴ�����һ����ʱ�����á���ˣ�getrefcount()���õ��Ľ������������Ķ�1��
from sys import getrefcount

a = [1, 2, 3]
print(getrefcount(a))

b = [a, a]
print(getrefcount(a))
