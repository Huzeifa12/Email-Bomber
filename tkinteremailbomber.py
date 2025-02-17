import smtplib
from tkinter import *

root=None
emailText=None
passwordText=None
recipientEmailText=None
mey_msgText=None
UpdateText=None



def bomber():
    email=emailText.get()
    r_email=recipientEmailText.get()
    password=passwordText.get()
    message=my_msgText.get()
    
    my_connection=smtplib.SMTP("smtp.gmail.com",587)
    my_connection.starttls()
    my_connection.login(email,password)
    a=1
    while a<20:
        my_connection.sendmail(email,r_email,message)
        updateText.set(f"You have bombed  for {a} time(s)")
        a+=1
        
    my_connection.close()
    
    print("Hello")
    
    
def emailEntry():
    global emailText
    emailLabel=Label(root,text="ENTER EMAIL")
    emailLabel.pack()
    emailText=Entry(root)
    email=emailText.get()
    emailText.pack()
    
    
    
def passwordEntry():
    global passwordText
    passwordLabel=Label(root,text="ENTER PASSWORD")
    passwordLabel.pack()
    passwordText=Entry(root)
    passwordText.pack()
    password=passwordText.get()
        
def recipientEmailEntry():
    global recipientEmailText
    recipientEmailLabel=Label(root,text="ENTER RECIPIENT EMAIL HERE")
    recipientEmailLabel.pack()
    recipientEmailText=Entry(root)
    recipientEmailText.pack()
    recipient_email=recipientEmailText.get()
    
def messageEntry():
    global my_msgText
    
    messageLabel=Label(root, text="ENTER MESSAGE HERE")
    messageLabel.pack()
    my_msgText=Entry(root)
    my_msgText.pack()
    
def updateBarEntry():
    global updateText
    
    updateText=StringVar()
    updateText.set("")
    updateLabel=Label(root, textvariable=updateText)
    updateLabel.pack()
    
    
    
def main():
    
    root=Tk()
    emailEntry()
    passwordEntry()
    recipientEmailEntry()
    messageEntry()
    
    my_botton=Button(root,text="Bomb" ,command=bomber)
    my_botton.pack()
    updateBarEntry()
    root.mainloop()
    
   

main()
