import smtplib
import passwords as pwd

my_email=pwd.my_email
password=pwd.password
recepient=pwd.recepient

server_connection=smtplib.SMTP("smtp.gmail.com",587)

server_connection.starttls()
server_connection.login(my_email,password)

server_connection.sendmail(my_email, recepient,msg="Greetings")

server_connection.close()
                           

changes="git changes v3 to v3.6"