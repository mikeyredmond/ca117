class Point(object):

   def __init__(self, x=0, y=0):
      self.xco = x
      self.yco = y

   def distance(self, p2):
      d = (((self.xco - p2.xco) ** 2) + (self.yco - p2.yco) ** 2) ** (1 / 2)
      return d

   def __str__(self):
      return '({:.1f}, {:.1f})'.format(self.xco, self.yco)

class Segment(object):

   def __init__(self, p1, p2):
      self.point1x = p1.xco
      self.point1y = p1.yco
      self.point2x = p2.xco
      self.point2y = p2.yco

   def midpoint(self):
      xmp = ((self.point1x + self.point2x) / 2)
      ymp = ((self.point1y + self.point2y) / 2)
      return xmp, ymp

   def length(self):
      l = (((self.point2x - self.point1x) ** 2) + (self.point2y - self.point1y) ** 2) ** (1 / 2)
      return l

class Circle(object):

   def __init__(self, centre=0, radius=0):
      self.r = radius
      self.cx = centre.xco
      self.cy = centre.yco

   def overlaps(self, circle):
      return(((self.cx - circle.cx) ** 2) + ((self.cy - circle.cy) ** 2)) ** (1 / 2) < self.r + circle.r
