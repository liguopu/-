# 分析一个水杯的属性和功能，使用类描述并创建对象
# 高度，容积，颜色，材质
# 能存放液体

class Cup:
    __height = 0
    __volume = 0
    __colour = ""
    __texture = ""

    #  水杯高度
    def setHeight(self, height):
        if height > 50 or height <= 0:
            print("请输入正确的水杯高度")
        else:
            self.__height = height

    def getHeight(self):
        return self.__height

    #  水杯容积
    def setVolume(self, volume):
        if volume > 2000 or volume <= 0:
            print("请输入正确的水杯容积")
        else:
            self.__volume = volume

    def getVolume(self):
        return self.__volume

    # 水杯颜色
    def setColour(self, colour):
        if colour == "":
            print("水杯颜色不能为空")
        else:
            self.__colour = colour

    def getColour(self):
        return self.__colour

    #  水杯材质
    def setTexture(self, texture):
        if texture == "":
            print("水杯颜色不能为空")
        else:
            self.__texture = texture

    def getTexture(self):
        return self.__texture

    #  打印结果
    def drinking(self):
        print("这是一个高为：", self.__height, "厘米", "容积为：", self.__volume, "毫升", "颜色是：", self.__colour,
              "材质为：", self.__texture, "的水杯")


c = Cup()
c.setHeight(30)
c.setVolume(800)
c.setColour("粉红色")
c.setTexture("玻璃")
c.drinking()
