import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

body = '''Hello,This is the body of the emailsicerely yoursG.G.'''
sender = ''
password = ''
receiver = ''
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
