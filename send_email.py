#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Import smtplib for the actual sending function
import os, mimetypes
import smtplib
import email
import email.MIMEMultipart
import email.MIMEBase
import email.MIMEText
import datetime
from datetime import date
from email import Utils
from email.mime.image import MIMEImage

def send(message, receivrers, subject='Don\'t have Subject'):

    filename = "/data/boyu/token_issue/temp/analysis_result.html"
    # Open a plain text file for reading.  For this example, assume that
    # the text file contains only ASCII characters.
    # Create a text/plain message
    target = open(filename, 'w')
    target.write(message[0])
    target.close()
#    msg = email.MIMEText.MIMEText(message[1], _subtype="html", _charset="utf-8")

    # me == the sender's email address
    # you == the recipient's email address
    msg = email.MIMEMultipart.MIMEMultipart('related')
    msgText = email.MIMEText.MIMEText(message[1], 'html', 'utf-8')
    msg.attach(msgText)
    msg['Subject'] = subject + ' at ' + (date.today() + datetime.timedelta(days=-1)).strftime('%Y-%m-%d')
    msg['From'] = "example@xxx.com"
    msg['To'] = ", ".join(receivrers)
    if os.path.exists(filename):
	att = email.MIMEText.MIMEText(open(filename, 'rb').read(), 'base64', 'utf-8')
	att["Content-Type"] = 'application/octet-stream'
	att.add_header("Content-Disposition", "attachment", filename = os.path.basename(filename))
	msg.attach(att)
    #msg = email.MIMEText.MIMEText(message[1], _subtype="html", _charset="utf-8")

    # Send the message via our own SMTP server, but don't include the
    # envelope header.
    s = smtplib.SMTP('stmp.xxx.com')
    #s.login("bo.yu", "YUjz0123456")
    s.sendmail("example@xxx.com", receivrers, msg.as_string())
    s.quit()
