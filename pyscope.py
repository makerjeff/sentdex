import os
import pygame
import time
import random

class pyscope :
    screen = None;

    def __init__(self):
        "Initializes a new pygame screen using the framebuffer"
        # Based on "python GUI in Linux framebuffer"
        # http://www.karoltomala.com/blog/?p=679
        disp_no = os.getenv("DISPLAY")
        if disp_no:
            print ("I'm rnuning under X display = {0}").format(disp_no)

        # Check which frame buffer drivers are available
        # start fbcon, since directfb hangs with composite output
        drivers = ['fbcon', 'directfb', 'svgalib']
        found = False
        for driver in drivers:
            # make sure that SDL_VIDEODRIVER is set
            if not os.getenv('SDL_VIDEODRIVER'):
                os.putenv('SDL_VIDEODRIVER', driver)
            try:
                pygame.display.init()
            except pygame.error:
                print ('Driver: {0} failed.').format(driver)
                continue
            found = True
            break

        if not found:
            raise Exception('no suitable video driver found!')

        size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
        print ("frame buffer size " + size[0] + " x " + size[1])
        self.screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
        # Clear the screen to start
        self.screen.fill((0,0,0))
        # Init font support
        pygame.font.init()
        # Render screen
        pygame.display.update()

    def __del__(self):
        "Destructor to make sure pygame shuts down, etc"

    def test(self):
        # fill the screen with red(255,0,0)

        red = (255,0,0)
        self.screen.fill(red)
        #update display
        pygame.display.update()

# create instance of pyscope class
scope = pyscope()
scope.test()
time.sleep(10)