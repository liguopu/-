t = []
a = {}
f = open("baidu_x_system.log", "r")
line = f.readline()
while line != "":
    s = line[:13]
    line = f.readline()
    t.append(s)
f.close()
for i in t:
    a[i] = t.count(i)
print(a)
