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

# 定义列表
a = [1,2,3,4,5,6]

# 将a作为函数的参数
print(list_sum(a))
