# coding:GB2312
import re
m = re.search('[0-9]','abcd4ef23g')  # ���������ַ�����ֱ�����ַ��ϵ����ַ�����
print(m.group(0))
n = re.match('[0-9]','23')    # ��ͷ��ʼ����ַ����Ƿ����������ʽ��������ַ����ĵ�һ���ַ���ʼ�������
print(n.group(0))

m2 = re.search("output_(\d{4})", "output_1986.txt")
print(m2.group(1))

m3 = re.search("output_(?P<year>\d{4})", "output_1986.txt")   #(?P<name>...) Ϊgroup����
print(m3.group("year"))