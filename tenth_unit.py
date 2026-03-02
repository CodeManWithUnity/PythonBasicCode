# 字典
# d1 ={'one': 1, 'two': 2, 'three': 3}
# print(d1)
# a = dict(one=1, two=2, three=3)
# print(a)
#
#
# d = dict([('two', 2), ('one', 1), ('three', 3)])
# print(d)
#
# names= ['Ben', 'Alien', 'Helen']
# nbook = dict.fromkeys(names, "000")
# print(nbook)
# books = {'Ben': '13800897658', 'Helen': '13100349319'}
# h = books['Helen']
# print(h)
# my_info = {
#     'name': 'wenjie',
#     'age': 18,
#     'sex': '不清楚',
#     'hobby': ['抽烟', '喝酒', '烫头']
# }
# print(f"我的姓名是:{my_info['name']},"'\n'
#       f"我的年龄是{my_info.get('age')},"'\n'
#       f"我的性别是{my_info.get('sex', '不知道对不对')},"'\n'
#       f"我的爱好有{','.join(my_info.get('hobby'))}")
#
# 字典的删除
# pop
# books = {'Ben': '13800897658', 'Helen': '13100349319'}
# b = books.pop('Kelen')
# books = {'Ben': '13800897658', 'Helen': '13100349319'}
# b = books.pop('Kelen','110')
# print(b)

# print(b)
# clear
# del
# books = {'Ben': '13800897658', 'Helen': '13100349319'}
# del books
# print(books)
# 用多种方法创建字典，字典内容为{'a':1,'b':3,'c':6}
# 获取值为3
# 删除键值对'b':3
# 清空
# dic = {'a': 1, 'b': 3, 'c': 6}
# dic = dict(a=1, b=2, c=3)
# value = dic.get('c')
# print(value)
# del dic['b']
# dic.clear()

# 字典的遍历
# books = {'Ben': '13800897658',
#                 'Alien': '13710976543',
#                 'Helen': '13100349319'}
# for k in books.keys():
#     print(k)
# for v in books.values():
#     print(v)
# for k,v in books.items():
#     print(k,v)

# 创建一个双色球票字典，key为球的颜色（红色、蓝色）和注数，value为球的号码，手动输入不同球的号码和注数，存到字典并打印。
#
# 红球  1-33   排重
# 蓝球  1-26
# 字典内容  txt  word







# 字典
