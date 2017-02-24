# coding:GB2312
# 通过闭包对一个数据 x 做“流水线操作”，至少三层闭包，每一层依次进行一项操作，（如先求绝对值，再开方，再求相反数）。
def xf(x):
    def kf(x):
        def jd(x):
            return abs(x)
        return jd(x)**0.5
    return -kf(x)

print xf(-4)
