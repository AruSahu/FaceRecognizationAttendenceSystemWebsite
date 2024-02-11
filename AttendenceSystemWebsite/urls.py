"""AttendenceSystemWebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from loginApp import views

app_name = 'loginApp'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    path('login/', include('loginApp.urls')),
    path("success_admin/", views.success_admin, name="success_admin"),
    path("success_teacher/", views.success_teacher, name="success_teacher"),
    path("failed/", views.failed, name="failed"),
    path('admin/', admin.site.urls),
    path("success_teacher/takeAttendence/", views.takeAttendence, name="takeAttendence"),
    path("logout/", views.logout, name="logout"),
    path("upload/", views.send_files, name="uploads"),
    path("uploadCSV/", views.send_files_csv, name="uploadCSV"),
    path("success_teacher/takeAttendence/success_page/", views.success_page, name="success_page"),
    path("success_teacher/checkAttendenceForm/", views.checkAttendenceForm, name="checkAttendenceForm"),
    path("success_teacher/checkAttendence/", views.checkAttendence, name="checkAttendence")

]

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



