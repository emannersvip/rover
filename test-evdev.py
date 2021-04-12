#!/usr/bin/env python3

# sudo pip3 install evdev
from evdev import InputDevice, categorize, ecodes
# import evdev

gamepad = InputDevice('/dev/input/event3')

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
    if event.type == ecodes.EV_ABS:
        print((event))
        if event.value == 1:
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
            else:
                print('UNMAPPED')
            