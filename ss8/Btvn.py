import pygame

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def distant(self,Point):
        d = ((self.y - Point.y) ** 2 + (Point.x - self.x) ** 2) ** 0.5
        print("Khoang cach giua hai diem la:", d)
        print()

    def halfway(self,Point):
        mid_x = max(self.x,Point.x) - (abs(self.x - Point.x)) / 2
        mid_y = max(self.y,Point.y) - (abs(self.y - Point.y)) / 2
        print("Toa do cua trung diem la: ({0},{1})".format(mid_x,mid_y))
        print()

    def reflect_x(self):
        ref_x = self.x
        ref_y = 0 - self.y
        print("Toa do cua diem doi xung qua truc Ox la: ({0},{1})".format(ref_x, ref_y))
        print()

    def reflect_y(self):
        ref_x = 0 - self.x
        ref_y = self.y
        print("Toa do cua diem doi xung qua truc Oy la: ({0},{1})".format(ref_x, ref_y))
        print()

    def reflect_origin(self):
        ref_x = 0 - self.x
        ref_y = 0 - self.y
        print("Toa do cua diem doi xung qua goc O la: ({0},{1})".format(ref_x, ref_y))
        print()

    def get_line_to(self, Point):
        a = int((self.y - Point.y) / (self.x -Point.x))
        b = int(self.y - a * self.x)
        print("Phuong trinh duong thang di qua hai diem la: y = {0} * x + {1}".format(a,b))
        print()




point_a = Point(2,1)
point_b = Point(10,9)

point_a.reflect_x()
point_a.reflect_y()
point_a.reflect_origin()

point_b.reflect_x()
point_b.reflect_y()
point_b.reflect_origin()

point_a.distant(point_b)
point_b.halfway(point_a)

point_a.get_line_to(point_b)

class Rectangle:
    def __init__(self, x,y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def area(self):
        s = self.width * self.height
        print("Dien tich hinh chu nhat bang:", s)
    def perimeter(self):
        p = (self.height + self.width) * 2
        print ("Chu vi hinh chu nhat bang:",p)
    def flip(self):
        (self.height, self.width) = (self.width,self.height)
        print("Hinh chu nhat bay gio co chieu dai = {0}, chieu rong = {1}".format(self.width, self.height))

    def contain(self, Point):
        # (x,y) = self.position
        if (self.x - self.width < Point.x < self.x and self.y - self.height < Point.y < self.y):
            print("True")
        else:
            print ("False")


hcn = Rectangle(5, 7, 10, 10)
hcn.area()
hcn.perimeter()
hcn.flip()
hcn.contain(point_a)