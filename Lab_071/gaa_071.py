class Score(object):

   def __init__(self, goals=0, points=0):
      self.g = goals * 3
      self.p = points
      self.total = self.g + self.p

   def greater_than(self, score2):
      if self.total > score2.total:
         return True
      else:
         return False

   def less_than(self, score2):
      if self.total < score2.total:
         return True
      else:
         return False

   def equal_to(self, score2):
      if self.total == score2.total:
         return True
      else:
         return False
