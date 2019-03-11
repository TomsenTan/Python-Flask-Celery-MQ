from celery_app import celery_demo
import smtplib
from email.mime.text  import MIMEText
from celery_app.models import Reminder



@celery_demo.task
def add(x,y):
    x = x+y
    print(x)
    return x

#发送邮件
@celery_demo.task(bind=True,ignore_result=True,default_retry_delay=300,max_retries=5)
def send(self):
    msg = MIMEText('This is a test Email send from a celery task')

    msg['Subject'] = 'Log the logger'
    msg['From'] = 'XXXXXX@126.com'
    msg['To'] = 'XXXXXXe@126.com'

    try:
        smtp_server = smtplib.SMTP('localhost')
        smtp_server.starttls()
        smtp_server.login('XXXXX@126','XXXXXX')
        smtp_server.sendmail('XXXXXX@126','XXXXXX@126.com',
                             msg.as_string())
        smtp_server.close()

        return
    except Exception as e:
        self.retry(exc=e)
#
# @celery_demo.task(bind=True, ignore_result=True, default_retry_delay=300, max_retries=5)
# def on_reminder_save(mapper,connect,self):
#     remind.apply(args=(self.id,),eta=self.date)
