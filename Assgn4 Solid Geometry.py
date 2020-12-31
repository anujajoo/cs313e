#!/bin/python3

import sys, math
 
class Point (object):
  # constructor with default values
  def __init__ (self, x = 0, y = 0, z = 0):
    self.x = x
    self.y = y
    self.z = z
 
  # create a string representation of a Point
  # returns a string of the form (x, y, z)
  def __str__ (self):
    return '(' + str(self.x)+ ', ' + str(self.y) + ', ' + str(self.z) + ')'
 
  # get distance to another Point object
  # other is a Point object
  # returns the distance as a floating point number
  def distance (self, other):
    # Using algebra we can get the distance between points self and other
    dist = math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2 + (self.z - other.z)**2)
    return dist
 
  # test for equality between two points
  # other is a Point object
  # returns a Boolean
  def __eq__(self, other):
    tol = 1.0e-6
    #line not indented bc long but still works
    check = (abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol) and ((self.z - other.z) < tol) 
    return check


class Sphere (object):
  # constructor with default values
  def __init__ (self, x = 0, y = 0, z = 0, radius = 1):
    self.x = x
    self.y = y
    self.z = z
    self.center = Point(self.x, self.y, self.z)
    self.radius = radius
    #create set of point coord values at max x,y,z values on circle along parallel to axes
    self.xmin = self.x - self.radius
    self.xmax = self.x + self.radius
    self.ymin = self.y - self.radius
    self.ymax = self.y + self.radius
    self.zmin = self.z - self.radius
    self.zmax = self.z + self.radius

  # returns string representation of a Sphere of the form:
  # Center: (x, y, z), Radius: value
  def __str__ (self):
    return 'Center: (' + str(self.x)+ ', ' + str(self.y) + ', ' + str(self.z) + '), Radius: ' + str(self.radius)

  # compute surface area of Sphere
  # returns a floating point number
  def area (self):
    self.surfacearea = float(4 * (math.pi) * self.radius**2)
    return self.surfacearea
  # compute volume of a Sphere
  # returns a floating point number
  def volume (self):
    self.volume = (4/3) * math.pi * (self.radius**3)
    return self.volume
  # determines if a Point is strictly inside the Sphere
  # p is Point object
  # returns a Boolean
  def is_inside_point (self, p):
    return self.center.distance(p) < self.radius

  # determine if another Sphere is strictly inside this Sphere
  # other is a Sphere object
  # returns a Boolean
  def is_inside_sphere (self, other):
    #completely inside if distance bw centers + other sphere radius less than og radius
    return (self.center.distance(other.center) + other.radius) < self.radius

  def is_outside_sphere (self, other):
    #completely outside if distance between centers larger than sum of radii
    return self.center.distance(other.center) > (self.radius + other.radius)

  # determine if a Cube is strictly inside this Sphere
  # determine if the eight corners of the Cube are strictly 
  # inside the Sphere -- meaning dist of each point < radius strictly
  # a_cube is a Cube object
  # returns a Boolean
  def is_inside_cube (self, a_cube):
    toggle = True
    for vertex in a_cube.vertices:
        if self.center.distance(vertex) < self.radius:
            toggle = True
        else:
            toggle = False
            break
    return toggle

  # determine if a Cube is strictly outside this Sphere
  def is_outside_cube(self, a_cube):
    toggle = False
    if (self.xmax < a_cube.xmin) or (self.xmin > a_cube.xmax):
        toggle = True
    elif (self.ymax < a_cube.ymin) or (self.ymin > a_cube.ymax):
        toggle = True
    elif (self.zmax < a_cube.zmin) or (self.zmin > a_cube.zmax):
        toggle = True
    return toggle

  # determine if a Cylinder is strictly inside this Sphere
  # a_cyl is a Cylinder object
  # returns a Boolean
  def is_inside_cyl (self, a_cyl):
    self.xranges = ((self.xmin < a_cyl.xmin < self.xmax) and (a_cyl.xmax < self.xmax))
    self.yranges = ((self.ymin < a_cyl.ymin < self.ymax) and (a_cyl.ymax < self.ymax))
    self.zranges = ((self.zmin < a_cyl.zmin < self.zmax) and (a_cyl.zmax < self.zmax))
    if  self.xranges == True and self.yranges == True and self.zranges == True:
        toggle = True
        if (self.center.distance(a_cyl.top_up_center) < self.radius) and (self.center.distance(a_cyl.bottom_down_center) < self.radius):
            toggle = True
        else:
            toggle = False
    else:
        toggle = False
    return toggle

  
  # determine if another Sphere intersects this Sphere
  # other is a Sphere object
  # two spheres intersect if they are not strictly inside
  # or not strictly outside each other
  # returns a Boolean
  def does_intersect_sphere (self, other):
    toggle = False
    if self.is_inside_sphere(other) == False and self.is_outside_sphere(other) == False:
        toggle = True
    return toggle

  # determine if a Cube intersects this Sphere
  # the Cube and Sphere intersect if they are not
  # strictly inside or not strictly outside the other
  # a_cube is a Cube object
  # returns a Boolean
  def does_intersect_cube (self, a_cube):
    if self.is_inside_cube(a_cube) == False and self.is_outside_cube(a_cube) == False:
        return True
    else:
        return False
  
  # return the largest Cube object that is circumscribed
  # by this Sphere
  # all eight corners of the Cube are on the Sphere
  # returns a Cube object
  def circumscribe_cube (self):
    #center has to be shared, and diagonal = radius. so reverse solve.
    self.side = (2/math.sqrt(3))*self.radius
    return Cube(self.x, self.y, self.z, self.side)


