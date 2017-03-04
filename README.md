# NOTES
- [Adafruit: Pi Video Output Using Pygame tutorial](https://learn.adafruit.com/pi-video-output-using-pygame/pointing-pygame-to-the-framebuffer)
- [ProgramArcadeGames.com](http://programarcadegames.com/index.php?lang=en&chapter=python_as_calculator)
- [OpenCV 3.0.0-dev documentation: Getting started with Videos](http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html): This is where Sentdex tutorials originate I think. (DO ME!)
- [OpenCV Video Writer on Mac OS X: FourCC compressions that work ](https://gist.github.com/takuma7/44f9ecb028ff00e2132e) (IMPORTANT!)
- [MatPlotLib Colors](http://matplotlib.org/examples/color/named_colors.html)
- [PythonProgramming.net: Basics](https://pythonprogramming.net/python-3-loop-tutorial/?completed=/python-3-variables-tutorial/)
- [Python IO: Core tools for working with streams](https://docs.python.org/2/library/io.html)
- [Python_for_SS](http://www-rohan.sdsu.edu/~gawron/python_for_ss/course_core/book_draft/anatomy/files.html)
- [Python: Difference between Text and Binary modes](http://stackoverflow.com/questions/9644110/difference-between-parsing-a-text-file-in-r-and-rb-mode/9644141#9644141)
- [RPi OpenCV tutorial](http://rpihome.blogspot.com/2015/03/face-detection-with-raspberry-pi.html)
- [Python OpenCV: Basic Image Manipulations](http://www.pyimagesearch.com/2014/01/20/basic-image-manipulations-in-python-and-opencv-resizing-scaling-rotating-and-cropping/) Scale, Rotate, etc.
- [Picamera Module Documentation](http://picamera.readthedocs.io/en/release-1.12/recipes1.html): Picamera tutorials.
- [Python BaseHTTPServer documentation](https://wiki.python.org/moin/BaseHttpServer)
- [Python BareBones HTTP Server](https://daanlenaerts.com/blog/2015/06/03/create-a-simple-http-server-with-python-3/)
- [Python Original (more advanced) HTTP Server](https://www.junian.net/2014/07/simple-http-server-and-client-in-python.html): This one parses a file-read on command and returns the data in the file. 
- [Stack Overflow: Writing Image Files with Basic Python Server](http://stackoverflow.com/questions/28567733/how-to-encode-image-to-send-over-python-http-server): Also serves as an example for getting different routes.
- [How to relink OpenCV when it disappears](http://stackoverflow.com/questions/21140953/opencv-installed-but-not-linked-error-message-on-os-x-mavericks): Use 'brew link opencv3 --force'.
- [Setting OpenCV webcam resolutions](http://answers.opencv.org/question/34461/how-to-set-camera-resolution-webcam-with-opencv/): with cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
- [Flask: Python Web Framework](https://www.fullstackpython.com/flask.html) (USE ME! Required for Socket.io)
- [Python Socket.IO](https://python-socketio.readthedocs.io/en/latest/) (USE ME!)
- [OpenCV3.0.0-dev docs: Python Tutorials List](http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_feature2d/py_table_of_contents_feature2d/py_table_of_contents_feature2d.html): Feature Detection and Description track.  DO ME.
- [Python time.clock()](http://stackoverflow.com/questions/18169099/python-get-milliseconds-since-epoch-millisecond-accuracy-not-seconds1000): Use this for accurate benchmarking in python.
- [Python OpenCV Face Recognition](http://hanzratech.in/2015/02/03/face-recognition-using-opencv.html)
- [Python 'With' statement](http://effbot.org/zone/python-with-statement.htm)
- [**PiCamera Documentation**](https://picamera.readthedocs.io/en/release-1.12/recipes1.html): Includes a basic streaming tutorial.
- [SimpleCV](http://simplecv.org/): A better CV library for Python?
- [Python Module of the Week: TCP/IP Client and Server](https://pymotw.com/2/socket/tcp.html)
- [Python Time Module: strftime()](https://docs.python.org/2/library/time.html#time.strftime)
    - Time string for Python: time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime())


#Google Python
- [Google Developers Python Introduction](https://developers.google.com/edu/python/introduction)
- special variable "__name__" is equal to "__main__" when module is run directly.  Use this to check if it's an imported module.
- [Google Developers Python Strings](https://developers.google.com/edu/python/strings)
- file.tell() = gives position of file cursor.
- file.seek(0, 0) = sets the cursor position.
- file.readline() = reads up until \n (?)