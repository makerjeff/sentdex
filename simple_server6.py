#!/usr/local/bin/python
# writing from scratch

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from time import sleep
import time
import random
from picamera import PiCamera
from io import BytesIO

# create stream
photostream = BytesIO()

def get_photo_from_pi():
    camera = PiCamera()
    camera.resolution = (640,480)
    camera.vflip = True
    camera.hflip = True
    camera.annotate_text = 'From Pi'

    camera.start_preview()
    sleep(2)
    camera.capture(photostream, format='jpeg', quality=15)
    return

#HTTPRequestHandler class
class jwxHTTPRequestHandler(BaseHTTPRequestHandler):

    #overwrite do_GET function (guessing there's a do_POST function too)
    def do_GET(self):

        # ===== BASE PATH =====
        if self.path == '/':
            delay = random.randint(0,1)
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

        # GET IMAGE
        elif self.path == '/image':
            delay = random.randint(0,1)
            print 'Delaying for ' + str(delay) + ' seconds.'
            self.send_response(200)
            self.send_header('Content-type', 'image')
            self.end_headers()

            image = open('images/jurassic-park-tour-jeep.jpg')
            self.wfile.write(image.read())
            return

        elif self.path == '/index':
            print 'No delay, sending index file.'
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            file = open('public/index.html')
            self.wfile.write(file.read())
            return

        elif self.path == '/picamera':
            print 'attempting to capture photo and return'
            get_photo_from_pi()
            self.send_response(200)
            self.send_header('Content-type','image')
            self.end_headers()

            self.wfile.write(photostream.read())
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
    server_address = ('192.168.1.101', 3000)

    httpd = HTTPServer(server_address, jwxHTTPRequestHandler)
    print 'Server is running.'
    httpd.serve_forever()

# module switch
if __name__ =='__main__':
    run()
