# -*- coding: utf-8 -*-
#from selenium import webdriver

# 继承
# 1、什么叫继承
# 2、为什么要继承？相同代码写一次
# 3、属性不需要写覆盖关系，直接继承后就拥有；方法可覆写（override），覆写的前提是要和父类的方法名一致，也可直接继承用

class Animal():

    def __init__(self):
        self.eye = ''
        self.ear = ''

    def chi(self):
        print('动物吃')
    
    def pao(self):
        print('动物跑')
        
    def pa(self):
        print('就地趴下')


class Cat(Animal):

    def __init__(self):
        self.weiba = '耷拉着'
    def zhua(self):
        print('抓老鼠')
    def pa(self):
        print('优雅的趴')
        
    #这个chi覆盖了父类的chi
    def chi(self):
        print('猫咪的吃')


class Bird():
    def fei(self):
        print('我飞飞飞')

class Dog(Cat,Bird):
    #这个chi覆盖了父类的chi
    def chi(self):
        print('我是用啃的')
        
    def pa(self):
        print('大字趴下')


tom = Cat()
tom.pao()
tom.chi()
tom.weiba='翘'
tom.zhua()
tom.pa()
tom.weiba()


erha = Dog()
erha.ear = '尖尖的'
erha.eye = '蓝色'
erha.chi()
erha.zhua()
erha.fei()
erha.pa()

erha.pao()


#driver=webdriver.Chrome()
#driver.ex

