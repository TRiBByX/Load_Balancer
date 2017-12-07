from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import View

import socket
import ast


class Index(View):
    """Index class, just the fronpage of the site."""

    def get(self, request):
        """Get method for the index."""
        s = socket.socket()
        host = socket.gethostname()
        port = 8888

        s.connect((host, port))

        s.send('get')

        context = {'servers': ast.literal_eval(s.recv(1024))}
        return(render(request, 'panel/dashboard.html', context=context))
