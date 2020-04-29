class Contact(object):

   def __init__(self, name, phone, email):
      self.name = name
      self.phone = phone
      self.email = email

   def __str__(self):
      return '{} {} {}'.format(self.name, self.phone, self.email)

class ContactList(object):

   def __init__(self, d={}):
      self.d = d

   def add_contact(self, other):
      self.d[other.name] = other

   def del_contact(self, name):
      if name in self.d:
         self.d.pop(name)

   def get_contact(self, name):
      if name in self.d:
         return self.d[name]
      else:
         return None

   def __str__(self):
      a = []
      print('Contact list' + "\n" + '-' * len('Contact list'))
      for k, v in sorted(self.d.items()):
         a.append('{}'.format(v))
      return "\n".join(a)
