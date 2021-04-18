## How to test smtp

First of all, launch a local smtp server.

- Utility in Module in Shell

~~~bash
python -m smtpd -n -c DebuggingServer localhost:1025
~~~

- Utility in Code

~~~python
from datetime import datetime
import asyncore
from smtpd import DebuggingServer

class EmailServer(DebuggingServer):
    def process_message(self, peer, mailfrom, rcpttos, data, **kwargs):
        print(peer, mailfrom, rcpttos, data, kwargs)                            

def run():
    foo = EmailServer(('localhost', 1025), None)
    try:
        asyncore.loop()
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    run()
~~~

## send email

~~~python
from email.mime.text import MIMEText
import smtplib

def send_email(email_to: str, title: str, subject: str):
    msg = MIMEText(subject, 'plain', 'utf-8')
    msg['From'] = 'a user'
    msg['To'] = email_to
    msg['Subject'] = title

    server = smtplib.SMTP(settings.SMTP_HOST, 25)
    # server.login(settings.SMTP_USER, settings.SMTP_PASSWORD)
    server.sendmail('another user', [email_to], msg.as_string())
    server.quit()
~~~


