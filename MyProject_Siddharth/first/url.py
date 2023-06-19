from django.contrib import admin
from django.urls import path
from first.views import book_list
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name="home"),
    path("add", views.add_book, name="add"),
    path('book-list/', book_list, name='book_list')
]