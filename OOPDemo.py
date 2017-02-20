# coding:GB2312
# class Bird(object):
#     have_feather = True
#     way_of_reproduction = 'egg'
#     def move(self, dx, dy):
#         position = [0,0]
#         position[0] = position[0] + dx
#         position[1] = position[1] + dy
#         return position

# class Chicken(Bird):
#     way_of_move = 'walk'
#     possible_in_KFC = True

# class Oriole(Bird):
#     way_of_move = 'fly'
#     possible_in_KFC = False

# class happyBird(Bird):
#     def __init__(self, more_words):  # 特殊方法：名字前后各加两个下划线
#         print 'We are happy birds.', more_words

# summer = happyBird('Happy,Happy!')
# summer = Chicken()
# print summer.have_feather
# print 'after move:', summer.move(5,8)
# print summer.way_of_move

# =========================================================================
# class Human(object):
#     laugh = 'hahahaha'
#     def show_laugh(self,a):
#         print self.laugh,a
#     def laugh_100th(self):
#         for i in range(100):
#             self.show_laugh(i)

# lilei = Human()
# lilei.laugh_100th()
#==========================================================================
# 特殊方法：名字前后两个下划线
class Human(object):
    def __init__(self,input_gender):
        self.gender = input_gender
    def printGender(self):
        print self.gender

li_lei = Human('male')
print li_lei.gender  # 结果与下一行对比
li_lei.printGender()
print dir(list)
print help(list)