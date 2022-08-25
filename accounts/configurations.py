AUTHENTICATION_BACKENDS = [ # Needed to login by username in Django admin, regardless of `allauth`
'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',

]

ACCOUNTS_APPS = [
    'allauth',
    'allauth.account',
    'dj_rest_auth.registration',
    ########## Auth Providers ##########
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.microsoft',
    "rest_framework",
    'rest_framework.authtoken',
]



AUTH_USER_MODEL = "accounts.User"

SITE_ID = 1
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_ADAPTER= 'accounts.adapter.MyCustomAdapter'
SOCIALACCOUNT_ADAPTER= 'accounts.adapter.MyCustomSocialAdapter'
REST_USE_JWT = True
JWT_AUTH_COOKIE = 'jwt-auth'
USER_FIRST=True
USER_NOPASSWORD=True
USER_DELETE=False