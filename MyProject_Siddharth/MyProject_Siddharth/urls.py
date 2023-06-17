from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('greet/', views.greet, name="greet"),
    path('child/', views.child, name="child"),
    path('form/', views.my_form_view, name='my_form'),
]
