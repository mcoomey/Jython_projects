import pygame
from pygame.locals import *

def Run():
    while True:
        pressed=pygame.key.pressed()
        if pressed[K_q]:
            exit()
        
        mousepress=pygame.mouse.get_pressed()
        
    return
    
        