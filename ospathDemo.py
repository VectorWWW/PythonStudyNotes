# coding:GB2312
import os.path
path = 'E:\�ĵ�\GitHub\PythonStudyNotes\ospathDemo.py'

print(os.path.basename(path))    # ��ѯ·���а������ļ���
print(os.path.dirname(path))     # ��ѯ·���а�����Ŀ¼

info = os.path.split(path)       # ��·���ָ���ļ�����Ŀ¼�������֣�����һ�����з���
path2 = os.path.join(" \ ", 'E:', '�ĵ�', 'GitHub', 'PythonStudyNotes')  # ʹ��Ŀ¼�����ļ�������һ��·���ַ���

p_list = [path, path2]
print(os.path.commonprefix(p_list))    # ��ѯ���·���Ĺ�ͬ����