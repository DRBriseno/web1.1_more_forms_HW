import math
import random
import string

list_of_acct_nums = range(1, 10**9,) #  => [1: 99999999]

random_number = random.randit(1, 10*9 - 1) # random 8 digit number => 00000003



class BankAccount:
    def __init__(self, full_name, money, account_number, balance, interest, routing_number=36333777):
        self.full_name = full_name
        self.money = money
        self.account_number = account_number
        self.interest = interest 
        self.balance = balance
        self.routing_number = routing_number
        #self.interest = balance * .00083
        #self.account_number = random.randint(00000000,999999999)

        ran_index = random.randint(len(list_of_acct_nums))  #get a random number from the list
        self.random_number = list_of_acct_nums.pop(rand_index) #pops each so it doesnt repeat
        self.random_number = str(random_number)
        self.random_number = 0*(7 - len(random_number)) + random_number

        def deposit(self,ammount):
            self.money = self.money + ammount
            return self.get_balance()