class Cube (object):
  # Cube is defined by its center (which is a Point object)
  # and side. The faces of the Cube are parallel to x-y, y-z,
  # and x-z planes.
  def __init__ (self, x = 0, y = 0, z = 0, side = 1):
    self.x = x
    self.y = y
    self.z = z
    self.side = side
    self.center = Point(self.x, self.y, self.z)
    
    #create ranges for xyz
    self.length = side/2
    self.xmin = self.x - self.length
    self.xmax = self.x + self.length
    self.ymin = self.y - self.length
    self.ymax = self.y + self.length
    self.zmin = self.z - self.length
    self.zmax = self.z + self.length

    #create vertices
    #tur = top upper right, bbl, bottom bottom left.... etc
    #opposite diagonals: tur/bbl, tul/bbr, tbl/bur, tbr/bul
    self.tur = Point(self.xmax, self.ymax, self.zmax)
    self.tul = Point(self.xmin, self.ymax, self.zmax)
    self.tbr = Point(self.xmax, self.ymax, self.zmin)
    self.tbl = Point(self.xmin, self.ymax, self.zmin)
    self.bur = Point(self.xmax, self.ymin, self.zmax)
    self.bul = Point(self.xmin, self.ymin, self.zmax)
    self.bbr = Point(self.xmax, self.ymin, self.zmin)
    self.bbl = Point(self.xmin, self.ymin, self.zmin)
    #create list of vertices as point objects to loop through in later operations
    self.vertices = [self.tur, self.tul, self.tbr, self.tbl, self.bur, self.bul, self.bbr, self.bbl]
    
  # string representation of a Cube of the form: 
  # Center: (x, y, z), Side: value
  def __str__ (self):
    return 'Center: (' + str(self.x)+ ', ' + str(self.y) + ', ' + str(self.z) + '), Side: ' + str(self.side)
  # compute the total surface area of Cube (all 6 sides)
  # returns a floating point number
  def area (self):
    SA  = float((self.side**2) * 6)
    return SA
  # compute volume of a Cube
  # returns a floating point number
  def volume (self):
    self.V = float(self.side **3)
    return self.V
  
  # determines if a Point is strictly inside this Cube
  # p is a point object
  # returns a Boolean
  def is_inside_point (self, p):
    return (self.xmin <= p.x <= self.xmax) and (self.ymin <= p.y <= self.ymax) and (self.zmin <= p.z <= self.zmax)

  # determine if a Sphere is strictly inside this Cube 
  # a_sphere is a Sphere object
  # returns a Boolean
  def is_inside_sphere (self, a_sphere):
    return self.center.distance(a_sphere.center) + a_sphere.radius < self.length

  # determine if another Cube is strictly inside this Cube
  # other is a Cube object
  # returns a Boolean
  def is_inside_cube (self, other):
    check_x = self.xmin < other.xmin and self.xmax > other.xmax
    check_y = self.ymin < other.ymin and self.ymax > other.ymax
    check_z = self.zmin < other.zmin and self.zmax > other.zmax
    return check_x and check_y and check_z

  # determine strictly outside (mutual) from persp of other cube
  def is_outside_cube (self, other):
    check_x = self.xmax < other.xmin or self.xmin > other.xmax
    check_y = self.ymax < other.ymin or self.ymin > other.ymax
    check_z = self.zmax < other.zmin or self.zmin > other.zmax
    return check_x == True or check_y == True or check_z == True
    
  # determine if a Cylinder is strictly inside this Cube
  # a_cyl is a Cylinder object
  # returns a Boolean
  def is_inside_cylinder (self, a_cyl):
    pass
  
  # determine if another Cube intersects this Cube
  # two Cube objects intersect if they are not strictly
  # inside and not strictly outside each other
  # other is a Cube object
  # returns a Boolean
  def does_intersect_cube (self, other):
    return self.is_outside_cube(other) == False and self.is_inside_cube(other) == False

  # determine the volume of intersection if this Cube 
  # intersects with another Cube
  # other is a Cube object
  # returns a floating point number
  def intersection_volume (self, other):
    self.side_x_min = 0
    self.side_x_max = 0
    self.side_y_min = 0
    self.side_y_max = 0
    self.side_z_min = 0
    self.side_z_max = 0
    if self.does_intersect_cube(other) == True:
        #finds intersection x side length parameters
        if self.xmin > other.xmin:
            self.side_x_min = self.xmin
        elif other.xmin > self.xmin:
            self.side_x_min = other.xmin
        if self.xmax < other.xmax:
            self.side_x_max = self.xmax
        elif other.xmax < self.xmax:
            self.side_x_max = other.xmax
        #finds intersection y side length parameters
        if self.ymin > other.ymin:
            self.side_y_min = self.ymin
        elif other.ymin > self.ymin:
            self.side_y_min = other.ymin
        if self.ymax < other.ymax:
            self.side_y_max = self.ymax
        elif other.ymax < self.ymax:
            self.side_y_max = other.ymax
        #finds intersectionz side length parameters
        if self.zmin > other.zmin:
            self.side_z_min = self.zmin
        elif other.zmin > self.zmin:
            self.side_z_min = other.zmin
        if self.zmax < other.zmax:
            self.side_z_max = self.zmax
        elif other.zmax < self.zmax:
            self.side_z_max = other.zmax
        #find side lengths of intersection volume and then find volume
        self.side_x = self.side_x_max - self.side_x_min
        self.side_y = self.side_y_max - self.side_y_min
        self.side_z = self.side_z_max - self.side_z_min

        self.volume = float(self.side_x * self.side_y * self.side_z)
        return self.volume

  # return the largest Sphere object that is inscribed
  # by this Cube
  # Sphere object is inside the Cube and the faces of the
  # Cube are tangential planes of the Sphere
  # returns a Sphere object
  def inscribe_sphere (self):
    return Sphere(self.x, self.y, self.z, self.length)


