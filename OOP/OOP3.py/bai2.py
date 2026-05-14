import math
import copy
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
class Rectangle:
    def __init__(self, corner, width, height):
        self.corner = corner
        self.width = width
        self.height = height
class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
def distance_between_points(p1, p2):
    return math.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)
def point_in_circle(circle, point):
    return distance_between_points(circle.center, point) < circle.radius
def rect_in_circle(circle, rect):
    corners = [
        rect.corner,
        Point(rect.corner.x + rect.width, rect.corner.y),
        Point(rect.corner.x, rect.corner.y + rect.height),
        Point(rect.corner.x + rect.width, rect.corner.y + rect.height)
    ]
    return all(point_in_circle(circle, corner) for corner in corners)
def rect_circle_overlap(circle, rect):
    closest_x = max(rect.corner.x, min(circle.center.x, rect.corner.x + rect.width))
    closest_y = max(rect.corner.y, min(circle.center.y, rect.corner.y + rect.height))
    closest_point = Point(closest_x, closest_y)
    return distance_between_points(circle.center, closest_point) < circle.radius
if __name__ == '__main__':
    center_point = Point(150, 100)
    my_circle = Circle(center_point, 75)

    print(f"Circle created at center ({my_circle.center.x}, {my_circle.center.y}) with radius {my_circle.radius}")
    test_point_inside = Point(160, 110)
    test_point_outside = Point(300, 300)
    print(f"Point (160, 110) in circle? {point_in_circle(my_circle, test_point_inside)}")
    print(f"Point (300, 300) in circle? {point_in_circle(my_circle, test_point_outside)}")
    rect_inside = Rectangle(Point(140, 90), 10, 10)
    print(f"Rectangle strictly inside? {rect_in_circle(my_circle, rect_inside)}")
    rect_overlap = Rectangle(Point(100, 50), 200, 200)
    print(f"Rectangle overlaps circle? {rect_circle_overlap(my_circle, rect_overlap)}")
    

