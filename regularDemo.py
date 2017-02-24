# coding:GB2312
import re
m = re.search('[0-9]','abcd4ef23g')  # 搜索整个字符串，直到发现符合的子字符串。
print(m.group(0))
n = re.match('[0-9]','23')    # 从头开始检查字符串是否符合正则表达式。必须从字符串的第一个字符开始就相符。
print(n.group(0))

m2 = re.search("output_(\d{4})", "output_1986.txt")
print(m2.group(1))

m3 = re.search("output_(?P<year>\d{4})", "output_1986.txt")   #(?P<name>...) 为group命名
print(m3.group("year"))