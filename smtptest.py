import smtplib

my_email="dorcasafranie1@gmail.com"
password="mgwf kcia lppj hkdt"
recepient="lydiapratt0@gmail.com"

server_connection=smtplib.SMTP("smtp.gmail.com",587)

server_connection.starttls()
server_connection.login(my_email,password)

server_connection.sendmail(my_email, recepient,msg="Greetings")

server_connection.close()
                           