class Cylinder (object):
  # Cylinder is defined by its center (which is a Point object),
  # radius and height. The main axis of the Cylinder is along the
  # z-axis and height is measured along this axis
  def __init__ (self, x = 0, y = 0, z = 0, radius = 1, height = 1):
    self.x = x
    self.y = y
    self.z = z
    self.center = Point(self.x, self.y, self.z)
    self.radius = radius
    self.height = height
    #set some useful values
    self.length = height/2
    self.topcenter = Point(self.x, self.y, self.z + self.length)
    self.bottomcenter = Point(self.x, self.y, self.z - self.length)

    # self.top_up_center = Point(self.x, self.y + length, self.topcenter.z)
    # self.bottom_down_center = Point(self.x, self.y - length, self.bottomcenter.z)
    # self.top_down_center = Point(self.x, self.y + length, self.topcenter.z)
    # self.bottom_up_center = Point(self.x, self.y + length, self.bottomcenter.z)
    # self.top_right_center = 

    self.xmin = self.x - self.radius
    self.xmax = self.x + self.radius
    self.ymin = self.y - self.radius
    self.ymax = self.y + self.radius
    self.zmin = self.bottomcenter.z
    self.zmax = self.topcenter.z
    # returns a string representation of a Cylinder of the form: 
  # Center: (x, y, z), Radius: value, Height: value
  def __str__ (self):
    return 'Center: (' + str(self.x)+ ', ' + str(self.y) + ', ' + str(self.z) + '), Radius: ' + str(self.radius) + ', Height: ' + str(self.height)

  # compute surface area of Cylinder / returns a floating point number
  def area (self):
    self.area = (2 * (math.pi) * (self.radius)) * (self.height + self.radius)
    return float(self.area)
  # compute volume of a Cylinder / returns a floating point number
  def volume (self):
    self.volume = (math.pi) * (math.pow(self.radius, 2)) * (self.height)
    return float(self.volume)

  # determine if a Point is strictly inside this Cylinder
  # p is a Point object
  # returns a Boolean
  def is_inside_point (self, p):
    if self.xmin < p.x <self.xmax and self.ymin < p.y < self.ymax and self.zmin < p.z < self.zmax:
        self.compare_center = Point(self.x, self.y, p.z)
        return self.compare_center.distance(p) < radius
    else:
        return False
  # determine if a Sphere is strictly inside this Cylinder
  # a_sphere is a Sphere object
  # returns a Boolean
  def is_inside_sphere (self, a_sphere):
    self.xranges = ((self.xmin < a_sphere.xmin < self.xmax) and (a_sphere.xmax < self.xmax))
    self.yranges = ((self.ymin < a_sphere.ymin < self.ymax) and (a_sphere.ymax < self.ymax))
    self.zranges = ((self.zmin < a_sphere.zmin < self.zmax) and (a_sphere.zmax < self.zmax))
    if  self.xranges == True and self.yranges == True and self.zranges == True:
        self.compare_center = Point(self.x, self.y, a_sphere.z)
        if self.compare_center.distance(a_sphere.center) + a_sphere.radius < self.radius:
            return True
        else: return False
    else:
        return False

  # determine if a Cube is strictly inside this Cylinder
  # determine if all eight corners of the Cube are inside
  # the Cylinder
  # a_cube is a Cube object
  # returns a Boolean
  def is_inside_cube (self, a_cube):
    self.xranges = ((self.xmin < a_cube.xmin < self.xmax) and (a_cube.xmax < self.xmax))
    self.yranges = ((self.ymin < a_cube.ymin < self.ymax) and (a_cube.ymax < self.ymax))
    self.zranges = ((self.zmin < a_cube.zmin < self.zmax) and (a_cube.zmax < self.zmax))
    if  self.xranges == True and self.yranges == True and self.zranges == True:
        toggle = True
        for vertex in a_cube.vertices:
            self.compare_center = Point(self.x, self.y, vertex.z)
            if self.compare_center.distance(vertex) < self.radius:
                toggle = True
            else:
                toggle = False
                break
    else:
        toggle = False
    return toggle   

  # determine if another Cylinder is strictly inside this Cylinder
  # other is Cylinder object
  # returns a Boolean
  def is_inside_cylinder (self, other):
    self.xranges = ((self.xmin < other.xmin < self.xmax) and (other.xmax < self.xmax))
    self.yranges = ((self.ymin < other.ymin < self.ymax) and (other.ymax < self.ymax))
    self.zranges = ((self.zmin < other.zmin < self.zmax) and (other.zmax < self.zmax))
    if  self.xranges == True and self.yranges == True and self.zranges == True:
        toggle = True
        self.compare_center = Point(self.x, self.y, other.z)
        if self.compare_center.distance(other.center) + other.radius < self.radius:
            return True
        else: return False
    else:
        return False

  def is_outside_cylinder (self, other):
    self.xranges = (other.xmax < self.xmin) or (other.xmin > self.xmax)
    self.yranges = (other.ymax < self.ymin) or (other.ymin > self.ymax)
    self.zranges = (other.zmax < self.zmin) or (other.zmin > self.zmax)
    if  self.xranges == True or self.yranges == True or self.zranges == True:
        toggle = True
    else:
        if self.zmin< other.bottomcenter.z < self.zmax:
            compare_center = Point(self.x, self.y, other.bottomcenter.z)
            if compare_center.distance(other.bottomcenter) > self.radius + other.radius:
                toggle = True
            else:
                toggle = False
        elif self.zmin < other.topcenter.z < self.zmax:
            compare_center = Point(self.x, self.y, other.topcenter.z)
            if compare_center.distance(other.topcenter) > self.radius + other.radius:
                toggle = True
            else:
                toggle = False
    return toggle

  # determine if another Cylinder intersects this Cylinder
  # two Cylinder object intersect if they are not strictly
  # inside and not strictly outside each other
  # other is a Cylinder object
  # returns a Boolean
  def does_intersect_cylinder (self, other):
    if self.is_outside_cylinder(other) == False and self.is_inside_cylinder(other) == False:
        return True
    else:
        return False

