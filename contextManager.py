# coding:GB2312
# �ر��ļ�
# without context manager
# f = open("new.txt", "w")
# print(f.closed)         # whether the file is open
# f.write("hello world!")
# f.close()
# print(f.closed)

# with context manager
with open("new.txt", "w") as f:
    print(f.closed)
    f.write("Hello World!")
print(f.closed)
# ���γ���ʵ����ִ�е�����ͬ�Ĳ��������ǵĵڶ��γ����ʹ���������Ĺ����� (with...as...)�������Ĺ����������������ĳ���顣�������ĳ����ִ�н�����ʱ��(Ҳ���ǲ�������)�������Ĺ������Զ��ر����ļ� (����ͨ��f.closed����ѯ�ļ��Ƿ�ر�)�������൱��ʹ�������涨���ļ�����f��ʹ�÷�Χ��