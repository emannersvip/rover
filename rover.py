#! /usr/bin/env python

import math
from time import sleep
# git clone https://github.com/pimoroni/pantilt-hat.git
import pantilthat
# Camera Guide: Chapter 5, Page 28
# sudo apt install python-picamera python3-picamera
from picamera import PiCamera

# Angular notes
# Pan: -1 = clockwise
#      +1 = counter clockwise
# Tilt:-1 = Up
# Tilt:+1 = Down
# Both Pan & Tilt rotate across a 180 degree plane
# The integer degree is that position on those planes

#angle = math.sin(.2) * 90
#angle = int(angle)
#angle = angle * -1
#print(angle)

pantilthat.pan(-15)
pantilthat.tilt(-38)

camera = PiCamera()
# Resolutions: 4k=3840x2160, 1k=1920x1080, 720p=1280x720, 480p=640x480
camera.start_preview(fullscreen=False, window=(2480,1340,1280,720))
#camera.start_preview()
sleep(5)
camera.stop_preview()
