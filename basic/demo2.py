# -*- coding: utf-8 -*-


# 定义
class HomeWork():    
    def __init__(self, sex):
        self.name = ''  # 你不能直接self.name就完事，得有一个初始值
        self.age = 0 #硬赋
        self.sex = sex
      


# 调用
hw=HomeWork('女')
hw.name = 'cc'
hw.age = 19
print(hw.sex,hw.name)


# 我打开一个文件或我找到某个类，我想玩他，首先进行类的实例化
caichang=HomeWork(0)
# 立刻看这个类有没有__init__（初始化）方法，如果有，立刻看有没有参数，如果有，立刻传参
caichang=HomeWork(0)
# 这个__init__中的所有定义都是这个类的属性
# 你可以随便的对象.属性或对象.方法来操作这个类

