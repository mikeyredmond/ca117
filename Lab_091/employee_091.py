class Employee(object):

   def __init__(self, name, employeenumber):
      self.name = name
      self.employeenumber = employeenumber

   def wages(self):
      return 0

   def __str__(self):
      return 'Name: {:s}'.format(self.name) + "\n" + 'Number: {:d}'.format(self.employeenumber) + "\n" + 'Wages: {:.2f}'.format(self.wages())

class Manager(Employee):

   def __init__(self, name, employeenumber, salary):
      super().__init__(name, employeenumber)
      self.salary = salary

   def wages(self):
      return self.salary / 52

class AssemblyWorker(Employee):

   def __init__(self, name, employeenumber, hourly_rate, hours_worked):
      super().__init__(name, employeenumber)
      self.hourly_rate = hourly_rate
      self.hours_worked = hours_worked

   def wages(self):
      return self.hourly_rate * self.hours_worked
