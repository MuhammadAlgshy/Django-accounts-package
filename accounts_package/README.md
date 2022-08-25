# Account Package

# Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Prerequisites](#prerequisites)
- [Installing](#install)
- [Settings](#settings)
- [Run](#run)
- [Test](#test)
- [Build the package](#build_pkg)

# About <a name = "about"></a>

The package meant will allow you use the access tokens generateted by third-party authentication provider (Google, Microsoft) to authentication with Djnago Applicaiton with viarty of option is the settings to customize.

# Prerequisites <a name="prerequisites"></a>

What things you need to install the software and how to install them:

Python Version: 3.8 or 3.9 <br />
Enviroment: Pipenv

# Installing  <a name = "installing"></a>

A step by step series of examples that tell you how to get a development env running.

Navigate to your django project *projectname* (Linux, windows)

```console
$ cd projectname
```
Install python packages 

```console
$ python -m pipenv install dj-rest-auth
$ python -m pipenv install django-allauth
$ python -m pipenv install djangorestframework
$ python -m pipenv install djangorestframework-simplejwt

```
# Settings <a name = "settings"></a>
__Import settings from accounts in settings.py:__
```python
from accounts.configurations import *
```
__Add accounts to installed apps:__
```python
INSTALLED_APPS = [
    ...
    'accounts',

] + ACCOUNTS_APPS
```
__Add accounts url to url.py in your project:__
```python
urlpatterns = [
     ...
    path("", include("accounts.urls")),
]
```
__Add following variables to the envrioment:__

```python

#Authentication Providers | if you want to use init_authprovider

GOOGLE_CLIENT_ID= "your google client id"
GOOGLE_SECRET= "google secret"

MS_CLIENT_ID= "your micrsoft client id"
MS_SECRET= "your secret"

# Super User Information | if your want to use init_users
SUPER_USERNAME="email"
SUPER_PASSWORD="password"

```
__Customizable Settings__
```python
AUTHENTICATION_BACKENDS = [ 
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',

]
AUTH_USER_MODEL = "accounts.User" # User Model to be used in the admin site
pypi-AgENdGVzdC5weXBpLm9yZwIkNWI4YTIxMTYtOGIyMi00OGY0LTkwZTYtNDQ0ZWEyNmUxMWJhAAIleyJwZXJtaXNzaW9ucyI6ICJ1c2VyIiwgInZlcnNpb24iOiAxfQAABiAQWafdMBRKKmn9ZcEsNV3kJj_Ftm58_BYKiTRYaCm3Lw
SITE_ID = 1 # Set your site ID
ACCOUNT_USER_MODEL_USERNAME_FIELD = None 
ACCOUNT_EMAIL_REQUIRED = True # Use email instead of username
ACCOUNT_USERNAME_REQUIRED = False # Disable Uesrname field for authentication
ACCOUNT_AUTHENTICATION_METHOD = 'email' # Use email to authenticate
ACCOUNT_ADAPTER= 'accounts.adapter.MyCustomAdapter' 
SOCIALACCOUNT_ADAPTER= 'accounts.adapter.MyCustomSocialAdapter'
REST_USE_JWT = True # User JWT instead ot Token
JWT_AUTH_COOKIE = 'jwt-auth' # Save jwt as token on client size.
USER_FIRST=True # You have to create the user first before using Google and MS authentication
USER_NOPASSWORD=True # You can Create User without password.
USER_DELETE=False # Allow User Deletion in admin panel
```

# Run <a name = "run"></a>
Install all packages
```console
$ python -m pipenv install
or 
$ python manage.py init_pkg

```
Run Database Migration 
```console
$ python manage.py migrate
```
Initiate Super user 
```console
$ python manage.py init_users
```
Initiate Authentication Social Applications
```console
$ python manage.py init_authprovider
```
Run Django Server 
```console
$ cd projectname/
$ python manage.py runserver
```
 
# Test <a name = "test"></a>
### APIs
1. Google Auth: Go to http://localhost:8000/auth/google (Use the Access Token)

2. Microsoft Auth: Go to http://localhost:8000/auth/ms (Use the Access Token)

3. Check Auth: Go to http://localhost:8000/auth/secure

### Useful Links:

Google Playground: https://developers.google.com/oauthplayground/

<br>
<hr>

# Build the package <a name = "build_pkg"></a>

1. Copy the latest version of "accounts" app to "accounts_package" folder. 
2. Update version in setup.cfg:
```
version = x.x
```
3. Update MANIFIST.in with new installed packages.

3. Update README.md