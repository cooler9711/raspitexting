import os
import smtplib

contents = ""
with open('../pass.darthvader9711@gmail.com.txt') as f:
    for line in f.readlines():
        contents += line
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("darthvader9711@gmail.com", contents)
msg = raw_input("what is the message that you want to send? ")
server.sendmail("darthvader9711@gmail.com", "4358308794@mms.att.net", msg)
server.quit()
print("sent \"" + msg + "\"")