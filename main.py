from display import *
from draw import *
from parser import *
from matrix import *
import math

screen = new_screen()
color = [ 135, 206, 250 ]
edges = []
polygons = []
transform = new_matrix()

parse_file( 'dw_script', edges, polygons, transform, screen, color )
