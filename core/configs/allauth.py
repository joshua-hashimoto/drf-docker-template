
SITE_ID = 1
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',  # django default
    'allauth.account.auth_backends.AuthenticationBackend',  # new for allauth
)
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_VERIFICATION = None
# ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
