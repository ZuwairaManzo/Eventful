import smtplib
from email.mime.text import MIMEText

def send_email_notification(recipient, subject, body):
    # Implement email sending logic using smtplib or a third-party library
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = 'sender@example.com'
    msg['To'] = recipient

    # Send the email
    s = smtplib.SMTP('localhost')
    s.send_message(msg)
    s.quit()