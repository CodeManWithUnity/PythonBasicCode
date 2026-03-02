# 第3单元 -python控制结构及其语句2
# 计算1到100的总和
# i = 1
# num = 0
# while i <= 100:
#     num += i
#     i += 1
#
# print("总和是", num)


# num = 0
# i = 1
# for i in range(1 ,101):
#     num += i
# print("总和是",num)

#
# 计算5的阶乘
# 计算1-100的偶数和
# 计算1-100的奇数和

# print("计算5的阶乘")
# i = 1
# num = 1
# for i in range(1,6):
#     num *= i
#
# print("结果是",num)

# print("计算1-100的偶数和")
# i = 1
# num = 0
# for i in range(1, 101):
#     if i % 2 == 0:
#         num += i
#
# print("1-100的偶数和", num)

# print("计算1-100的奇数和")
# i = 1
# num = 0
# for i in range(1,101,2):
#     num+=i
# print("1-100的奇数和是:",num)

# 需求分析：公鸡5文钱一只，母鸡3文钱一只，小鸡3只一文钱，用100文钱买100只鸡，如何买？
# x = 1
# y = 1
# z = 1
# for x in range(1,100):
#     for y in range(1,100):
#         z = 100 - x- y
#         if (5*x + y + z/3 == 100):
#             print('公鸡：%s,母鸡：%s,小鸡：%s'%(x,y,z))

# # 九九乘法表
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(f"{j}×{i}={i*j}", end="\t")
#     print()  # 换行


# 课后作业
# 求1-10的累加和
# i = 1
# num = 0
# for i in range(1, 11):
#     num += i

# print("1-10的累加和是", num)
# 输入n和m, 求n-m的累加和
# print("请输入n的值")
# n = int(input())
# print("请输入m的值")
# m = int(input())
# if n >= m:
#     print("你输入的数字不规范请重新输入")
# else:
#     num = 0
#     i = n
#     for i in range(n, m + 1):
#         num += i
#         i += 1
# print("%d到%d的累加和是：%d" % (n, m, num))

# 求10的阶乘
# i = 1
# num = 1
# while i < 11:
#     num *= i
#     i += 1
# print("10的阶乘是",num)


# 输入n, 求n的阶乘
# print("请输入n的值")
# n = int(input())
# i = 1
# num = 1
# while i < n + 1:
#     num *= i
#     i += 1
#
# print("%d的阶乘是%d"%(n,num))

# 打印九九乘法表
# print("打印的九九乘法表如下：")
# i = 1
# j = 1
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print("%d*%d=%d" % (j, i, j * i),end='\t')
#     print('\n')
# 输入n和m,打印n行m列图形
# n = int(input())
# m = int(input())
# for i in range(1, n + 1):
#     for j in range(1, m + 1):
#         print("*", end='\t')
#     print('\n')
# 求100-999之间所有的水仙花数
# 补充知识：水仙花数是指一个 3 位数，它的每个位上的数字的 3次幂之和等于它本身
# 例如：1的3次幂 + 5的3次幂+ 3的3次幂 = 153。

# print("100-999之间所有的水仙花数")
#
# for i in range(100, 1000):
#     ge_wei = i % 10
#     shi_wei = i // 10 % 10
#     bai_wei = i // 100
#     if ge_wei ** 3 + shi_wei ** 3 + bai_wei ** 3 == i:
#         print("水仙花数是", i, end='\n')
# 第3单元 -python控制结构及其语句2
