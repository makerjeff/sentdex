# based on this tutorial: http://picamera.readthedocs.io/en/release-1.12/recipes1.html

from time import sleep  #instead of time.sleep
from picamera import PiCamera #OSX won't have this library

camera = PiCamera()
camera.resolution = (1024, 768)
camera.start_preview()
#Camera warmup hold time
sleep(2)
camera.capture('foo1.jpg')