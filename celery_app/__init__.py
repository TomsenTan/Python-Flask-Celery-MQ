from flask import Flask
from flask_sqlalchemy  import SQLAlchemy
from config  import SQLConfig


app = Flask(__name__)
app.config.from_object(SQLConfig)
db = SQLAlchemy(app)

app.config['CELERY_BROKER_URL'] = 'amqp://guest@localhost//'
app.config['CELERY_RESULT_BACKEND'] = 'amqp://guest@localhost//'

from celery import Celery
celery_demo = Celery(app.name,broker=app.config['CELERY_BROKER_URL'],backend=app.config['CELERY_RESULT_BACKEND'])
celery_demo.conf.update(app.config)



