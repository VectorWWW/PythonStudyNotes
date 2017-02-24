# coding:GB2312
import os.path
path = 'E:\文档\GitHub\PythonStudyNotes\ospathDemo.py'

print(os.path.basename(path))    # 查询路径中包含的文件名
print(os.path.dirname(path))     # 查询路径中包含的目录

info = os.path.split(path)       # 将路径分割成文件名和目录两个部分，放在一个表中返回
path2 = os.path.join(" \ ", 'E:', '文档', 'GitHub', 'PythonStudyNotes')  # 使用目录名和文件名构成一个路径字符串

p_list = [path, path2]
print(os.path.commonprefix(p_list))    # 查询多个路径的共同部分