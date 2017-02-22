#!/usr/local/bin/python

# TODO: work on this as the basis for photocapture.

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from time import sleep
import random


#HTTPRequestHandler class
class jwxHTTPRequestHandler(BaseHTTPRequestHandler):

    #overwritten do_GET function
    def do_GET(self):

        # ===== BASE PATH =====

        if self.path == '/':

            # artificial delay
            delay = random.randint(0,5)
            print 'Delaying for ' + str(delay) + ' seconds.'
            sleep(delay)

            #send status
            self.send_response(200)

            #send headers
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            #send message to client
            message = '<h1>Hello world from simple_server3!</h1>'

            #write content as utf8
            self.wfile.write(bytes(message))
            return

        # ===== DATA PATH =====
        elif self.path == '/data':
            delay = random.randint(0,2)
            print 'Delaying data for ' + str(delay) + ' seconds.'
            sleep(delay)

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            message = '{status: "success", payload: {message: "some data"}}'
            self.wfile.write(message)
            return

        # ===== 404 ERROR =====
        else:
            delay = random.randint (0,2)
            print 'Delaying 404 for ' + str(delay) + ' seconds.'
            sleep(delay)

            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()

            self.wfile.write('404 error. ')
            return

# MAIN LOOP
def run():
    print 'Attempting to start server...'

    #server settings
    server_address = ('127.0.0.1', 3000)

    httpd = HTTPServer(server_address, jwxHTTPRequestHandler)
    print 'Server is running...'
    httpd.serve_forever()

# module switch
if __name__ == '__main__':
    run()