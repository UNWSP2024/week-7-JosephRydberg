# Program #4: Coordinates
# Write a distance function that will take two 3-dimensional coordinates (as input) 
# and will return (as output) the distance between those points in space.  
# The 3-dimensional coordinates must be stored as tuples.
import math


# Now write a mainline that has the user enter the two tuples.
# The mainline calls the distance function and stores the distance in a variable.  The mainline then displays the distance.  
# Also include exception handling to deal with faulty input.
# The distance between two points (x1,y1,z1) and (x2, y2, z2) is 
#    given by:   sqrt ((x2-x1)^2 + (y2 - y1)^2 + (z1 - z2)^2)

def point_distance():
    point1 = (int(input("X1 cord")), int(input("Y1 cord")), int(input("Z1 cord")))
    point2 = (int(input("X2 cord")), int(input("Y2 cord")), int(input("Z2 cord")))

    distance = math.sqrt((point2[0] - point1[0])^2 + (point2[1] - point1[1])^2 + (point1[2] - point2[2])^2)
    print(distance)

point_distance()