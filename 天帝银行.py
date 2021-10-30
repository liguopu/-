#
# 字典开发
# 1.编程实现：仔细业务之间的包含关系，并完成以下编程需求，要适当提高代码的可复用性。
# a)用户：账号（str：系统随机产生8位数字）、姓名(str)、密码(int:6位数字)、地址、存款余额(int)、开户行（银行的名称（str））写死的！
# b)地址：国家(str)、省份(str)、街道(str)、门牌号(str)
# c)银行：能存储100用户的库(字典)、本银行名称（比如：中国工商银行的昌平支行,str）
# i.银行业务功能
# 1.添加用户（传入参数：用户的所有信息。返回值：整型值（1：成功，2：用户已存在，3：用户库已满））
# a)业务逻辑：
# 先检查该用户的账号在库里是否存在。若不存在则在用户库里添加一个该用户并返回代号1
# 若存在则返回代号2。另外在添加用户的时候检测用户库是否已注册满，若已满则返回代号3
# 2.存钱（传入值：用户的账号、存取的金额。返回值：布尔类型值）
# a)业务逻辑：
# 先根据传入的账号信息查询用户库里是否有该用户。若没有则返回False
# 若有，则将该用户的金额存进去。
# 3.取钱（传入值：用户的账号，用户密码，取钱金额。返回值：整型值（0：正常，1：账号不存在，2：密码不对，3：钱不够））
# a)业务逻辑：
# 先根据账号信息来查询该用户是否存在，若不存在，则返回代号1，
# 若存在，则继续判断密码是否正确，若不正确，则返回代号2。
# 若账号密码都正确，则继续判断当前用户的金额是否满足要取出的钱，若不满足，则返回代号3，
# 若满足，则将该用户的金额减去。
# 4.转账（传入值：转出的账号，转入的账号，转出账号的密码，转出的金额。返回值：0：正常，1：账号不对，2密码不对，3钱不够）
# a)业务逻辑：
# 先查询用户库是否存在转出和转入的账号，若不存在则返回代号,1，
# 若账号都存在则继续判断转出账号的密码是否正确，若不正确，则返回2，
# 若正确则继续判断要转出的金额是否足够，若不够则返回3，
# 否则正常转出，转出的账号用户金额要相对应的减少，转入的金额相对应的增加。
# 5.查询账户功能（传入值：账号，账号密码，返回值：空）
# a)业务逻辑：
# 先根据账号判断用户库是否存在该用户，若不存在则打印提示信息：该用户不存在。
# 否则继续判断密码是否正确。若不正确则打印相对应的错误信息。
# 若账号和密码都正确，则将该用户的信息都打印出来，比如：当前账号：xxxx,密码:xxxxxx,余额：xxxx元，用户居住地址：xxxxxxxxxxxxx，当前账户的开户行：xxxxxxxxxx.
# d)界面类：在执行该入口程序时，就打印银行业务选择菜单：比如：
# i.
# ii.然后就开始处理各种输入操作，直到业务处理完成!
import random

print("""
*************************
*       天帝银行         *
*      账户管理系统       *
*************************
        
*1.开户                 *
*2.存钱                 *
*3.取钱                 *
*4.转账                 *
*5.查询                 *
*6.欢迎下次光临           *
************************
""")
# 初始化银行
bank = {}
bank_name = "天帝银行"


# 定义添加到银行
def bankadd(account, name, password, country, province, street, door):
    if len(bank) >= 100:
        return 3
    elif name in bank:
        return 2
    else:
        bank[name] = {
            "account": account,
            "password": password,
            "country": country,
            "province": province,
            "street": street,
            "door": door,
            "money": 0,
            "bank_name": bank_name
        }
        return 1


