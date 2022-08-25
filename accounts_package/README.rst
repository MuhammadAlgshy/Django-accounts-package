Account Package
===============

Table of Contents
=================

-  `About <#about>`__
-  `Getting Started <#getting_started>`__
-  `Prerequisites <#prerequisites>`__
-  `Installing <#install>`__
-  `Settings <#settings>`__
-  `Run <#run>`__
-  `Test <#test>`__
-  `Build the package <#build_pkg>`__

About 
=====

The package meant will allow you use the access tokens generateted by
third-party authentication provider (Google, Microsoft) to
authentication with Djnago Applicaiton with viarty of option is the
settings to customize.

Prerequisites 
=============

What things you need to install the software and how to install them:

Python Version: 3.8 or 3.9 Enviroment: Pipenv

Installing 
==========

A step by step series of examples that tell you how to get a development
env running.

Navigate to your django project *projectname* (Linux, windows)

.. code:: console

   $ cd projectname

Install python packages

.. code:: console

   $ python -m pipenv install dj-rest-auth
   $ python -m pipenv install django-allauth
   $ python -m pipenv install djangorestframework
   $ python -m pipenv install djangorestframework-simplejwt

Settings 
========

**Import settings from accounts in settings.py:**

.. code:: python

   from accounts.configurations import *

**Add accounts to installed apps:**

.. code:: python

   INSTALLED_APPS = [
       ...
       'accounts',

   ] + ACCOUNTS_APPS

**Add accounts url to url.py in your project:**

.. code:: python

   urlpatterns = [
        ...
       path("", include("accounts.urls")),
   ]

**Add following variables to the envrioment:**

.. code:: python


   #Authentication Providers | if you want to use init_authprovider

   GOOGLE_CLIENT_ID= "your google client id"
   GOOGLE_SECRET= "google secret"

   MS_CLIENT_ID= "your micrsoft client id"
   MS_SECRET= "your secret"

   # Super User Information | if your want to use init_users
   SUPER_USERNAME="email"
   SUPER_PASSWORD="password"

**Customizable Settings**

.. code:: python

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

Run 
===

Install all packages

.. code:: console

   $ python -m pipenv install
   or 
   $ python manage.py init_pkg

Run Database Migration

.. code:: console

   $ python manage.py migrate

Initiate Super user

.. code:: console

   $ python manage.py init_users

Initiate Authentication Social Applications

.. code:: console

   $ python manage.py init_authprovider

Run Django Server

.. code:: console

   $ cd projectname/
   $ python manage.py runserver

Test 
====

APIs
----

1. Google Auth: Go to http://localhost:8000/auth/google (Use the Access
   Token)

2. Microsoft Auth: Go to http://localhost:8000/auth/ms (Use the Access
   Token)

3. Check Auth: Go to http://localhost:8000/auth/secure

Useful Links:
-------------

Google Playground: https://developers.google.com/oauthplayground/

