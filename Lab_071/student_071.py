class Student(object):

   def __init__(self, surname=0, forename=0, sid=0, modlist=[]):
      self.id = sid
      self.sn = surname
      self.fn = forename
      self.ml = modlist

   def add_module(self, module):
      self.ml.append(module)

   def del_module(self, module):
      if module in self.ml:
         self.ml.remove(module)

   def print_details(self):
      s = ' '
      print('{:s}: {:d}'.format("ID", self.id))
      print('{:s}: {:s}'.format("Surname", self.sn))
      print('{:s}: {:s}'.format("Forename", self.fn))
      print('{:s}: '.format("Modules") + s.join(self.ml))
