from django.conf.urls import url
from panel.views import Index
from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^$', Index.as_view(), name='dashboard')
]