# 定义开户参数
def user():
    account = random.randint(10000000, 99999999)
    name = input("请输入您的名称")
    password = input("请输入您的密码")
    print("请输入您的详细信息")
    country = input("\t请输入您的国籍")
    province = input("\t请输入您的省份")
    street = input("\t请输入您的街道")
    door = input("\t请输入您的门牌号")
    num = bankadd(account, name, password, country, province, street, door)
    if num == 3:
        print("本银行已满请到其他银行开户")
    elif num == 2:
        print("用户已存在")
    elif num == 1:
        print("恭喜你开户成功，一下是您的相信信息")
        info = '''    
                   ------------个人信息------------
                   用户名:%s
                   账号：%s
                   密码：******
                   国籍：%s
                   省份：%s
                   街道：%s
                   门牌号：%s
                   余额：%s
                   开户行名称：%s
               '''
        # 每个元素都可传入%
        print(info % (name, account, country, province, street, door, bank[name]["money"], bank_name))


# 存钱
def save():
    q = input("请输入您的用户名：")
    if q in bank:
        print("您的存款余额为：", bank[q]["money"])
        w = int(input("请输入您要存款的金额："))
        if w >= 0:
            bank[q]["money"] = bank[q]["money"] + w
            print("存钱成功，您当前账户余额为：", bank[q]["money"])
        else:
            print("输入错误")
    else:
        print("您输入的用户名不存在")
        return False


# 取钱    0：正常，1：账号不存在，2：密码不对，3：钱不够
def draw():
    e = input("请输入您的用户名：")
    r = input("请输入您的密码：")
    if e in bank:
        if r == bank[e]["password"]:
            print("您的用户名为：", e, "您的账户余额为：", bank[e]["money"])
            t = int(input("请输入您的取款金额"))
            if t <= bank[e]["money"]:
                bank[e]["money"] = bank[e]["money"] - t
                print("正常")
                print("您的取款金额为：", t, "您的余额为:", bank[e]["money"])
            elif t > bank[e]["money"]:
                print("钱不够")
        else:
            print("密码不对")
    else:
        print("账号不存在")


# 转账
# 4.转账（传入值：转出的账号，转入的账号，转出账号的密码，转出的金额。返回值：0：正常，1：账号不对，2密码不对，3钱不够）
# a)业务逻辑：
# 先查询用户库是否存在转出和转入的账号，若不存在则返回代号,1，
# 若账号都存在则继续判断转出账号的密码是否正确，若不正确，则返回2，
# 若正确则继续判断要转出的金额是否足够，若不够则返回3，
# 否则正常转出，转出的账号用户金额要相对应的减少，转入的金额相对应的增加。

def eft_(name, password, payee, money):
    if name in bank:
        if password == bank[name]["password"]:
            if payee in bank:
                if money <= bank[name]["money"]:
                    bank[name]["money"] = bank[name]["money"] - money
                    bank[payee]["money"] = bank[payee]["money"] + money
                    print("转账成功，您的余额为：", bank[name]["money"])
                else:
                    return 3
            else:
                return 1
        else:
            return 2
    else:
        return 0


def eft():
    name = input("请输入您的用户名：")
    password = input("请输入您的密码：")
    payee = input("请输入收款人的用户名：")
    money = int(input("请输入您要转出的金额："))
    num = eft_(name, password, payee, money)
    if num == 0:
        print("您的用户名不存在")
    elif num == 1:
        print("收款人用户名不存在")
    elif num == 2:
        print("您的密码错误")
    elif num == 3:
        print("转账失败，余额不足")


# 查询
def inquire():
    name = input("请输入要查询的用户名")
    password = input("请输入要查询到用户名的密码")
    if name in bank:
        if password == bank[name]["password"]:
            print("您的用户名为：", name, "您的账户余额为：", bank[name]["money"])
        else:
            print("您输入的用户名密码错误")
    else:
        print("您输入的用户名不存在")


while True:
    index = int(input("请输入您要办理的业务："))
    if index == 1:
        print("开户")
        user()
    elif index == 2:
        print("存钱")
        save()
    elif index == 3:
        print("取钱")
        draw()
    elif index == 4:
        print("转账")
        eft()
    elif index == 5:
        print("查询")
        inquire()
    elif index == 6:
        print("下次光临")
        break
