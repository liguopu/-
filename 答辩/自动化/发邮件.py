import yagmail


file = "HKR-login.html"

yag = yagmail.SMTP("1066419883@qq.com", "ldbprykqnlalbdjb", "smtp.qq.com")

content = "HKR测试报告"

yag.send("1477710743@qq.com", "测试报告", content, file)
