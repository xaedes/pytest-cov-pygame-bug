
Running the test code with "./test_draw.py" will pass.
Running the test code with "coverage run ./test_draw.py" will NOT pass.

The code draws an antialiased line using pygame. This is tested against an reference image 'image.png'.

It should look like 'image.png'. But using "coverage .." will result in 'image_test.png'
