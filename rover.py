#! /usr/bin/env python

import math
from time import sleep
# git clone https://github.com/pimoroni/pantilt-hat.git
import pantilthat
# Camera Guide: Chapter 5, Page 28
# sudo apt install python-picamera python3-picamera
from picamera import PiCamera
# OpenCV
import cv2
# sudo pip3 install evdev
# https://python-evdev.readthedocs.io/en/latest/tutorial.html
from evdev import InputDevice, categorize, ecodes

#----------------------------------------------------------------
gamepad = InputDevice('/dev/input/event3')
lAnaHori = 00
lAnaVert = 1
lTrig = 2
rAnaHori = 3
rAnaVert = 4
rTrig = 5

dpadHori = 16
dpadVert = 17

aBtn = 304
bBtn = 305
xBtn = 307
yBtn = 308

lBmper = 310
rBmper = 311

select = 314
start = 315
guide = 316

lAnaClick = 317
rAnaClick = 318
#----------------------------------------------------------------
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
sleep(1)
camera.stop_preview()

for event in gamepad.read_loop():
    if event.type == ecodes.EV_ABS or event.type == ecodes.EV_KEY:
        if event.code == aBtn:
            print('A')
        elif event.code == bBtn:
            print('B')
        elif event.code == xBtn:
            print('X')
        elif event.code == yBtn:
            print('Y')
        elif event.code == lBmper:
            print('L_BUMPER')
        elif event.code == rBmper:
            print('R_BUMPER')
        elif event.code == select:
            print('SELECT')
        elif event.code == start:
            print('START')
        elif event.code == guide:
            print('GUIDE')
        elif event.code == lAnaClick:
            print('L_ANA_CLICK')
        elif event.code == rAnaClick:
            print('R_ANA_CLICK')
        elif event.code == dpadHori:
            if int(event.value) < 0:
                print('D_HORI_LEFT')
            elif event.value > 0:
                print('D_HORI_RIGHT')
            else:
                print('D_HORI_?')
        elif event.code == dpadVert:
            if event.value < 0:
                print('D_VERT_UP')
            elif event.value > 0:
                print('D_VERT_DOWN')
            else:
                print('D_VERT_?')
        elif event.code == lAnaHori:
            if event.value < 0:
                print('L_ANA_LEFT')
            elif event.value > 0:
                print('L_ANA_RIGHT')
        elif event.code == lAnaVert:
            if event.value < 0:
                print('L_ANA_UP')
            elif event.value > 0:
                print('L_ANA_DOWN')
        elif event.code == rAnaHori:
            if event.value < 0:
                print('R_ANA_LEFT')
            elif event.value > 0:
                print('R_ANA_RIGHT')
        elif event.code== rAnaVert:
            if event.value < 0:
                print('R_ANA_UP')
            elif event.value > 0:
                print('R_ANA_DOWN')
        else:
            print('UNMAPPED')
            print(event)
