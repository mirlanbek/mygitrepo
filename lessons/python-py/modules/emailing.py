---- from server ----


def send_email(mesg):
    from email.message import EmailMessage
    msg=EmailMessage()
    msg["To"] = "mirlan.tokonbekov@gmail.com"
    msg["Subject"] = "DO NOT REPLY"
    process = subprocess.Popen(['/usr/lib/sendmail', '-t'], stdin=subprocess.PIPE)
    msg.set_content(mesg.strip())
    process.communicate(input=msg.as_bytes())

mesg="Salam kat"
send_email(mesg)




---------------- from email ---------------------


import smtplib
import time


port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = " mirlanadyk@gmail.com "
receiver_email = "mirlan.tokonbekov@gmail.com"
password = " ogxq3spvb3ea4dlnsd "

message = """\
Subject: DUT's status table

{} is not accessible."""

def send(ip):

    smtpObj = smtplib.SMTP(smtp_server, port)
    smtpObj.starttls()
    smtpObj.login(sender_email, password)
    time.sleep(1)
    smtpObj.sendmail(sender_email, receiver_email, message.format(ip))
    smtpObj.close()
send(123)
