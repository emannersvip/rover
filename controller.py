#! /usr/bin/env python

# XBox One controller
# https://pimylifeup.com/xbox-controllers-raspberry-pi/
# sudo apt-get install xboxdrv joystick

import pygame

pygame.joystick.init()

print (pygame.joystick.get_count())

_joystick = pygame.joystick.Joystick(0)
_joystick.init()

print(_joystick.get_init())
print(_joystick.get_id())
print(_joystick.get_name())