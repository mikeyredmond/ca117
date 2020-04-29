class BankAccount(object):

   next_account = 16555232
   account_type = 'General'

   def __init__(self, fn, sn, balance):
      self.fn = fn
      self.sn = sn
      self.balance = balance
      self.account_number = self.next_account
      BankAccount.next_account += 1

   def lodge(self, money):
      self.balance += money

   def withdraw(self, money):
      if self.balance - money < 0:
         print('Insufficient funds available')
      else:
         self.balance -= money

   def __str__(self):
      return 'Name: {:s} {:s}'.format(self.fn, self.sn) + "\n" + 'Account number: {:d}'.format(self.account_number) + "\n" + 'Account type: {:s}'.format(self.account_type) + "\n" + 'Balance: {:.2f}'.format(self.balance)


class CurrentAccount(BankAccount):

   overdraft = 1000
   account_type = 'Current'

   def withdraw(self, money):
      if self.balance - money < -1000:
         print('Insufficient funds available')
      elif self.balance - money < 0 and self.balance - money > -1000:
         self.balance -= money
      else:
         self.balance -= money

   def __str__(self):
      return 'Name: {:s} {:s}'.format(self.fn, self.sn) + "\n" + 'Account number: {:d}'.format(self.account_number) + "\n" + 'Account type: {:s}'.format(self.account_type) + "\n" + 'Balance: {:.2f}'.format(self.balance) + "\n" + 'Overdraft: {:.2f}'.format(-self.overdraft)

class SavingsAccount(BankAccount):

   irate = 0.01
   account_type = 'Savings'

   def apply_interest(self):
      self.balance += (self.balance * self.irate)
      return self.balance

   def __str__(self):
      return 'Name: {:s} {:s}'.format(self.fn, self.sn) + "\n" + 'Account number: {:d}'.format(self.account_number) + "\n" + 'Account type: {:s}'.format(self.account_type) + "\n" + 'Balance: {:.2f}'.format(self.balance) + "\n" + 'Interest rate: {:.2f}'.format(self.irate)
