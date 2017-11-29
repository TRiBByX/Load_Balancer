# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

# Create your views here.
class index(View):
    """Index class, just the fronpage of the site."""

    def get(self, request):
        """Get method for the index."""
        return(HttpResponse('<h1>Welcome to the index</h1>'))
