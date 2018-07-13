#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#这个要好好学一下！json！
#ython语言特定的序列化模块是pickle
# 但如果要把序列化搞得更通用、更符合Web标准，就可以使用json模块

#利用json模块
import json

d = dict(name='Bob', age=20, score=88)

#怎么把string变成json格式
data = json.dumps(d)
print('JSON Data is a str:', data)

#把json格式再变成str
reborn = json.loads(data)
print(reborn)

#我们的目的就是直接把一个类对象变成json！里面的属性利用json存储就很棒！

class Student(object):

    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __str__(self):
        return 'Student object (%s, %s, %s)' % (self.name, self.age, self.score)

s = Student('Bob', 20, 88)

#这样匿名函数的作用就出来了!!
#Student实例首先被student2dict()函数转换成dict，然后再被顺利序列化为JSON
#因为通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。可以把类的属性和值变成dic传出来！！！
# 也有少数例外 比如定义了__slots__的class

std_data = json.dumps(s, default=lambda obj: obj.__dict__)
print('Dump Student:', std_data)

#从json对象里拿到dic  object_hook函数负责把dict转换为Student实例 这里的d是一个dic 明显就可以按照属性取值的方式取出来！！
rebuild = json.loads(std_data, object_hook=lambda d: Student(d['name'], d['age'], d['score']))
print(rebuild)

#可以为student对象专门写一个转化函数,把对象转化成dic，然后在用json.dump转化成json
def student2dict(std):
    return {
        'name':std.name,
        'age':std.age,
        'score':std.score
     }
