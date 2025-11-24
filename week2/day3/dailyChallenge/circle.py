import math
def validate_circle(init_func):
    def wrapper(self, *args, **kwargs):
        if "radius" in kwargs:
            self.radius = float(kwargs["radius"])
        elif "diameter" in kwargs:
            self.radius = float(kwargs["diameter"]) / 2
        else:
            raise ValueError("You must provide either radius OR diameter.")
        return init_func(self)
    return wrapper


class Circle:
    @validate_circle
    def __init__(self):
        pass 

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    @property
    def area(self):
        return math.pi * (self.radius ** 2)

    def __repr__(self):
        return f"Circle(radius={self.radius})"

    def __str__(self):
        return f"A circle with radius {self.radius} and diameter {self.diameter}"

    def __add__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return Circle(radius=self.radius + other.radius)

    def __eq__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius == other.radius

    def __gt__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius > other.radius

    def __lt__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius < other.radius
c1 = Circle(radius=4)
c2 = Circle(diameter=10)
c3 = Circle(radius=7)

print(c1)  
print(c2.diameter)
print(c2.area)

c4 = c1 + c2
print("New circle after addition:", c4)

print("c1 > c2 ?", c1 > c2)
print("c2 == c3 ?", c2 == c3)

circles = [c3, c1, c2, c4]
sorted_circles = sorted(circles)
print("Sorted circles:", sorted_circles)

# #BONUS
import turtle

def draw_circles(circles, spacing=50):
    """
    Draw a list of circles using Turtle.
    
    circles: list of Circle objects (assumed sorted or unsorted)
    spacing: space between the circles on the canvas
    """
    screen = turtle.Screen()
    screen.title("Drawing Circles")
    
    t = turtle.Turtle()
    t.speed(1)  
    t.penup()
    
    start_x = -200 
    start_y = 0
    
    for circle in circles:
        t.goto(start_x + circle.radius, start_y - circle.radius) 
        t.pendown()
        t.circle(circle.radius)
        t.penup()
        
        
        start_x += circle.diameter + spacing
    
    t.hideturtle()
    screen.mainloop()

c1 = Circle(radius=30)
c2 = Circle(radius=50)
c3 = Circle(radius=20)

circles = [c1, c2, c3]

circles.sort()

draw_circles(circles)
