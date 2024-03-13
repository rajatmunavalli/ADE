import matplotlib.pyplot as plt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Polygon:
    def __init__(self, points):
        self.points = points
    
    def area(self):
        n = len(self.points)
        area = 0.0
        for i in range(n):
            j = (i + 1) % n
            area += self.points[i].x * self.points[j].y
            area -= self.points[j].x * self.points[i].y
        area = abs(area) / 2.0
        return area
    
    def perimeter(self):
        perimeter = 0.0
        n = len(self.points)
        for i in range(n):
            j = (i + 1) % n
            dx = self.points[j].x - self.points[i].x
            dy = self.points[j].y - self.points[i].y
            perimeter += (dx ** 2 + dy ** 2) ** 0.5
        return perimeter
    
    def contains_point(self, point):
        n = len(self.points)
        inside = False
        p1x, p1y = self.points[0].x, self.points[0].y
        for i in range(n + 1):
            p2x, p2y = self.points[i % n].x, self.points[i % n].y
            if point.y > min(p1y, p2y):
                if point.y <= max(p1y, p2y):
                    if point.x <= max(p1x, p2x):
                        if p1y != p2y:
                            xinters = (point.y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                        if p1x == p2x or point.x <= xinters:
                            inside = not inside
            p1x, p1y = p2x, p2y
        return inside

points = [Point(0, 0), Point(4, 0), Point(4, 3), Point(1, 2)]

x_coords = [point.x for point in points]
y_coords = [point.y for point in points]

polygon = Polygon(points)

polygon_area = polygon.area()
polygon_perimeter = polygon.perimeter()

test_point1 = Point(2, 1)
test_point2 = Point(5, 2)
test_point3 = Point(3, 3)

plt.figure(figsize=(8, 8))

plt.plot(x_coords + [points[0].x], y_coords + [points[0].y], 'b-', label='Polygon')
plt.scatter(x_coords, y_coords, color='red', label='Vertices')

test_points = [test_point1, test_point2, test_point3]
for test_point in test_points:
    plt.scatter(test_point.x, test_point.y, color='green', label='Test Point')

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Visualization of Polygon')
plt.legend()

plt.grid(True)
plt.axis('equal')
plt.show()

print("Area of the polygon:", polygon_area)
print("Perimeter of the polygon:", polygon_perimeter)
print("Is point", test_point1.x, ",", test_point1.y, "inside the polygon?", polygon.contains_point(test_point1))
print("Is point", test_point2.x, ",", test_point2.y, "inside the polygon?", polygon.contains_point(test_point2))
print("Is point", test_point3.x, ",", test_point3.y, "inside the polygon?", polygon.contains_point(test_point3))
