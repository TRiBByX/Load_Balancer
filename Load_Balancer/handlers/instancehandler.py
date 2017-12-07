from models import models
from handlers import vmhandler
import socket
import threading
import json


def instanceLoop():
    """A loop that keeps the tcp client running."""
    try:
        while True:
            tcpLoop()
    except KeyboardInterrupt:
        return None


def tcpLoop():
    """A TCP loop that handles incoming command calls."""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 8888
    print(host, port)
    s.bind((host, port))

    s.listen(1)
    c = None

    while True:
        if c is None:
            print('[No connection established]')
            c, addr = s.accept()
            print('[Connection established with: {}]'.format(addr))
        else:
            print('[Waiting for command...]')
            data = c.recv(1024)
                # TODO: Build command structure underneath.
            if not data:
                break

            data = data.split(' ')
            if data[0] == 'get':
                print 'I GOTS IT!'
                _dict = vmhandler.get_ip_dict()
                _dict = json.dumps(_dict)
                print(_dict)
                c.send(_dict)
            elif data[0] == 'post':
                print 'post'
