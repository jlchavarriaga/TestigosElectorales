from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config.environment import MAILER
from smtplib import SMTP


class MailerProcess:
    def __init__(self, *recipients, **settings) -> None:
        self._recipients = recipients
        self._settings = settings

    def run(self):
        self._set_email_format(*self._recipients, **self._settings)
        self._send_email()

    def _send_email(self):

        try:
            with SMTP(host=MAILER['HOST'], port=MAILER['PORT'], timeout=MAILER['TIMEOUT']) as conn:
                conn.starttls()
                conn.login(
                    user=MAILER['USERNAME'],
                    password=MAILER['PASSWORD']
                )
                conn.sendmail(
                    from_addr=self._msg['From'],
                    to_addrs=self._msg['To'].split(','),
                    msg=self._msg.as_string()
                )
        except Exception as e:
            raise e

    def _set_email_format(self, *recipients, **settings) -> MIMEMultipart:

        self._msg = MIMEMultipart()

        # Setting of the email message

        self._msg['From'] = MAILER['USERNAME']
        self._msg['To'] = ",".join(recipients)
        self._msg['Subject'] = settings['subject']

        # add in the message body
        self._msg.attach(MIMEText(settings['body'], 'plain'))
