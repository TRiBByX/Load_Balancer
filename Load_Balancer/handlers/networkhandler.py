import random
import SimpleHTTPServer
import SocketServer
import socket
from handlers import vmhandler
from handlers import instancehandler


class networkhandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

    def do_GET(self):
        ip_dict = vmhandler.get_ip_dict()
        # ran = random.choice(ip_dict.keys())
        # ip = '104.197.31.161'

        # print(self.path)
        
        self.send_response(307)
        new_path = 'http://{}{}'.format('facebook.com', self.path)
        print(new_path)
        self.send_header('Location', new_path)
        self.end_headers()

def serve():
    PORT = 8070
    handler = SocketServer.TCPServer(("", PORT), networkhandler)
    handler.allow_reuse_address = True
    print "serving at port 8070"
    handler.serve_forever()


