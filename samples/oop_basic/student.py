#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#面向对象基础，就是OOP
#类和实例
#面向对象最重要的概念就是类（Class）和实例（Instance），必须牢记类是抽象的模板，比如Student类，而实例是根据类创建出来的一个个具体的“对象”，
# 每个对象都拥有相同的方法，但各自的数据可能不同
#class后面紧接着是类名，即Student，类名通常是大写开头的单词，紧接着是(object)，表示该类是从哪个类继承下来的，
# 通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类
#后面的小括号是表明类是从哪个类继承的

class Student(object):

#self是指的创造的实例的本身，类中的方法在定义的时候一定要加self
#特殊方法“__init__”前后分别有两个下划线！！！
#有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数
#通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去
#注意到__init__方法的第一个参数永远是self，表示创建的实例本身，
# 因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身
#需要用到对象中的属性的时候必须用self  ！！！
#方法中需要self参数，你这个方法就可以用这个对象的其他方法还有属性了，只要你用self当做参数

#定义一个方法，除了第一个参数是self外，其他和普通函数一样。定义方法的时候最好要传入self
# 要调用一个方法，只需要在实例变量上直接调用，除了self不用传递，其他参数正常传入
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

#这样从类中创造对象的！
bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)

print('bart.name =', bart.name)
print('bart.score =', bart.score)
bart.print_score()

print('grade of Bart:', bart.get_grade())
print('grade of Lisa:', lisa.get_grade())
