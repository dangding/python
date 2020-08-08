# 设置分数
score = 70

# 注意控制块语句后面，需要加冒号
if score < 60:
    print("不及格")
# 表示:60<=score<70
elif score >= 60 and score < 70:
    print("及格")
elif score >=70 and score < 85:
    print("良好")
# 其他情况均为优秀
# 因为所有小于85的区间都已经在前面的条件中覆盖到，
# 所以剩下的，也就只有大于等于85的情况了
else:
    print("优秀")
