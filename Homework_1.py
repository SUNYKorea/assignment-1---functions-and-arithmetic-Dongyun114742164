# Name: Dongyun Lee
# SBUID: 114742164

# Remove the ellipses (...) when writing your solutions.

# ---------------------------- Exercise I ---------------------------------------
# ----------------- Convert Fahrenheit to Celsius -------------------------------
# TODO: Complete the implementation of fahrenheit2celsius () and what_to_wear(). 

def fahrenheit2celsius(fahrenheit): 
   return 5/9*(fahrenheit-32)

def what_to_wear(celsius):
   if (celsius < -10):
       print("You have to wear Puffy jacket")
   elif (-10 <= celsius < 0):
       print("You have to wear Scarf")
   elif (0 <= celsius < 10):
       print("You have to wear")
   elif (10 <= celsius < 20):
       print("You have to wear Light jacket")
   else:
       print("You have to wear T-shirt")
    

# ---------------------------- Exercise II --------------------------------------
# ----------------- Area and perimeter of a triangle  ---------------------------
# TODO: Fill the functions shoelace_triangle_area, euclidean_distance and
# compute_triangle_perimeter from scratch  

def shoelace_triangle_area(x1, y1, x2, y2, x3, y3):
    # Computing the area of the triangle.
    # p1 = tuple that shows (x,y) of the first point
    # p2 = tuple that shows (x,y) of the second point
    # p3 = tuple that shows (x,y) of the third point
    # Return the area of the triangle.

    p1 = x1, y1
    p2 = x2, y2
    p3 = x3, y3
    return abs(1/2*((x1*y2 + x2*y3 + x3*y1)-(x1*y3 + x2*y1 + x3*y2)))

def euclidean_distance(x1, y1, x2, y2):
    # Computing the euclidean distance between p1 and p2.
    # Return the euclidean distance between p1 and p2.

    import math
    
    p1 = x1, y1 
    p2 = x2, y2
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)
 
def compute_triangle_perimeter(x1, y1, x2, y2, x3, y3):
    # Computing the perimeter of the triangle with 3 vertices.
    # Vertices = list of 3 tuples each shows (x,y) of a verice.
    # Return the perimeter of the triangle.

    p1 = x1, y1
    p2 = x2, y2
    p3 = x3, y3

    s1 = euclidean_distance(x1, y1, x2, y2)
    s2 = euclidean_distance(x2, y2, x3, y3)
    s3 = euclidean_distance(x1, y1, x3, y3)
    return s1 + s2 + s3
 

# ---------------------------- Exercise III -------------------------------------
# ----------------- Compute the area of a regular polygon -----------------------
# TODO: Fill the functions deg2rad, apothem  and polygon_area 

import math

def deg2rad(deg):
    return deg*(math.pi/180)
    
def apothem(number_sides, length_side):
    n = number_sides
    s = length_side
    return length_side/(2*math.tan(math.pi/number_sides))

def polygon_area(number_sides, length_side):
    n = number_sides
    s = length_side
    return (number_sides*(length_side**2))/(4*math.tan(math.pi/number_sides))


# ---------------------------- Test -------------------------------------
# The following lines are for testing purposes, and will not be part of
# your grade. You may freely modify the following codes.

# Exercise 1 test
fahrenheit = 40
what_to_wear(fahrenheit2celsius(fahrenheit))

# Exercise 2 test
x1, x2, x3, y1, y2, y3 = -4, -5, 3, -4, 5, -3 # declaration of the vertices of the triangle
area = shoelace_triangle_area(x1, y1, x2, y2, x3, y3)
perimeter = compute_triangle_perimeter(x1, y1, x2, y2, x3, y3)
print("The area of the triangle is : " + str(area) + " , its perimeter is : " + str(perimeter) )

# Exercise 3 test
number_sides = 5
length_side = 4
print ("The area of the polygon is : " + str(polygon_area(number_sides, length_side)))