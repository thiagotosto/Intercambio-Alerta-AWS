# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText


def send_email(to, mensagem):
	#fp = open(textfile, 'rb')
	# Create a text/plain message
	msg = MIMEText(mensagem['body'])
	#fp.close()
	me = 'thiagotosto@gmail.com'
	you = to
	msg['Subject'] = mensagem['subject']
	msg['From'] = 'intercambioalerta@gmail.com'
	msg['To'] = to

	# Send the message via our own SMTP server, but don't include the
	# envelope header.
	s = smtplib.SMTP('localhost')
	try:
		s.sendmail(me, [you], msg.as_string())
	except:
		raise
	s.quit()
