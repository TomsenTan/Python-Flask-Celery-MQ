BROKER_URL = 'amqp://guest@localhost//'
CELERY_RESULT_BACKEND = 'amqp://guest@localhost//'

CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERT_ACCEPT_CONTENT = ['json']
CELERY_TIMEZONE = 'Europe/Oslo'
CELERY_ENABLE_UTC = True

CELERY_ROUTES = {
    'task.add':'low-priority',  #add方法的权限在队列中较低

}

CELERY_ANNOTATIONS ={          #设置工作程序的时间间隔
    'task.add':{'rate_limit':'10/m'}

}