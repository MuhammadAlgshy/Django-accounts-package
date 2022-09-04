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

REST_FRAMEWORK = {
    "NON_FIELD_ERRORS_KEY": "error",
    "DEFAULT_RENDERER_CLASSES": ("rest_framework.renderers.JSONRenderer",),
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_AUTHENTICATION_CLASSES": (
        # "rest_framework.authentication.BasicAuthentication",
        # "rest_framework.authentication.SessionAuthentication",
        'rest_framework_simplejwt.authentication.JWTAuthentication', 

    ),
    # "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    # "PAGE_SIZE": 50,
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

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

from datetime import timedelta

SIMPLE_JWT = { 'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30), }