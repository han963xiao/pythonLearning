#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#为了限制score的范围，可以通过一个set_score()方法来设置成绩，再通过一个get_score()来获取成绩，这样，在set_score()方法里，就可以检查参数
#但是这样每次赋值都要调用方法不是很舒服的！

class Student(object):
#利用这个注释表明下面这个是属性！是属性的get方法！
    @property
    def score(self):
        return self._score
#在利用这个注释表示这个是属性的setter方法，名字可以随便起的
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
#也就是直接使用score不赋值就是引出这个属性值
#使用score并且赋值是对于属性赋值

s = Student()
s.score = 60
print('s.score =', s.score)
# ValueError: score must between 0 ~ 100!
s.score = 9999
