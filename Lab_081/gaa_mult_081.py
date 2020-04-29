class Score(object):

   def __init__(self, goals=0, points=0):
      self.goals = goals
      self.points = points

   def totalscore(self):
      total = self.goals * 3 + self.points
      return total

   def __eq__(self, other):
      return self.totalscore() == other.totalscore()

   def __gt__(self, other):
      return self.totalscore() > other.totalscore()

   def __lt__(self, other):
      return self.totalscore() < other.totalscore()

   def __ge__(self, other):
      return self.totalscore() >= other.totalscore()

   def __le__(self, other):
      return self.totalscore() <= other.totalscore()

   def __add__(self, other):
      tg = self.goals + other.goals
      tp = self.points + other.points
      return Score(tg, tp)

   def __sub__(self, other):
      tg = self.goals - other.goals
      tp = self.points - other.points
      return Score(tg, tp)

   def __mul__(self, other):
      tg = self.goals * other
      tp = self.points * other
      return Score(tg, tp)

   def __rmul__(self, other):
      tg = other * self.goals
      tp = other * self.points
      return Score(tg, tp)

   def __imul__(self, other):
      z = other * self
      self.goals, self.points = z.goals, z.points
      return self

   def __iadd__(self, other):
      z = self + other
      self.goals, self.points = z.goals, z.points
      return self

   def __isub__(self, other):
      z = self - other
      self.goals, self.points = z.goals, z.points
      return self

   def __str__(self):
      return '{:d} goal(s) and {:d} point(s)'.format(self.goals, self.points)
