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
