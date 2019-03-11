from celery_app import celery_demo
import smtplib
from email.mime.text  import MIMEText
from celery_app.models import Reminder

# app = Celery('task',broker = 'amqp://guest@localhost//')
# app.config_from_object('celeryconfig')


@celery_demo.task
def add(x,y):
    x = x+y
    print(x)
    return x


@celery_demo.task(bind=True,ignore_result=True,default_retry_delay=300,max_retries=5)
def remind(self,pk):
    reminder = Reminder.query.get(pk)
    msg = MIMEText(reminder.text)

    msg['Subject'] = 'Log the logger'
    msg['From'] = 'XXX@126.com'
    msg['To'] = 'XXX@126.com'

    try:
        smtp_server = smtplib.SMTP('localhost')
        smtp_server.starttls()
        smtp_server.login('xxxxxx','xxxxxx')
        smtp_server.sendmail('xxxxxxx','xxxxxxm',
                             msg.as_string())
        smtp_server.close()

        return
    except Exception as e:
        self.retry(exc=e)

@celery_demo.task(bind=True, ignore_result=True, default_retry_delay=300, max_retries=5)
def on_reminder_save(mapper,connect,self):
    remind.apply(args=(self.id,),eta=self.date)
