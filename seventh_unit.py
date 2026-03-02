# 列表list
# list1 = [i for i in range(11)]
# print(list1)
# 利用列表推导式方式生成：
# 1-10之间的奇数
# 10以内可以被3整除的数
# 生成10个随机数，范围在10-30之间
# 字符串s1 ='ABC'，字符串 s2 = '123'，要求：生成序列 A1 A2 A3 B1 B2 B3 C1 C2 C3
# 过滤掉长度小于3的字符串列表，并将剩下的转换成大写字母
#       list1 = ['太白金星', 'fdsaf', 'alex', 'sb', 'ab']
# 题目1
# list1 = [i for i in range(1,11,2)]
# print(list1)
# list2 = [i for i in range(0,10) if i % 3 == 0]
# print(list2)
import random

# list3 = [random.randint(10, 30) for i in range(10)]
# print(list3)
# s1 = 'ABC'
# s2 = '123'
# list4 = [a + b for a in s1 for b in s2]
# print(list4)

# list5 = ['太白金星', 'fdsaf', 'alex', 'sb', 'ab']
#
#
# list6 = [i.upper() for i in list5 if len(i) >= 3]
# print(list6)


# append	在列表末尾追加新的元素对象
# insert	将对象插入列表指定位置
# extend	在列表末尾一次性追加另一个序列中的多个值
# pop       移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
# remove    移除列表中某个值的第一个匹配项
# clear     清空整个列表内数据
# del       删除列表内元素或者整个列表
# menu=["羊肉泡馍","宫保鸡丁","鱼香肉丝"]
# n2 = menu.pop(0)
# print('删除的数据： ', n2)
# print('删除后的列表： ', menu)
# menu=["羊肉泡馍","宫保鸡丁","鱼香肉丝","鱼香肉丝","鱼香肉丝"]
# menu.remove("鱼香肉丝")
# print(menu)
# new_menu = [i for i in menu if i != "鱼香肉丝"]
# print(new_menu)
# 定义一个球号列表，存储1到9共9个数，删除第一个数，并打印删除的这个数
# 然后删除列表中的5，打印现在的列表，
# 最后清空列表，打印列表
# 最后从内存中删除整个列表，打印最后的结果。

# ball_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# first_data = ball_list.pop(0)
# print("第一个删除的数是：", first_data)
#
# ball_list.remove(5)
# print(ball_list)
#
# ball_list.clear()
# print(ball_list)
#
# try:
#     del ball_list
# except:
#     print("这块内存找不到了")
# finally:
#     print("内存找不到")

# sort	原地排序，改变了原列表
# sorted	对原列表进行排序，然后返回排序后的新列表，不改变原列表。





# # 列表list
