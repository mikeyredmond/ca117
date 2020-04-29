class BankAccount(object):

   next_account_number = 16555232
   total_lodgements = 0
   interest_rate = 0.043

   def __init__(self, forename, surname, balance=0):
      self.forename = forename
      self.surname = surname
      self.account_number = self.next_account_number
      self.balance = balance
      BankAccount.next_account_number += 1

   def lodge(self, other):
      self.balance += other
      BankAccount.total_lodgements += 1

   def apply_interest(self):
      self.balance += self.balance * BankAccount.interest_rate

   def __iadd__(self, other):
      self.balance += other
      BankAccount.total_lodgements += 1
      return self

   def __str__(self):
      return 'Name: {:s} {:s}'.format(self.forename, self.surname) + "\n" + 'Account number: {:d}'.format(self.account_number) + "\n" + 'Balance: {:.2f}'.format(self.balance)
