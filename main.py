import os
import smtplib

contents = ""
with open('../pass.cooler9711@gmail.com.txt') as f:
    for line in f.readlines():
        contents += line
msg = raw_input("what do you want to email? ")
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("darthvader9711@gmail.com", contents)
server.sendmail("darthvader9711@gmail.com", "4358308794@mms.att.net", msg)
server.quit()
print("sent " + msg)