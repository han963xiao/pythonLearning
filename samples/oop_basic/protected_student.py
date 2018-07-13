#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#定义一个类中的方法时，一定要加一个self！！！一定要加一个self！！！一定要加一个self！！！这样才能访问这个对象的一切属性还有方法
#你会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的,有的类的方法没有阻止你
# 但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问
class Student(object):

    def __init__(self, name, score):
        #如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__
        # 在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
        self.__name = name
        self.__score = score
#跟java一样java的getter还有setter方法
    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

bart = Student('Bart Simpson', 59)
#初始化赋值完了之后就不能访问了！这里是利用seter方法来访问的
print('bart.get_name() =', bart.get_name())
bart.set_score(60)
print('bart.get_score() =', bart.get_score())

print('DO NOT use bart._Student__name:', bart._Student__name)
