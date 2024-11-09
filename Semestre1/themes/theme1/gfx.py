import studentlib.gfx as gfx
from typing import Image

#Exercice 1.9
#Question 1
gfx.show_image(gfx.draw_line(-0.5, 0.2, 0.7, -0.5))

#Question 2
gfx.show_image(gfx.overlay(gfx.fill_triangle(-1,-1, -1,1, 1,1), gfx.fill_triangle(1,1, 1,-1, -1,-1)))

#Question 3 Image 2
gfx.show_image(gfx.draw_line(-1,0,1,0))

#Question 3 Image 3
gfx.show_image(gfx.fill_triangle(-1,-1, -1,1, 1,1))

#Question 3 Image 4
gfx.show_image(gfx.overlay(gfx.fill_triangle(-1, 0, 0,0,-1,-1), gfx.fill_triangle(-1,1, 0,0,-1,0)))

#Question 4 Image 5 
gfx.show_image(gfx.overlay(gfx.fill_triangle(1, 0, 0,0,1,-1), gfx.fill_triangle(1,1, 0,0,1,0)))

#Question 4 Image 6
gfx.show_image(gfx.draw_ellipse(-1,-1,1,1))

#Question 4 Image 7
gfx.show_image(gfx.fill_ellipse(-1,-1,1,1))

#Question 4 Image 8
gfx.show_image(gfx.overlay(gfx.fill_triangle(-1, 0, 0,0,-1,-1), gfx.fill_triangle(-1,1, 0,0,-1,0),gfx.fill_triangle(1, 0, 0,0,1,-1), gfx.fill_triangle(1,1, 0,0,1,0)))

#Question4 Image 9
gfx.show_image(gfx.overlay(gfx.fill_ellipse(-1.8,1,0,-1),gfx.fill_ellipse(0,1,1.8,-1)))



