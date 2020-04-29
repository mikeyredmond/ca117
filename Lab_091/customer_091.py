class Customer(object):

   discount = 0

   def __init__(self, name, balance, street, town, county):
      self.name = name
      self.balance = balance
      self.street = street
      self.town = town
      self.county = county
      self.newbalance = 0

   def owes(self):
      self.newbalance = self.balance - (self.balance * (self.discount / 100))
      return self.newbalance

   def __str__(self):
      return self.name + "\n" + self.street + "\n" + self.town + "\n" + self.county + "\n" + 'Balance: {:.2f}'.format(self.balance) + "\n" + 'Discount: {:d}%'.format(self.discount) + "\n" + 'Amount due: {:.2f}'.format(self.owes())

class ValuedCustomer(Customer):

   discount = 10
