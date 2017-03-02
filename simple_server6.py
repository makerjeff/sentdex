#!/usr/local/bin/python
# writing from scratch

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from time import sleep
import random

#HTTPRequestHandler class
class jwxHTTPRequestHandler(BaseHTTPRequestHandler):

    #overwrite do_GET function (guessing there's a do_POST function too)
    def do_GET(self):

        # ===== BASE PATH =====
        if self.path == '/':
            delay = random.randint(0,3)
            print 'Delaying for ' + str(delay) + ' seconds.'
            sleep(delay)

            #send status
            self.send_response(200)

            #send headers
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            #message to send
            message = '<h1>Hello world from simple_server6!</h1>'

            #write content as utf8
            self.wfile.write(bytes(message))
            return

        elif self.path == '/image':
            delay = random.randint(0,3)
            print 'Delaying for ' + str(delay) + ' seconds.'
            self.send_response(200)
            self.send_header('Content-type', 'image')
            self.end_headers()

            image = open('images/jurassic-park-tour-jeep.jpg')
            self.wfile.write(image.read())
            return

        else:
            delay = random.randint(0,2)
            print 'Delaying 404 for ' + str(delay) + ' seconds.'
            sleep(delay)

            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()

            self.wfile.write('404 error. ')
            return

def run():
    print 'Starting server...'

    #server settings
    server_address = ('127.0.0.1', 3000)

    httpd = HTTPServer(server_address, jwxHTTPRequestHandler)
    print 'Server is running.'
    httpd.serve_forever()

# module switch
if __name__ =='__main__':
    run()