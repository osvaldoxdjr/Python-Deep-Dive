from math import pi

class Circle:
    def __init__(self, radius):
        self._radius = None
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        if radius <= 0:
            raise ValueError('Radius must be positive')
        self._radius = radius

    def area(self):
        return pi*self.radius**2

    def perimeter(self):
        return 2*pi*self.radius

    def __str__(self):
        return 'Circle - Radius {:f}'.format(self.radius)

    def __repr__(self):
        return 'Circle - Radius {:f}'.format(self.radius)

circle = Circle(1.0)
print(format(circle), # Object Information
      'Area = {:f}'.format(circle.area()), # Area of the circle
      'Perimeter = {:f}'.format(circle.perimeter()), # Perimeter of the circle
      sep ='\n')