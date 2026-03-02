# str = "this is string example....wow!!! this is really string.this is string example....wow!!! this is really string"
# print(str.replace('is', 'was'))
# print(str.replace('is', 'was', 3))
# s3= 'HELLO world'
# s3_low = s3.lower()
# s3_upper = s3.upper()
# print(s3_low)
# print(s3_upper)
# islower()  判断字符串是否全部为小写
# isupper()  判断字符串是否全部为大写
# isdigit( )  判断字符串中是否全部为整数
# Isalpha() 判断字符串中是否全部为纯英文字符
# Isalnum() 判断字符串中是否只包含数字或字母
# isspace() 判断字符串中是否只包含空格，如果有返回Trun反之返回False
import random

# 输入两个字符串，从第一个字符串中删除第二个字符串中所有字符。
# 例如：输入"abcde"和"be"
# 字符串变为“acd”
# print("请输入两个字符串")
# print("请输入第一个")
# s1 = input()
# print("请输入第二个")
# s2 = input()
#
# s3 = ''
#
# for i in range(0, len(s1)):
#     if s1[i] not in s2:
#         s3 += s1[i]
# print(s3)

# 需求说明
# 设计字符分类系统
# 将该字符中的数字、大写、小写以及其他字
#     符分类

# title() 将字符串转化为标题，即所有单词的首字母大写，其他字母小写
# a = "hello World CHINA"
# b = a.title()
# c = a.upper()
# d = a.capitalize()
# print(b)
# print(c)
# print(d)
# split
# str = "Line1-abcdef Line2-abc Line4-abcd "
# print(str)
# print(str.split(' '))
# print(str.split(' ', 1))
# sep = ['Hello', 'world', 'from', 'Python']
# seq = '+'
# print(seq.join(sep))
# sr = "Line1-abcdef   Line2-abc    Line4-abcd   "
# print(sr.split('  '))
# print(sr.split())
# print(sr.split(' ', 1))
# 文章内容如下：
# There are moments in life when you miss someone so much that you
# just want to pick them from your dreams and hug them for real!
# Dream what you want to dream;go where you want to go;be what
# you want to be,because you have only one life and one chance to do
# all the things you want to do.
# 要求：
# 将字符串中所有的符号替换成空格, 保存到变量A
# 将字符串A转换成小写,保存到变量lowA
# 将字符串A转换成大写,保存到变量upA
# sr = '''There are moments in life when you miss someone so much that you
# just want to pick them from your dreams and hug them for real!
# Dream what you want to dream;go where you want to go;be what
# you want to be,because you have only one life and one chance to do
# all the things you want to do.
# '''
#
# A = sr.replace('!', ' ')
# A = A.replace(';', ' ')
# A = A.replace(',', ' ')
# A = A.replace('.', ' ')
# print(A)
# lowA = A.lower()
# print(lowA)
# upA = A.upper()
# print(upA)
# # 要求：
# # 将字符串A所有单词首字母大写，,保存到变量tiA
# # 将字符串A第一个单词首字母大写,保存到变量caA
# # 统计字符串A中单词‘to'的个数，,保存到变量c
# tiA = A.title()
# caA = A.capitalize()
# c = A.count('to')
# print("tiA的值是%s" % tiA)
# print("caA的值是%s" % caA)
# print("c的值是%d" % c)
# replace()		替换的功能的方法
# count()		统计字符串中单词个数
# isalnum()/isascii()		判断字符串是否为纯英文或是数字
# isupper() /is.lower()		判断字符串是否全部为大写或是小写
# split()  		查找某一字符串在另一字符串中的位置
# “”.join （）		连接字符串数组
# str.split(str="分隔符", num=分割次数)	指定分隔符对字符串进行切片
# index() 		是否包含指定的字符
# title() 		所有单词的首字母大写
# capitalize() 		第一个字母转换成大写
# import random
#
# lst = ['python', 'C', 'C++', 'javascript']
# str1 = ('I love python')
# print(random.choice(lst))
#     print(random.choice(str1))
# 生成六位验证码，其中包含大写、小写或数字。
# 思路提示
# 分析需求，根据需求展开思路
# 首先生成字母和数字,并连接成一个字符串
# 从中连续随机抽取4个字符，并连接成字符串

# all_str = 'abcdefghijklmnopqrstyvwxyzABCDEFGHIJKLMNOPQRSTYVWXYZ0123456789'
# yan_zheng_ma = ''
# # # for i in range(0,6):
# # #     cr = random.choice(all_str)
# # #     yan_zheng_ma += cr
# # # print(yan_zheng_ma)
# # yan_zheng_ma = ''.join(random.choices(all_str, k=6))
# # print(yan_zheng_ma)
# yan_zheng_ma = ''.join(random.sample(all_str,k=6))
# print(yan_zheng_ma)