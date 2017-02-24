# coding:GB2312
# 用装饰器实现第一题
def jd(x):
    return abs(x)

def kf(F):
    def new_F(x):
        return F(x)**0.5
    return new_F

def xf(F):
    def new_F(x):
        return -F(x)
    return new_F

func = xf(kf(jd))

print func(-4)