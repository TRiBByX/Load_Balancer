# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse


class Index(View):
    """Index class, just the fronpage of the site."""

    def get(self, request):
        """Get method for the index."""
        return render(request, 'panel/dashboard.html')
