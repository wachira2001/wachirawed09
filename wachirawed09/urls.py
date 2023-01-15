
from django.contrib import admin
from wachirawed09 import views
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ProfileApp/', include('ProfileApp.urls')),
    path('', views.home, name="home"),



]
