#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from draw import draw

import pygame
import numpy as np

def test_draw():
    screen = draw()
    reference = pygame.image.load("image.png")

    pygame.image.save(screen, "image_test.png")    

    np.testing.assert_almost_equal(
        pygame.surfarray.pixels3d(screen),
        pygame.surfarray.pixels3d(reference)
        )
