#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import pygame

def draw():
    size = (40,40)
    screen = pygame.Surface(size)
    screen.fill((255,255,255))
    pygame.draw.aalines(screen, (0,0,0), False, [(10,10),(30,20)])
    return screen
    
def main():
    pygame.image.save(draw(), "image.png")

if __name__ == '__main__':
    main()