class Element(object):

   def __init__(self, n=0, title=0, symbol=0, bp=0):
      self.number = n
      self.name = title
      self.s = symbol
      self.boilingpoint = bp

   def print_details(self):
      print('{:s}: {:d}'.format("Number", self.number))
      print('{:s}: {:s}'.format("Name", self.name))
      print('{:s}: {:s}'.format("Symbol", self.s))
      print('{:s}: {:} {:s}'.format("Boiling point", self.boilingpoint, "K"))
