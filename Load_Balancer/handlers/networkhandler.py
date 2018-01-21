import random
import SimpleHTTPServer
import SocketServer
import socket
from handlers import vmhandler
from handlers import instancehandler


class networkhandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

    def do_GET(self):
        print('do_Get')
        _dict = vmhandler.get_dict()
        ip_list = []
        for key, value in _dict.items():
            if value['ip'] is None:
                pass
            else:
                ip_list.append(value['ip'])
        ran = random.choice(ip_list)
        # ip = '104.197.31.161'

        # print(self.path)

        self.send_response(307)
        new_path = 'http://{}{}'.format(ran, self.path)
        print(new_path)
        self.send_header('Location', new_path)
        self.end_headers()


def serve():
    PORT = 8060
    handler = SocketServer.TCPServer(("", PORT), networkhandler)
    handler.allow_reuse_address = True
    print "serving at port 8060"
    handler.serve_forever()
