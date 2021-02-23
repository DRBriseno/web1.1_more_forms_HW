import random 

class BankAccount():
      ROUTING_NUMBER = 12345678
      BALANCE = 0
      ACCOUNT_NUMBER = random.randint(1, 10**8 - 1)
def __init__(self, name):
    self.name = name
    self.routing_number = BankAccount.ROUTING_NUMBER
    self.balance = BankAccount.BALANCE
    self.account_number = BankAccount.ACCOUNT_NUMBER
