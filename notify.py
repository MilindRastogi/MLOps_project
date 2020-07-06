import smtplib
f = open("accuracy.txt' , r)
acc = f.read()

s = smtplib.SMTP(host= 'smtp.gmail.com', port= 587)
s.starttls()
s.login('rashmishrma660@gmail.com' , 'lastsupreme24')
msg = 'Congratulations your accurracy is  {}'.format(acc)
s.sendmail("rashmishrma660@gmail.com", "milindrastogi24@gmail.com", msg)