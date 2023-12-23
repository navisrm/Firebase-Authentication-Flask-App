import smtplib
from email.message import EmailMessage
import sys

def send_email(sender_email, receiver_email, message_body):

    

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    # an email account to send emails, you should use App Pasword otherwise it won't work
    sender = sender_email
    password = 'XXXXXXXXXXXXXX'
    receiver = receiver_email
    server.login(sender, password)
    # sender: example@example.com
    # receiver: the email account which you want to receive emails on

    msg = EmailMessage()
    msg['To'] = receiver
    msg.set_content(message_body)
    server.send_message(msg)


    #server.sendmail(sender, receiver, message_body)
    server.quit()