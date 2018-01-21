from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
# from handlers import tcphandler

import socket
import json
# import ast


class Index(View):
    """Index class, just the fronpage of the site."""

    def get(self, request):
        """Get method for the index."""
        s = socket.socket()
        host = socket.gethostname()
        port = 8888
        s.connect((host, port))
        s.send('get')
        data = json.loads(s.recv(2048))
        context = {'objs': data}
        s.close()
        return(render(request, 'panel/dashboard.html', context=context))

    def post(self, request):
        """Post method for index."""
        s = socket.socket()
        host = socket.gethostname()
        port = 8888
        s.connect((host, port))
        s.send('post start instance-2')
        s.close()
        return HttpResponse('hello darkness my old friend')
