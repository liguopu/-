'''
任务：开始金币有5个金币，每猜一次减一个为0就退出（or充钱）猜错3次也退出
'''
import random
randint=random.randint(1, 10)#随机生成数字的范围
print(randint)
k=1
j=5
while k<=3:
    print("您当前剩余金币为：",j)
    num=int(input("请输入您猜的数字"))
    if num==randint:
        print("恭喜您猜对了😀")
        break
    elif num>randint:
        j=j-1
        print("不好意思，您猜大了哦😔，金币数-1")
    elif num<randint:
        print("不好意思，您猜小了哦😔，金币数-1")
        j=j-1
    k=k+1