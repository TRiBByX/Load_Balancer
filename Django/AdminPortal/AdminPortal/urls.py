from django.conf.urls import url, include
from django.contrib import admin
from AdminPortal.views import Login

urlpatterns = [
    url(r'^$', Login.as_view()),
    url(r'^admin/', admin.site.urls),
    url(r'^dashboard/', include('panel.urls')),
]
