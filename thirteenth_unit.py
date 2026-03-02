# 函数
# def add(*args):
#     num = 0
#     for i in args:
#         num += i
#     return num
#
#
#
# num_1 = add(1, 2, 3, 4, 5, 6)
#
#
# print(num_1)
# 定义一个login函数，接收用户名和密码2个参数
# 如果用户名和密码正确，打印“欢迎xxx光临八维餐厅”
# 如果不正确，打印“输入有误”
# 正确的用户名：张三
# 正确的密码：666
# name = "张三"
# password = 666
#
#
# def login(inname, inpassword):
#     if inname == name and inpassword == password:
#         print("欢迎xxx光临八维餐厅")
#     else:
#         print("输入有误")
#
#
# input_name = input("请输入用户名：\n")
# input_password = int(input("请输入密码\n"))
# login(input_name, input_password)

# 定义函数实现如下功能：
# 输出1-100之间所有能被7整除但是不能被5整除的数
# def func1():
#     num_list = []
#     for i in range(0, 101):
#         if i % 7 == 0 and i % 5 != 0:
#             num_list.append(i)
#     for i in num_list:
#         print(i, end="\t")
#
#
# func1()


# 定义函数实现如下功能：
# 不断地输入数字，输入b退出，将输入的所有数字返回
# 调用该函数，然后打印出以下内容：总和是多少  有多少个  平均是多少


# def func2():
#     num_list = []
#     while True:
#         num = input("请输入数字,输入b退出\n")
#         if num == 'b':
#             break
#         else:
#             nm = int(num)
#             num_list.append(nm)
#     zong =  zong_he(num_list)
#     print("总和是", zong)
#     gs = ge_shu(num_list)
#     print("个数是:", gs)
#     pj_value = zong / gs
#     print("平均值是", pj_value)
#
#
# def zong_he(num_list):
#     num = 0
#     for i in num_list:
#         num += i
#     return num
#
#
# def ge_shu(num_list):
#     num = len(num_list)
#     return  num
#     # print("数字的个数是", num)
#
# func2()


# 写一个函数，判断用户传入的对象（字符串、列表、元组）的元素是否为空

# def func3(obj):
#     if not isinstance(obj,(str,list,tuple)):
#         raise TypeError(f"只支持字符串、列表、元组，传入的是{type(obj).__name__}")
#     if isinstance(obj, str):
#         return len(obj.strip()) == 0
#     if isinstance(obj, list):
#         return len(obj) == 0
#     if isinstance(obj, tuple):
#         return len(obj) == 0
#
#
# sr1 = ""
# sr2 = 'hello world'
# ls1 = []
# ls2 = ['张三', '李四']
# t1 = ()
# t2 = ("黄瓜", "西红柿")
#
# is_empty = func3(sr1)
# print(is_empty)
#
# is_empty = func3(sr2)
# print(is_empty)
#
# is_empty = func3(ls1)
# print(is_empty)
#
# is_empty = func3(ls2)
# print(is_empty)
#
# is_empty = func3(t1)
# print(is_empty)
#
# is_empty = func3(t2)
# print(is_empty)

# 写函数，统计字符串中有几个字母，几个数字，几个空格，几个其他字符，并返回结果
# def func4(str):
#     letters = 0  # 字母
#     digits = 0  # 数字
#     spaces = 0  # 空格
#     others = 0  # 其他字符
#     for char in str:
#         if char.isalpha():
#             letters += 1
#         elif char.isdigit():
#             digits += 1
#         elif char.isspace():
#             spaces += 1
#         else:
#             others += 1
#     return{
#             'letters': letters,
#             'digits': digits,
#             'spaces': spaces,
#             'others': others
#     }
#
#
# test_cases ="Hello World 123!Python3.9\t\n你好123 ABCdef 2024! @#$%^&*()"
#
# str_dict = func4(test_cases)
#
# for k, v in str_dict.items():
#     print("%s有%d个" % (k, v))

# *args — 可变位置参数
# **kwargs — 可变关键字参数
# def build_profile(name, **kwargs):
#     """构建用户信息，接收任意额外属性"""
#     profile = {"name": name}
#     profile.update(kwargs)  # 将传入的关键字参数合并到profile
#     return profile
#
# # 调用时可以传入任意数量的关键字参数
# user1 = build_profile("张三", age=25, city="北京", hobby="编程")
# print(user1)
# # {'name': '张三', 'age': 25, 'city': '北京', 'hobby': '编程'}
#
# user2 = build_profile("李四", age=30, email="li@example.com", vip=True)
# print(user2)
# # {'name': '李四', 'age': 30, 'email': 'li@example.com', 'vip': True}
# def inspect_kwargs(**kwargs):
#     print(f"kwargs 类型: {type(kwargs)}")
#     for key, value in kwargs.items():
#         print(f"  {key}: {value}")
#
# inspect_kwargs(a=1, b=2, c=3)


# 函数
