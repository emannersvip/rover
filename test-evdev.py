#!/usr/bin/env python3

# sudo pip3 install evdev
# https://python-evdev.readthedocs.io/en/latest/tutorial.html
from evdev import InputDevice, categorize, ecodes
# import evdev

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

print(gamepad)

for event in gamepad.read_loop():
    #print(categorize(event))
    #if event.type == ecodes.EV_KEY:
    #if event.type == ecodes.EV_ABS:
    if event.type == ecodes.EV_ABS or event.type == ecodes.EV_KEY:
        #print(event)
        #print(categorize(event))
        #if event.value == 1 or event.value == 0 or event.value == -1:
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
    #else:
        #print('Unknown ecode')
        #print(event)
        #print(categorize(event))