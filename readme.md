
Testing this code with "py.test" will pass.
Testing this code with "py.test --cov=." will NOT pass.

The tested code draws an antialiased line using pygame.

It should look like 'image.png'. But using "--cov=." will result in 'image_test.png'
