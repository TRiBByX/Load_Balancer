from django.conf.urls import url
from panel.views import Index

urlpatterns = [
    url(r'^$', Index.as_view(), name='dashboard')
]
