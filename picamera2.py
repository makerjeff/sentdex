# based on this tutorial: http://picamera.readthedocs.io/en/release-1.12/recipes1.html
# editing this directly on the Pi.

from time import sleep  #instead of time.sleep
from picamera import PiCamera #OSX won't have this library

camera = PiCamera()
camera.resolution = (1024, 768)
camera.vflip = True
camera.hflip = True
camera.annotate_text = 'herro wold.'


camera.start_preview()
#Camera warmup hold time
sleep(2)

# modifying to have 50% quality.
camera.capture('foo2b.jpg', (2592, 1944, 35) )
