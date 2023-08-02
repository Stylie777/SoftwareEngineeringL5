from django.urls import path
from hello import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("", views.home, name="home"),
    path("hello/<name>", views.hello_there, name="Hello There"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
]
urlpatterns += staticfiles_urlpatterns()
