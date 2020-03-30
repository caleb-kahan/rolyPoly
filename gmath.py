import math
from display import *



#vector functions
#normalize vetor, should modify the parameter
def normalize(vector):
    magnitude = magnitude(vector)
    for i in range(len(vector)):
        vector[i]/=magnitude

def magnitude(vector):
    sum = 0
    for i in range(len(a)):
        sum+=(vector[i]*vector[i])
    return math.sqrt(sum)
#Return the dot porduct of a . b
def dot_product(a, b):
    sum = 0
    for i in range(len(a)):
        sum+=(a[i]*b[i])
    return sum

def cross_product(a,b):
    product = [a[1]*b[2] - a[2]*b[1],
         a[2]*b[0] - a[0]*b[2],
         a[0]*b[1] - a[1]*b[0]]
    return product
def subtract(a,b):
    return [b[0]-a[0],
            b[1]-a[1],
            b[2]-a[2]]
#Calculate the surface normal for the triangle whose first
#point is located at index i in polygons
def calculate_normal(polygons, i):
    a = subtract(polygons[i],polygons[i+1])
    b = subtract(polygons[i],polygons[i+2])
    n = cross_product(a,b)
    return n
