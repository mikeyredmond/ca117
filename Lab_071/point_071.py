class Point(object):

   def __init__(self, x=0, y=0):
      self.xco = x
      self.yco = y

   def reflect(self):
      self.xco = -(self.xco)
      self.yco = -(self.yco)

   def distance(self, p2):
      d = (((self.xco - p2.xco) ** 2) + (self.yco - p2.yco) ** 2) ** (1 / 2)
      return d
