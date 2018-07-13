#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#使用枚举类
#建立枚举类有两种方法，一种继承一种是直接枚举类的数组
from enum import Enum, unique

@unique
#@unique装饰器可以帮助我们检查保证没有重复值
#这些带@的都是装饰器，表明下面有一些特性
#建立枚举类的方法
#Weekday(Enum)说明他继承了枚举类，枚举类的方法，他都有！
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

day1 = Weekday.Mon

#下面的都是访问枚举类的方法！其实就是访问值的方法！！！
#他们其实都是一个一个对象
print('day1 =', day1)
#这样只是访问这个对象的名字
print('Weekday.Tue =', Weekday.Tue)
print('Weekday[\'Tue\'] =', Weekday['Tue'])
print('Weekday.Tue.value =', Weekday.Tue.value)
#访问值的方法
print('day1 == Weekday.Mon ?', day1 == Weekday.Mon)
print('day1 == Weekday.Tue ?', day1 == Weekday.Tue)
print('day1 == Weekday(1) ?', day1 == Weekday(1))

#这个也是枚举类的特殊方法，__members__.items
for name, member in Weekday.__members__.items():
    print(name, '=>', member)

#这是另一种建立枚举累的方法！类似filter还有sorted还有map() reduce()
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)
