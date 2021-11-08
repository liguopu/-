# 有笔记本电脑（屏幕大小，价格，cpu型号，内存大小，待机时长），行为（打字，打游戏，看视频）
class Laptop:
    __screen = 0
    __money = 0
    __cpu = ""
    __ram = ""
    __time = 0

    #  笔记本电脑属性
    def property(self):
        print("这台笔记本电脑的屏幕大小为:", self.__screen, "寸", "价格是:", self.__money, "元",
              "cpu型号是:", self.__cpu, "内存大小是:", self.__ram, "G", "待机时长是:", self.__time, "小时")

    #  间接赋值与取值  # 屏幕大小
    def setScreen(self, screen):
        if screen <= 0 or screen > 36:
            print("您输入的电脑屏幕大小过大或过小，单位：寸")
        else:
            self.__screen = screen

    def getScreen(self):
        return self.__screen

    # 价格
    def setMoney(self, money):
        if money <= 0:
            print("您输入的电脑价格有误")
        else:
            self.__money = money

    def getMoney(self):
        return self.__money

    #  cpu型号
    def setCpu(self, cpu):
        if cpu == "":
            print("请输入您的cpu型号")
        else:
            self.__cpu = cpu

    def getCpu(self):
        return self.__cpu

    #  内存大小
    def setRam(self, ram):
        if ram <= 0:
            print("请输入正确的内存大小")
        else:
            self.__ram = ram

    def getRam(self):
        return self.__ram

    #  待机时长
    def setTime(self, time):
        if time < 0:
            print("请输入正确的待机时长")
        else:
            self.__time = time

    def getTime(self):
        return self.__time

    #  笔记本电脑行为
    #  打字
    def typing(self, hour):
        print("小明正在使用笔记本电脑打字，已经打了", hour, "小时")

    #  打游戏
    def game(self, hour):
        print("小明正在使用笔记本电脑打游戏", "已经打了", hour, "小时")

    #  看视频
    def video(self, hour):
        print("小明正在用笔记本电脑看视频", "已经看了", hour, "小时")


L = Laptop()
L.setScreen(20)
L.setMoney(8000)
L.setCpu("8核")
L.setRam(1024)
L.setTime(48)
L.typing(1)
L.game(6)
L.video(6)
L.property()
