from flask import Config

class SQLConfig(Config):
  SQLALCHEMY_DATABASE_URI =  'mysql+pymysql://root:123456@localhost:3306/celery_email_demo'
  SQLALCHEMY_TRACK_MODIFICATIONS = True
  SQLALCHEMY_COMMIT_TEARDOWN = True
  SQLALCHEMY_COMMIT_ON_TEARDOWN = True


