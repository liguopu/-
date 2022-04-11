import yagmail


file = "movie.html"

yag = yagmail.SMTP("1066419883@qq.com", "ldbprykqnlalbdjb", "smtp.qq.com")

content = "movie添加影院测试报告"

yag.send("761962053@qq.com", "测试报告", content, file)
