#! /usr/bin/env python

# XBox One controller
# https://pimylifeup.com/xbox-controllers-raspberry-pi/
# https://www.pygame.org/docs/ref/joystick.html
# sudo apt-get install xboxdrv joystick

import pygame

pygame.init()
screen = pygame.display.set_mode((500, 700))
pygame.joystick.init()

print (pygame.joystick.get_count())

_joystick = pygame.joystick.Joystick(0)
_joystick.init()

print(_joystick.get_init())
print(_joystick.get_id())
print("Name of gamepad: " + _joystick.get_name())
print("Number of axis: " + str(_joystick.get_numaxes()))
print("Axis 0 value: " + str(_joystick.get_axis(0)))
print("Axis 1 value: " + str(_joystick.get_axis(1)))
print("Axis 2 value: " + str(_joystick.get_axis(2)))
print("Axis 3 value: " + str(_joystick.get_axis(3)))
print("Axis 4 value: " + str(_joystick.get_axis(4)))
print("Axis 5 value: " + str(_joystick.get_axis(5)))
#
print("Number of buttons on gamepad: " + str(_joystick.get_numbuttons()))
print("Button 0 value: " + str(_joystick.get_button(0)))
print("Button 1 value: " + str(_joystick.get_button(1)))
print("Button 2 value: " + str(_joystick.get_button(2)))
print("Button 3 value: " + str(_joystick.get_button(3)))
print("Button 4 value: " + str(_joystick.get_button(4)))
print("Button 5 value: " + str(_joystick.get_button(5)))
print("Button 6 value: " + str(_joystick.get_button(6)))
print("Button 7 value: " + str(_joystick.get_button(7)))
print("Button 8 value: " + str(_joystick.get_button(8)))
print("Button 9 value: " + str(_joystick.get_button(9)))
print("Button 10 value: " + str(_joystick.get_button(10)))
print(_joystick.get_numhats())

while not False:

    for event in pygame.event.get():
        if event.type == pygame.JOYBUTTONDOWN:
            print("Joystick button pressed.")
        elif event.type == pygame.JOYBUTTONUP:
            print("Joystick button released.")
        else:
            print("Event is: " + pygame.event.event_name())

pygame.joystick.quit()
pygame.quit()