import sys

import config
import apiMailer as mailer
import apiFetchCall as caller

# TODO:
# set up to take in three strings as arguments: NAME, ADDRESS, MESSAGE
# Then  do the following and add a sincerely, \nNAME\nADDRESS at the bottom

def main(name, address, subject, body):
    body = body + '\n\nSincerely,\n' + name + '\n' + address

    address = address.strip().replace(' ','%20')
    try:
        lat, long = caller.getGeo(address)
        reps = caller.getReps(lat, long)

        # Authenticat user to send email
        service = mailer.authenticate()

        # Format and send the mail
        for name, email in reps:
            this_body = 'Dear ' + name + ',\n\n' + body
            message = mailer.create_message('me', email, subject, this_body)
            message = service.users().messages().send(userId='me', body=message).execute()

    except:
        print("Unable to send")