def read_input():


    tuples_list = []
    for line in sys.stdin.readlines():
        line_tuple = ()
        line = line.strip()
        line_nums = line.split(' ')
        for i in line_nums:
            line_tuple = line_tuple + (float(i),)
        tuples_list.append(line_tuple)

    #in tuples_list, from [0] to [7] follows the order from input
    return tuples_list
 
def main():
  # read data from standard input
    data = read_input()

  # read the coordinates of the first Point p
    coords_P = data[0]
    # create a Point object 
    P = Point(coords_P[0], coords_P[1], coords_P[2])
    
    # create point object for origin
    Origin = Point()
  # read the coordinates of the second Point q
    coords_Q = data[1]
    # create a Point object 
    Q = Point(coords_Q[0], coords_Q[1], coords_Q[2])

  # read the coordinates of the center and radius of sphereA
    coords_sphereA = data[2]
    # create a Sphere object 
    sphereA = Sphere(coords_sphereA[0], coords_sphereA[1], coords_sphereA[2], coords_sphereA[3])
   
  # read the coordinates of the center and radius of sphereB
    coords_sphereB = data[3]
    # create a Sphere object
    sphereB = Sphere(coords_sphereB[0], coords_sphereB[1], coords_sphereB[2], coords_sphereB[3])
      
  # read the coordinates of the center and side of cubeA
    coords_cubeA = data[4]
    cubeA = Cube(coords_cubeA[0], coords_cubeA[1], coords_cubeA[2], coords_cubeA[3])
    # create a Cube object 

  # read the coordinates of the center and side of cubeB
    coords_cubeB = data[5]
    # create a Cube object 
    cubeB = Cube(coords_cubeB[0], coords_cubeB[1], coords_cubeB[2], coords_cubeB[3])
 
  # read the coordinates of the center, radius and height of cylA
    coords_cylA = data[6]
    # create a Cylinder object 
    cylA = Cylinder(coords_cylA[0], coords_cylA[1], coords_cylA[2], coords_cylA[3], coords_cylA[4])

  # read the coordinates of the center, radius and height of cylB
    coords_cylB = data[7]
    cylB = Cylinder(coords_cylB[0], coords_cylB[1], coords_cylB[2], coords_cylB[3], coords_cylB[4])

