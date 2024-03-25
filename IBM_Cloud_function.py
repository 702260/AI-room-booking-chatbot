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
    phone = args.get("phone")
    date = args.get("date")
    time = args.get("time")
    message = f"Hello team, \nThis is your AI Chatbot. We got a room booking request at {date} {time}. Phone number is {phone}. \n\nThanks and Regards,\nyour AI Chatbot."
    msg.attach(MIMEText(message, 'plain'))
    s.send_message(msg)
    return {message : 'Email Sent'}
