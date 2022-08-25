from django.urls import path
from .views import *
urlpatterns = [
    path("user/me/", UserAPIView.as_view(), name="user-detail"),
    path('auth/google/', GoogleLogin.as_view(), name='google_login'),
    path('auth/secure/', Secure_api.as_view(), name='secure'),
    path('auth/ms/', MSLogin.as_view(), name='ms'),

]