#reading data and creating objects done. now if/else for print statements

  # print if the distance of p from the origin is greater 
  # than the distance of q from the origin
    if P.distance(Origin) > Q.distance(Origin):
        print("Distance of Point p from the origin is greater than ", end = '')
        print("the distance of Point q from the origin\n")
    else:
        print("Distance of Point p from the origin is not greater than ", end = '')
        print("the distance of Point q from the origin\n")


  # print if Point p is inside sphereA
    if sphereA.is_inside_point(P) == True:
        print('Point p is inside sphereA')
    else:
        print('Point p is not inside sphereA')

  # print if sphereB is inside sphereA
    if sphereA.is_inside_sphere(sphereB) == True:
        print('sphereB is inside sphereA')
    else:
        print('sphereB is not inside sphereA')
  # print if cubeA is inside sphereA
    if sphereA.is_inside_cube(cubeA) == True:
        print('cubeA is inside sphereA')
    else:
        print('cubeA is not inside sphereA')
  # print if cylA is inside sphereA
    if sphereA.is_inside_cyl(cylA) == True:
        print('cylA is inside sphereA')
    else:
        print('cylA is not inside sphereA')

  # print if sphereA intersects with sphereB
    if sphereB.does_intersect_sphere(sphereA) == True:
        print('sphereA does intersect sphereB')
    else:
        print('sphereA does not intersect sphereB')
  # print if cubeB intersects with sphereB
    if sphereB.does_intersect_cube(cubeB) == True:
        print('cubeB does intersect sphereB')
    else:
        print('cubeB does not intersect sphereB')    
  # print if the volume of the largest Cube that is circumscribed 
  # by sphereA is greater than the volume of cylA
    if sphereA.circumscribe_cube().volume() > cylA.volume():
        print("Volume of the largest Cube that is circumscribed by sphereA is ", end = '')
        print("greater than the volume of cylA\n")
    else:
        print("Volume of the largest Cube that is circumscribed by sphereA is ", end = '')
        print("not greater than the volume of cylA\n")


  # print if Point p is inside cubeA
    if cubeA.is_inside_point(P) == True:
        print('Point p is inside cubeA')
    else:
        print('Point p is not inside cubeA')
  # print if sphereA is inside cubeA
    if cubeA.is_inside_sphere(sphereA) == True:
        print('sphereA is inside cubeA')
    else:
        print('sphereA is not inside cubeA')
  # print if cubeB is inside cubeA
    if cubeA.is_inside_cube(cubeB) == True:
        print('cubeB is inside cubeA')
    else:
        print('cubeB is not inside cubeA')
  # print if cylA is inside cubeA
    if cubeA.is_inside_cylinder(cylA) == True:
        print('cylA is inside cubeA')
    else:
        print('cylA is not inside cubeA')
  # print if cubeA intersects with cubeB
    if cubeB.does_intersect_cube(cubeA) == True:
        print('cubeA does intersect cubeB')
    else:
        print('cubeA does not intersect cubeB')
  # print if the intersection volume of cubeA and cubeB
  # is greater than the volume of sphereA
    if cubeA.intersection_volume(cubeB) > sphereA.volume():
        print("Intersection volume of cubeA and cubeB is ", end = '')
        print("greater than the volume of sphereA")
    else:
        print("Intersection volume of cubeA and cubeB is ", end = '')
        print("not greater than the volume of sphereA")

  # print if the surface area of the largest Sphere object inscribed 
  # by cubeA is greater than the surface area of cylA
    if cubeA.inscribe_sphere().area() > cylA.area():
        print("Surface area of the largest Sphere object inscribed by cubeA ", end = '')
        print("is greater than the surface area of cylA\n")
    else:
        print("Surface area of the largest Sphere object inscribed by cubeA ", end = '')
        print("is not greater than the surface area of cylA\n")
        
  # print if Point p is inside cylA
    if cylA.is_inside_point(P) == True:
        print('Point p is inside cylA')
    else:
        print('Point p is not inside cylA')
  # print if sphereA is inside cylA
    if cylA.is_inside_sphere(sphereA) == True:
        print('sphereA is inside cylA')
    else:
        print('sphereA is not inside cylA')
  # print if cubeA is inside cylA
    if cylA.is_inside_cube(cubeA) == True:
        print('cubeA is inside cylA')
    else:
        print('cubeA is not inside cylA')
  # print if cylB is inside cylA
    if cylA.is_inside_cylinder(cylB) == True:
        print('cylB is inside cylA')
    else:
        print('cylB is not inside cylA')
  # print if cylB intersects with cylA
    if cylA.does_intersect_cylinder(cylB) == True:
        print('cylB does intersect cylA')
    else:
        print('cylB does not intersect cylA')

 
if __name__ == "__main__":
  main()
