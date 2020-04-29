class Shape(object):

   def __init__(self, l):
      self.l = l

   def sides(self):
      nl = []
      i = 0
      while i < len(self.l) - 1:
         nl.append(self.l[i].distance(self.l[i + 1]))
         i += 1
      nl.append(self.l[0].distance(self.l[-1]))
      return nl

   def perimeter(self):
      return sum(self.sides())


class Point(Shape):

   def __init__(self, x, y):
      self.x = x
      self.y = y

   def distance(self, other):
      d = (((self.x - other.x) ** 2) + (self.y - other.y) ** 2) ** (1 / 2)
      return d


class Triangle(Shape):

   def area(self):
      side = self.sides()
      s = sum(side) / 2
      a, b, c = side[0], side[1], side[2]
      a1 = ((s * (s - a) * (s - b) * (s - c)) ** (1 / 2))
      return a1

class Square(Shape):

   def area(self):
      return self.sides()[0] ** 2
