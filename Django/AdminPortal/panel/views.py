from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
# from handlers import tcphandler

import socket
import json
import time
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

        vat = request.body
        vat = vat.replace('[', '')
        vat = vat.replace('"', '')
        vat = vat.replace(',', ' ')
        vat = vat.replace(']', '')
        vat = vat.split(' ')
        print(vat)

        for instance in vat:
            if instance == 'shutdown' or instance == 'start':
                pass
            else:
                s.connect((host, port))
                print('post {} {}'.format(vat[0], instance))
                s.send('post {} {}'.format(vat[0], instance))
                s.close()
                time.sleep(5)

        return HttpResponse('hello darkness my old friend')
