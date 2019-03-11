import os
from celery import Celery
from flask import Config


#测试用的耦合config
class DevConfig(Config):
    DEBUG = True,
    CELERY_BROKER_URL = 'amqp://guest@localhost:5672//'
    CELERY_BACKEND_URL = 'amqp://guest@localhost:5672//'


from celery_app import  app

app.config.from_object(DevConfig)


def make_celery(app):
     celery = Celery(
         app.import_name,
         broker = app.config['CELERY_BROKER_URL'],
         backend=app.config['CELERY_BACKEND_URL']
     )

     celery.conf.update(app.config)
     TaskBase = celery.Task

     class ContextTask(TaskBase):
          abstract = True

          def  __call__(self,*args,**kwargs):
              with app.app_context():
                   return TaskBase.__call__(self,*args,**kwargs)

     celery.task = ContextTask   

     return celery

env = os.environ.get('WEBAPP_ENV','dev')

flask_app = app

celery = make_celery(flask_app)

