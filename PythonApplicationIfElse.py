# 判断语句(比较,包含等)：=、>、<、in
# 返回boolean类型的结果
print(5==6)
print(5>6)
print(5<6)
print(1 in [1,2,3])

# 条件语句的语法
# 通过使用 if else 达成逻辑分支
x=12
y=20
if x >= y:
    print("----x is greater than y----")
if x < y:
    print("----x is less than y----")
# 使用if制作OldEnough.py程序

# else 的用法
if x >= y:
    print("----x is greater than y----")
else:
    print("----x is less than y----")
# 使用if-else制作OldEnough.py程序
# 写一个判断输入数字是奇数还是偶数的代码？？

# elif 的用法，可加入多个条件
score = eval(input("What's your test score?\n"))
if score >= 90:
    print("----A----")
elif 90 > score >= 75 :
    print("----B----")
elif 75 > score >= 60 :
    print("----C----")
else:
    print("----D----")

# 与、或 （and、or）的用法
print(1 and 0)
print(0 and 1)
print(1 and 1)
print(0 and 0)
print("----我是分割线----")
print(1 or 0)
print(0 or 1)
print(1 or 1)
print(0 or 0)

# 