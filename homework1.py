# coding:GB2312
# ͨ���հ���һ������ x ������ˮ�߲���������������հ���ÿһ�����ν���һ������������������ֵ���ٿ����������෴������
def xf(x):
    def kf(x):
        def jd(x):
            return abs(x)
        return jd(x)**0.5
    return -kf(x)

print xf(-4)
