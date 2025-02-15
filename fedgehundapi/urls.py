"""fedgehundapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path
from rest_auth.registration.views import VerifyEmailView
from edgar import views
from filer import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('fedgehund_auth.urls')),
    path('profile/', include('fedgehund_profile.urls')),
    path('api/', include('holdings.urls')),
    path('api/', include('edgar.urls')),
    path('api/', include('filer.urls')),
    #to rectify 'NoReverseMatch at /auth/registration/' issue
    re_path(r'^account-confirm-email/', VerifyEmailView.as_view(), name='account_email_verification_sent'),
	re_path(r'^account-confirm-email/(?P<key>[-:\w]+)/$', VerifyEmailView.as_view(), name='account_confirm_email'),
    re_path(r'^auth/', include('allauth.urls'), name='socialaccount_signup'),
    path('', include('fedgehundui.urls')),
]
