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

The project helps developers to use the access tokens generateted by third-party authentication provider (Google, Microsoft) to authentication with Djnago Applicaiton with viarty of option is the settings to customize.

# Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and can be used for production.

# Prerequisites <a name="prerequisites"></a>

What things you need to install the software and how to install them:

Python Version: 3.8 or 3.9 <br />
Enviroment: Pipenv

# Installing  <a name = "installing"></a>

A step by step series of examples that tell you how to get a development env running.

Create Workplace *projectname* (Linux, windows)

```console
$ mkdir projectname
```

Create Virtual Enviroment
navigate to *projectname*

```console
$ python -m install pipenv
$ python -m pipenv install
```

Activate Virtual Enviroment

```console
$ python -m pipenv shell
$ python -m pip install pipenv
```
Install python packages 

```console
$ python -m pipenv install
```
# Settings <a name = "settings"></a>

Change Djnago Secret Key in the .env file

```python
SECRET_KEY='your secret key'
```

Add Google and Microsoft Authentication Providers in the .env file
```python
#Authentication Providers
GOOGLE_CLIENT_ID= "your google client ID"
GOOGLE_SECRET= "your google secret key"
MS_CLIENT_ID= "your MS client ID"
MS_SECRET= "your MS secret key"
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
## install twine package:
```console
    $ python -m pip install --upgrade twine
```
## Update your preferencse:
1. Copy the latest version of "accounts" app to "accounts_package" folder. 
2. Update version in setup.cfg:
```
version = x.x
```
3. Update MANIFIST.in with new installed packages.

4. Update README.md

5. Go to "accounts_package" and run the follwoing to build the package:
```console
$ python -m pipenv install build

$ python -m build
```
6. generate and copy token and password from https://test.pypi.org/

7. push the package to your repo:

```console
$ python -m pipenv install twine 
$ python -m twine upload --repository testpypi dist/*
```

### Useful Links:

Packaging Python Projects:
https://packaging.python.org/en/latest/tutorials/packaging-projects/#uploading-the-distribution-archives