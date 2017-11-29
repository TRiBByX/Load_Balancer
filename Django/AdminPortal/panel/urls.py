from django.conf.urls import url
from panel.views import index
from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^$', index.as_view())
]
