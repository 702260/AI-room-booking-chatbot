import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def main(args):
    # set up the SMTP server
    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.starttls()
    s.login("priyankasoni2016@gmail.com", "Mommy@1010") #Replace with your own Gmail ID and Google Account App Password
    msg = MIMEMultipart() 
    msg['From']="Priyankasoni2016@gmail.com" #Replace with your own Gmail ID
    msg['To']="Priyankasoni2393@gmail.com" #Replace with your receiver email ID