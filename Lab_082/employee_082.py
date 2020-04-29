class Employee(object):

   next_employee_number = 0

   def __init__(self, name, hours_worked=0, hourly_rate=9.25):
      self.name = name
      self.id = self.next_employee_number
      self.hours_worked = hours_worked
      self.hourly_rate = hourly_rate
      self.wages = hours_worked * hourly_rate
      Employee.next_employee_number += 1

   def add_hours(self, other):
      self.hours_worked += other
      self.wages += other * self.hourly_rate

   def __str__(self):
      return 'Name: {:s}'.format(self.name) + "\n" + 'ID: {:d}'.format(self.id) + "\n" + 'Hours: {:.2f}'.format(self.hours_worked) + "\n" + 'Rate: {:.2f}'.format(self.hourly_rate) + "\n" + 'Wages: {:.2f}'.format(self.wages)
