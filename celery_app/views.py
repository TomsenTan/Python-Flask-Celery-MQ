from sqlalchemy import event
from flask  import request
from celery_app import app
from celery_app.models  import Reminder
from task import on_reminder_save



@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'GET':
        event.listen(Reminder, 'after_insert', on_reminder_save)
        return 'ok'



if __name__ == '__main__':
    app.run('',8000)

