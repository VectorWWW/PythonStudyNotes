# coding:GB2312
# ���ǿ�����__getattr__(self, name)����ѯ��ʱ���ɵ����ԡ������ǲ�ѯһ������ʱ�����ͨ��__dict__�����޷��ҵ������ԣ���ôPython����ö����__getattr__����������ʱ���ɸ����ԡ�
class bird(object):
    feather = True

class chicken(bird):
    fly = False
    def __init__(self, age):
        self.age = age
    def __getattr__(self, name):
        if name == 'adult':
            if self.age > 1.0: return True
            else: return False
        else: raise AttributeError(name)

summer = chicken(2)

print(summer.adult)
summer.age = 0.5
print(summer.adult)

print(summer.male)
# ÿ��������Ҫ���Լ��Ĵ���������__getattr__���Խ����еļ�ʱ�������Է���ͬһ�������д���__getattr__���Ը��ݺ�����������ͬ�����ԡ������������ǲ�ѯ������male��ʱ��raise AttributeError��
# Python�л���һ��__getattribute__���ⷽ�������ڲ�ѯ�������ԡ�__getattr__ֻ��������ѯ����__dict__ϵͳ�е�����)
# __setattr__(self, name, value)��__delattr__(self, name)�������޸ĺ�ɾ�����ԡ����ǵ�Ӧ������㣬�������������ԡ