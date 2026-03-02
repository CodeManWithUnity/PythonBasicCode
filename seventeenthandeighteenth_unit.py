# 创建”小一”角色，
# 装填子弹5颗，
# 开枪射击5次，输出”小一开枪射击,剩余子弹数x”
# 代码必须符合编码规范。使用面向对象的方式实现
# class Person(object):
#     def __init__(self, ):
#         pass
#     def __new__(cls, *args, **kwargs):
#         pass
#     def set_name(self, name):
#         self.name = name
#
#     def get_name(self):
#         return self.name
#
#     def info(self):
# #         print("我的名字叫:", self.get_name())
# class Person(object):
#     country = "中国"
#     name = ""
#     province = ""
#
#     def set_name(self, name):
#         self.name = name
#
#     def get_name(self):
#         return self.name
#
#     def set_country(self, country):
#         self.country = country
#
#     def get_country(self):
#         return self.country
#
#     def set_province(self, province):
#         self.province = province
#
#     def get_province(self):
#         return self.province
#
#     def info(self):
#         print("我叫%s,籍贯是%s" % (self.get_name(),self.get_province()))
#
#
# xiao_yi = Person()
# xiao_yi.set_name("小一")
# xiao_yi.set_country("中国")
# xiao_yi.set_province("新疆")
# xiao_yi.info()
# 创建登录类class Login(object):
# 定义实例属性username 和password
# username默认：admin
# password默认：123456
# 实现登录验证方法def login_check(self):
# 定义属性self.username获取用户输入账号
# 定义属性self.password获取用户输入密码
# 判断用户名密码是否相同：
# 相同-登陆成功
# 不同-登录失败
# class Login(object):
#     init_username = "admin"
#     init_password = 123456
#
#     def login_check(self):
#
#             self.username = input("请输入用户名\n")
#             self.password = int(input("请输入密码\n"))
#             if self.username == self.init_username and self.password == self.init_password:
#                 print("登录成功")
#             else:
#                 print("登录失败")
#
#
# L = Login()

# 魔法方法

# 打印方法

# 析构方法



# 装饰器
# L.login_check()