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

            #TODO: continue here.