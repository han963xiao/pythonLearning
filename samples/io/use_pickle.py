#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#我们把变量从内存中变成可存储或传输的过程称之为序列化
# 在Python中叫pickling，在其他语言中也被称之为serialization，marshalling，flattening等等
#序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上
#反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling

#python中用pickle模块来实现序列化
import pickle

d = dict(name='Bob', age=20, score=88)

#pickle.dumps()方法可以把任意对象化成一个bytes，然后可以把这个bytes写入文件中

#可以再序列化的时候就把东西传到文件中的！

# f=open('dump.txt','wb')
# pickle.dump(d,f)
# f.close()


data = pickle.dumps(d)
print(data)

#怎么从文件中把二进制队形读出来
reborn = pickle.loads(data)
print(reborn)

#Pickle的问题和所有其他编程语言特有的序列化问题一样，就是它只能用于Python，并且可能不同版本的Python彼此都不兼容
# 因此，只能用Pickle保存那些不重要的数据，不能成功地反序列化也没关系
