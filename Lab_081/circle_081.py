class Point(object):

   def __init__(self, x=0, y=0):
      self.xco = x
      self.yco = y

   def midpoint(self, other):
      midx = ((self.xco + other.xco) / 2)
      midy = ((self.yco + other.yco) / 2)
      return Point(midx, midy)

   def __str__(self):
      return '{:.1f}, {:.1f}'.format(self.xco, self.yco)

class Circle(object):

   def __init__(self, centre, radius=0):
      self.radius = radius
      self.centre = centre

   def __add__(self, other):
      np = Point.midpoint(self.centre, other.centre)
      new_radius = self.radius + other.radius
      return 'Centre: ({:.1f}, {:.1f})'.format(np.xco, np.yco) + "\n" + 'Radius: {:d}'.format(new_radius)

   def __str__(self):
      return 'Centre: ({:.1f}, {:.1f})'.format(np.xco, np.yco) + "\n" + 'Radius: {:d}'.format(new_radius)
