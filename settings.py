from decouple import config

DEBUG = config('DEBUG', default=False, cast=bool)
SQLALCHEMY_DATABASE_URI = config('SQLALCHEMY_DATABASE_URI')
SQLALCHEMY_TRACK_MODIFICATIONS = config('SQLALCHEMY_TRACK_MODIFICATIONS', default=False, cast=bool)
SECRET_KEY = config('SECRET_KEY')
DEBUG_TB_INTERCEPT_REDIRECTS = False
