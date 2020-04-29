class Triathlete(object):

   def __init__(self, name, tid):
      self.name = name
      self.tid = tid

   def __str__(self):
      return 'Name: {:s}'.format(self.name) + "\n" + 'ID: {:d}'.format(self.tid)

class Triathlon(object):

   def __init__(self):
      self.d = {}

   def add(self, other):
      self.d[other.tid] = other

   def remove(self, other):
      self.d.pop(other)

   def lookup(self, other):
      if other in self.d:
         return self.d[other]
