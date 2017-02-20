# coding:GB2312
# 关闭文件
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
# 两段程序实际上执行的是相同的操作。我们的第二段程序就使用了上下文管理器 (with...as...)。上下文管理器有隶属于它的程序块。当隶属的程序块执行结束的时候(也就是不再缩进)，上下文管理器自动关闭了文件 (我们通过f.closed来查询文件是否关闭)。我们相当于使用缩进规定了文件对象f的使用范围。