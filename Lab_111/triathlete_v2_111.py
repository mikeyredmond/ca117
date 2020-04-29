class Triathlete(object):

   all_time = 0
   d = {}

   def __init__(self, name, tid):
      self.name = name
      self.tid = tid

   def add_time(self, activity, time):
      Triathlete.d[activity] = time

   def get_time(self, activity):
      return self.d[activity]

   def __str__(self):
      return 'Name: {:s}'.format(self.name) + "\n" + 'ID: {:d}'.format(self.tid) + "\n" + 'Race time: {:d}'.format(sum(self.d.values()))
