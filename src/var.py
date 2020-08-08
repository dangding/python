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

fun()
