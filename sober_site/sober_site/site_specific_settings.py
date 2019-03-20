"""
This file contains information which is inherently specific to each instance.
It should not be shared (e.g. in a git repo).

The values here are dummy values (which nevertheless should work)

The variables defined here are imported to settings.py

"""

import os

class Container():
    pass

# this is duplicated in settings.py (not DRY but a also no big deal)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key which is used in production secret!
SECRET_KEY = '1234567890abcdefghijklmnopqrstuvwxyz1234567890abcd'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# set this to "deployment_server" for deployment
MACHINE_NAME = "local_dev_server"


FEEDBACK_SENDER = "feedback-sender@your-sober-domain.org"

# this is where the feedback form content is sent to
# set this to the mail address of the admin or main moderator
FEEDBACK_RECEIVER = "moderator@your-sober-domain.org"

EMAIL = Container()


# for testing purposes there are two options: Console-Backend or local dummy smtp-server:

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# python -m smtpd -n -c DebuggingServer localhost:1025
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_USE_TLS = False
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''


ALLOWED_HOSTS = ["127.0.0.1"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


