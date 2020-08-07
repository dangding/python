#### 本章要点

- 介绍python的基本语法

### 标识符

所谓标识符，就是python代码中，用来标识变量和函数的名称。

python中标识符的命名规则：

- 标识符只能由字母、数字、下划线组成，但不能以数字开头；
- 标识符区分大小写；
- 以单下划线和双下划线开头的标识符具有特殊含义，因此，建议初学者避开；
- 一行可以有多条语句，用`;`作为分隔符，如下所示：
```
>>> print("hello");print("world")
hello
world
```

### 关键词

即下列单词，为python语言保留标识符，用于代码中。

```
and  exec  not  assert  finally  or  break  for  pass  class  from  print  continue
global  raise  def  if  return  del  import  try  elif  in  while  else  is  with
except  lambda  yield
```

### 语法格式

python语言的代码块是通过`缩进`来进行控制的。也就是说，控制块内，同一级代码中，每一行前面的`空格`或`tab`是相同的。

**Note:** 这一点需要严格执行，尤其是要注意`空格`和`tab`是有区别的。建议统一风格，使用空格作为缩进。

比如以下代码是合法的：

```
if True:
    print("True")
else:
    print("False")
```

以下代码则是非法的：

```
if True:
    print("True")
else:
    print("False")
    # 这是一个没有缩进对齐的错误示例
  print("error")
```

执行的时候，将会收到报错信息。
