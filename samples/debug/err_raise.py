# err_raise.py

#自己建立一个异常错误类
class FooError(ValueError):
    #他是从valueerror里面继承的！
    pass

def foo(s):
    n = int(s)
    if n==0:
        #用raise语句抛出一个错误的实例,错误语句使用raise来抛出
        raise FooError('invalid value: %s' % s)
    return 10 / n

foo('0')
#只有在必要的时候才定义我们自己的错误类型。
# 如果可以选择Python已有的内置的错误类型（比如ValueError，TypeError），尽量使用Python内置的错误类
