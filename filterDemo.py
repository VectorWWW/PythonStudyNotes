# coding:GB2312
# filter�����ĵ�һ������Ҳ��һ������������Ҳ�ǽ���Ϊ�����ĺ������������ڶ��Ԫ�ء�����������󷵻ص���True����ôε�Ԫ�ر������ڷ��صı��С� filterͨ������ĺ�����ɸѡ���ݡ�ͬ������Python 3.X�У�filter���صĲ��Ǳ�����ѭ������

def func(a):
    if a > 100:
        return True
    else:
        return False
print filter(func,[10,56,101,500])
