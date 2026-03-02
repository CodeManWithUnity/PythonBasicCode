# 匿名函数、递归函数
# def funcname(a, b):
#     c = a + b
#     return c
# print(lambda a,b: a+b(1,2))
# 1、匿名函数
# print((lambda x, y, z: x + y + z)(1, 2, 3))
#
# # 2、使用匿名函数但有名字
# f = lambda x, y, z: x + y + z
# print(f(1, 2, 3))
# # 3、匿名函数默认值参数
# g = lambda x, y=2, z=3: x + y + z
# print(g(1))
#
# # 4、匿名函数关键字参数
# g = lambda x, y=2, z=3: x + y + z
# print(g(1, z=4, y=1))

# 斐波那契数列
# def fei_bo_na_qie(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fei_bo_na_qie(n - 1) + fei_bo_na_qie(n - 2)
#
#
# num = fei_bo_na_qie(10)
# print("num的值是", num)

# 月工资按天发放，第一天给你一分钱，然后，后一天是前一天的2倍，那么30天后工资为多少？

# def gong_zi(n):
#     if n <= 0:
#         print("请输入正确的天数")
#     elif n == 1:
#         return 1
#     else:
#         return gong_zi(n-1)*2
#
#
# n = int(input("请输入你想要查询的天数\n"))
# money = float(gong_zi(n) / 100)
# print("第%d天的工资是%f元" % (n, money))

# 使用递归完成以下作业
# 求n - m的累加和

# n = int(input("请输入n的值\n"))
# m = int(input("请输入m的值\n"))
#
#
# def lei_jia_he(num1,num2):
#     if num1 > num2:
#         print("请重新输入数字确保n的值小于m")
#         return "错误答案"
#     elif num1 == num2:
#         # print("累加和为", num1)
#         return num1
#     else:
#         return num1 + lei_jia_he(num1 + 1, num2)
#
#
# result = lei_jia_he(n,m)
# print(result)
# 求n的阶乘

# n = int(input("请输入n的值"))
# def jie_chen(n):
#     if n <= 0:
#         print("你输入的数字有误请重新输入")
#     elif n == 1:
#         return 1
#     else:
#         return n * jie_chen(n - 1)
#
#
# num = jie_chen(n)
# print("num的值是",num)

# 猴子每天吃的比前一天的一半还多1个桃，第十天的时候剩一个桃子，问第一天猴子有多少个桃子？
# 1
# 第十 第九 第八
# def tao_zi(day):
#     if day > 10 :
#         print("吃不到第十天后")
#         return "num False"
#     elif day == 10:
#         return 1
#     else:
#         return (tao_zi(day + 1) + 1) * 2
#
#
# num = tao_zi(1)
# print("第一天有个桃子", num)
