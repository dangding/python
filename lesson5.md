#### 本章要点

- 函数的定义、调用和参数传递

### 函数定义

函数是可重复使用的功能模块。通过函数，可以使得代码可以模块化，同时提交代码的利用率。比如，上一章中，所实现的求元素之和的实例，如果能定义成一个函数，那么可以供多个模块使用。

函数的定义如下：

```
# 定义函数，求列表中的元素之和
# def：函数定义的关键词
# list_sum：函数名称
# return：函数返回关键词
def list_sum(a):
    # 初始化sum的值
    sum = 0
    for i in a:
        sum = sum + i

    # 将计算结果作为函数返回值
    return sum
```

一定要注意，`缩进`和`冒号`。

### 函数调用

函数调用是指，在代码中，使用某个函数的功能，如，需要在代码中，求一个列表元素之和，则可以调用上述函数，代码如下：

```
# 定义列表
a = [1,2,3,4,5,6]

# 将a作为函数的参数，并把结果赋值在s
s = list_sum(a)
print(s)
```

`print`本身也是一个函数，`s`是其参数。

### 参数

参数是指，供函数处理的变量。传入参数后，在函数内部便可以使用该变量。

在这里，需要提一下变量的作用域，即定义的变量，在什么范围内有效。变量的作用域，是一个控制单元内，若不是在控制单元内定义的变量，作用范围则为整个模块。如：

```
# 模块内有效
v1 = 0
print (v1)

def fun():
    # 控制单元内有效
    v2 = 1
    print(v2)

    # 由于v1作用于模块内，因此，也可以访问
    print(v1)

# 不能访问，v2无效
#print(v2)

# 调用函数
fun()
```



*祝玩得开心！*