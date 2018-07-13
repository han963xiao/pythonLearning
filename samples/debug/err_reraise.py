# err_reraise.py

#在bar()函数中，我们明明已经捕获了错误，但是，打印一个ValueError!后，
# 又把错误通过raise语句抛出去了
def foo(s):
    n = int(s)
    if n==0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise
# raise语句如果不带参数，就会把当前错误原样抛出。
# 此外，在except中raise一个Error，还可以把一种类型的错误转化成另一种类型
bar()

