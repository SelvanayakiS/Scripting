import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('msg.html').read_text())

email = EmailMessage()
email['from'] = 'Master Hacker'
email['to'] = 'abc@gmail.com'
email['subject'] = 'You won $100,000,000'

email.set_content(html.substitute({'name': 'TunTun'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('masterhackermf@gmail.com', 'emfm vetm psir date')
	smtp.send_message(email)
	print('Email sent')
