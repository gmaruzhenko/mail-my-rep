import smtplib
import ssl

import config

### OUTDATED!!!!

MSG_FILE = 'message.txt'

port = 465  # For SSL
password = config.PASSWORD

# Create a secure SSL context
context = ssl.create_default_context()

with open(MSG_FILE, 'r') as f:
    message = f.read()


with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(config.SENDER, password)
    # TODO: Send email herea
    server.sendmail(config.SENDER, config.RECIEVER, message)
