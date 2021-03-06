"""helps_booking_admin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin, auth
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, re_path
from helps_admin import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', views.redirect_view, name=''),
    path('', views.sessions, name='sessions'),
    path('sessions/', views.sessions, name='sessions'),
    path('workshops/', views.workshops, name='workshops'),
    path('advisors/', views.advisors, name='advisors'),
    path('students/', views.students, name='students'),
    path('waiting_list/', views.waiting_list, name='waiting_list'),
    path('reports/', views.reports, name='reports'),
    path('email/', views.email, name='email'),
    path('room/', views.room, name='room'),
    path('message/', views.message, name='message'),
    path('exit/', views.exit, name='exit'),
    path('search_sessions/', views.search_sessions, name='search_sessions'),
    path('edit_session/', views.edit_session, name='edit_session'),
    path('delete_session/', views.delete_session, name='delete_session'),
    path('create_session/', views.create_session, name='create_session'),
    path('create_workshop/', views.create_workshop, name='create_workshop'),
    path('create_advisor/', views.create_advisor, name='create_advisor'),
    path('email/test', views.send_email, name='testemail'),
    path('search_reports/', views.search_reports, name='search_reports')

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_URL)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_URL)
