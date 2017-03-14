from django.conf.urls import url
from shop import views as application

urlpatterns = [
    url(r'^$', application.main, name='index'),
    url(r'^auth', application.auth, name='charges'),
]
