# coding:GB2312
def f(a, b, c):
    return a+b+c

print(f(1,2,3))

# �ؼ��ʴ���
print(f(c=3,b=2,a=1))
print(f(1,c=3,b=2))

# ����Ĭ��ֵ
def g(a,b,c=10):
    return a+b+c

print(g(3,2))
print(g(3,2,1))

# ����λ�ô���
def func(*name):
    print type(name)
    print name

func(1,4,6)
func(5,6,7,1,2,3)

# �����ؼ��ִ���
def func2(**dict):
    print type(dict)
    print dict

func2(a=1,b=9)
func2(m=2,n=1,c=11)

# �����
args = (1,3,4)
func(*args)
func(args)
dict = {'a': 1, 'b': 2, 'c':3}
func2(**dict)