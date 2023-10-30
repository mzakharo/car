import pygame
import time
import os
pygame.init()
clock = pygame.time.Clock()
keepPlaying = True

from gpiozero import PWMLED, LED


class Car:
    def __init__(self):
        self.stick = 0.25
        self.en1 = None

    def open(self):
        if self.en1 is not None:
            return
        self.en1 = LED(14)
        self.en2 = LED(15)
        self.left = PWMLED(18)

        self.en3 = LED(19)
        self.en4 = LED(26)
        self.right = PWMLED(13)

    def goleft(self, value):
        if value > 0:
            self.en2.on()
            self.en1.off()
        else:
            self.en1.on()
            self.en2.off()
        self.left.value = abs(value) if abs(value) > self.stick else 0

    def goright(self, value):
        if value > 0:
            self.en4.on()
            self.en3.off()
        else:
            self.en3.on()
            self.en4.off()
        self.right.value = abs(value) if abs(value) > self.stick else 0

    def close(self):
        if self.en1 is None:
            return
        self.en1.close()
        self.en2.close()
        self.en3.close()
        self.en4.close()
        self.left.close()
        self.right.close()
        self.en1 = None

car = Car()

try:
    joystick = pygame.joystick.Joystick(0)
except:
    joystick = None

mac = 'CA:96:AF:F5:AC:A3'

while keepPlaying:
    clock.tick(30)

    if joystick is None:
        os.system(f'bluetoothctl disconnect {mac}')
        os.system(f'bluetoothctl connect {mac}')
        time.sleep(3)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepPlaying = False
        elif event.type == pygame.JOYDEVICEREMOVED:
            joystick.quit()
            print('joystick quit')
            joystick = None
            car.close()
        elif event.type == pygame.JOYDEVICEADDED:
            joystick = pygame.joystick.Joystick(0)
            joystick.init()
            car.open()
            print('joystick init')
        elif event.type == pygame.JOYAXISMOTION:
            car.goleft(joystick.get_axis(1))
            car.goright(joystick.get_axis(3))
