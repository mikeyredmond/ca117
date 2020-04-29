class Triathlete(object):

   def __init__(self, name, tid):
      self.name = name
      self.tid = tid
      self.d = {}

   def add_time(self, activity, time):
      self.d[activity] = time

   def get_time(self, activity):
      return self.d[activity]

   def __eq__(self, other):
      return sum(self.d.values()) == sum(other.d.values())

   def __lt__(self, other):
      return sum(self.d.values()) < sum(other.d.values())

   def __gt__(self, other):
      return sum(self.d.values()) > sum(other.d.values())

   def __str__(self):
      return 'Name: {:s}'.format(self.name) + "\n" + 'ID: {:d}'.format(self.tid) + "\n" + 'Race time: {:d}'.format(sum(self.d.values()))

class Triathlon(object):

   def __init__(self):
      self.d = {}

   def add(self, other):
      self.d[other.tid] = other

   def best(self):
      return min(self.d.values())

   def worst(self):
      return max(self.d.values())

   def remove(self, other):
      self.d.pop(other)

   def lookup(self, other):
      if other in self.d:
         return self.d[other]

   def __str__(self):
      o = []
      for p in sorted(self.d.values(), key=sorter):
         o.append('Name: {:s}'.format(p.name))
         o.append('ID: {:d}'.format(p.tid))
      return "\n".join(o)

def sorter(t):
   return t.name
