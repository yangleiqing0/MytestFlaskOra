import os

secret_key = 'asldfwadadw@fwq@#!Eewew'
basedir = os.path.abspath(os.path.dirname(__file__))
DATABASE_URL = os.path.join(os.path.split(os.path.realpath(__file__))[0],'db\\test.sqlite')
SQLALCHEMY_ECHO = True  # 打印数据库操作语句
base_dir = os.path.join(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base_dir, 'db\\test.sqlite')
SQLALCHEMY_TRACK_MODIFICATIONS = False
# 这个配置将来会被禁用,设置为True或者False可以解除警告信息,建议设置False
debug = True

SQLALCHEMY_COMMIT_TEARDOWN = True

print(DATABASE_URL,SQLALCHEMY_DATABASE_URI)
