menu = [('宫爆鸡丁', 15), ('红烧肉', 30), ('水煮鱼', 58), ('水果沙拉', 20), ('大拌菜', 15)]
select = []
total = 0
pay = 0
message = []
while True:
    print('''
欢迎光临八维餐厅，请选择
1、查看菜品
2、点餐
3、自助结帐
4、请留言
5、离开餐厅
''')
    print("请输入你想要的功能：")
    n = int(input())
    if n == 1:
        for i in menu:
            print(i)
    elif n == 2:
        # print("请输入菜品名称：")
        # veg_name = input()
        for i, j in enumerate(menu):
            print("%d %s:%s" % (i, j[0], j[1]))
        while True:
            s = int(input("请输入菜品序号, -1则退出选择\n"))
            if s == -1:
                break
            else:
                select.append(menu[s])
            print("您选择的菜品是：")
            for i in select:
                print(i[0])
            print("请稍等你的菜马上好")
    elif n == 3:
        t = 0
        print("您选择的菜品是：")
        for i in select:
            print(i)
            t += i[1]
        print("消费了", t)
        while True:
            pay = int(input())
            if pay >= t:
                print("找零: ", pay - t)
                break
            else:
                print("你支付的金额不够请重新支付")
    elif n == 4:
        mge = input("请输入你的留言")
        message.append(mge)
        y = input("按1可以查看所有留言，按 0 可以离开")
        if y == '1':
            for i in message:
                print(i)
        elif y == 0:
            break
    elif n == 5:
        exit()