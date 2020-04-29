class Weight(object):

   OUNCES_PER_POUND = 16

   def __init__(self, pounds=0, ounces=0):
      self.pounds = pounds
      self.ounces = ounces
      self.weight = (pounds * 16) + ounces

   def from_ounces(ounces=0):
      pounds = ounces // 16
      ounces = ounces % 16
      return Weight(pounds, ounces)

   def __str__(self):
      return '{} pound(s) and {} ounce(s)'.format(self.pounds, self.ounces)

   def __eq__(self, other):
      return self.weight == other.weight

   def __lt__(self, other):
      return self.weight < other.weight

   def __le__(self, other):
      return self.weight <= other.weight

   def __iadd__(self, other):
      t = self + other
      self.pounds = t.pounds
      self.ounces = t.ounces
      self.weight = t.weight
      return self

   def __mul__(self, other):
      return Weight.from_ounces(self.weight * other)

   def __add__(self, other):
      nw = (self.pounds * 16) + (other.pounds * 16) + self.ounces + other.pounds
      pounds = nw // 16
      ounces = (nw % 16) - 2
      return Weight(pounds, ounces)
