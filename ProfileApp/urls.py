from django.urls import path
from ProfileApp import views
urlpatterns = [
    path('idol', views.idol, name="idol"),
    path('interests', views.interests, name="interests"),
    path('profile', views.profile, name="profile"),
    path('product', views.product, name="product"),
    path('stuy', views.study, name="study"),

]