# 第一单元 - python基础

# 双色球用户登录界面!
# print('请输入学生姓名')
# name = input()
# print('请输入学生年龄')
# age = int(input())
# print('请输入学生性别')
# sex = input()
#
#
# def is_old():
#     if age > 18:
#         print("这个孩子大于18岁")
#     else:
#         print("这个孩子小于18岁")
#
#
# is_old()


# 案例输入四位数,求个位数，十位数，百位数，千位数

# num = int(input())
# qian_wei = num // 1000
# bai_wei = num // 100 % 10
# shi_wei = num // 10 % 10
# ge_wei = num % 10
# print("输入的数字的千位是", qian_wei)
# print("输入的数字的百位是", bai_wei)
# print("输入的数字的十位是", shi_wei)
# print("输入的数字的个位是", ge_wei)


# 作业：输出一个消费金额实现以下功能
# 1.实现打折功能
#    打八五折后消费金额是多少
# 2.实现抹零功能
#   抹个位，求实际消费金额
#   抹十位，求实际消费金额
#   抹百位，求实际消费金额
# 3.实现满减功能
#    满300减50，求实际消费金额
# print("****消费金额功能****")
# print("--请入你的消费金额---")
# money = int(input())
#
# discount_money = money * 0.85
# print("打折后的价格是", discount_money)
# # 抹个位
# if money >= 10:
#     erase_ge_count = money - (money % 10)
# else:
#     erase_ge_count = money
# print("抹除个位后的价格是", erase_ge_count)
# # 抹十位
# if money >= 100:
#     shi_wei = money // 10 % 10
#     ge_wei = money % 10
#     erase_shi_count = money - (shi_wei * 10 + ge_wei)
# else:
#     erase_shi_count = money
# print("抹除十位后的价格是", erase_shi_count)
# # 抹百位
# if money >= 1000:
#     bai_wei = money // 100 % 10
#     shi_wei = money // 10 % 10
#     ge_wei = money % 10
#     erase_bai_count = money - (bai_wei * 100 + shi_wei * 10 + ge_wei)
# else:
#     erase_bai_count = money
#
# print("抹除百位后的价格是", erase_bai_count)
#
# # 满减功能
# if money >= 300:
#     man_jian_money = money - 50
# else:
#     print("没满300快，满减不了")
#
# print("满减后的价格是", man_jian_money)
# 第一单元 - python基础
