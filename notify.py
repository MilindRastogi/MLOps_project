import smtplib
f = open("accuracy.txt" , 'r')
acc = f.read()

s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login('<sender email id>' , '<password>')
msg = 'Congratulations your accurracy is  {}'.format(acc)
s.sendmail("<sender email id> ", "milindrastogi24@gmail.com", msg)
