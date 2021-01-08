#import smtplib
#from email.mime.multipart import MIMEMultipart 
#from email.mime.text import MIMEText
#msg = MIMEMultipart()
#msg['From'] = 'jassee1@hotmail.com'
#msg['To'] = 'jasseanonymus49@gmail.com'
#msg['Subject'] = 'simple email in python'
#message = 'hatar människor Send with Python 3'
#msg.attach(MIMEText(message))
#mailserver = smtplib.SMTP('SMTP.Office365.com',587)
# identify ourselves to smtp gmail client
#mailserver.ehlo()
# secure our email with tls encryption
#mailserver.starttls()
# re-identify ourselves as an encrypted connection
#mailserver.ehlo()
#mailserver.login('jassee1@hotmail.com', 'sony1111')
#mailserver.sendmail('jassee1@hotmail.com','jasseanonymus49@gmail.com',msg.as_string())
#mailserver.quit()
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

body = '''Hello,This is the body of the emailsicerely yoursG.G.'''
sender = 'jassee1@hotmail.com'
password = 'sony1111'
receiver = 'jasseanonymus49@gmail.com'
message = MIMEMultipart()
message['From'] = sender
message['To'] = receiver
message['Subject'] = 'This email has an attacment, a pdf file'
message.attach(MIMEText(body, 'plain'))
pdfname = 'Dokument1.pdf'
# open the file in bynary
binary_pdf = open(pdfname, 'rb')
payload = MIMEBase('application', 'octate-stream', Name=pdfname)
# payload = MIMEBase('application', 'pdf', Name=pdfname)
payload.set_payload((binary_pdf).read())
# enconding the binary into base64
encoders.encode_base64(payload)
# add header with pdf name
payload.add_header('Content-Decomposition', 'attachment', filename=pdfname)
message.attach(payload)
#use gmail with port
session = smtplib.SMTP('SMTP.Office365.com',587)
#enable security
session.starttls()
#login with mail_id and password
session.login(sender, password)
text = message.as_string()
session.sendmail(sender, receiver, text)
session.quit()
print('Mail Sent')