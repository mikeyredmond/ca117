class BankAccount(object):

   def __init__(self, balance=0.00):
      self.b = balance

   def deposit(self, money):
      self.b = self.b + money

   def withdraw(self, money):
      if self.b - money < 0:
         print('Insufficient funds available')
      else:
         self.b = self.b - money

   def __str__(self):
      return 'Your current balance is: {:.2f} {:s}'.format(self.b, 'euro')
