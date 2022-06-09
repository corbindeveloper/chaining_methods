class User:	
   bank_name = "First National Dojo"

   def __init__(self, name, email):
      self.name = name
      self.email = email
      self.account_balance = 0

   # deposit
   def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
      self.account_balance += amount	# the specific user's account increases by the amount of the value received
      return self

   # withdrawal
   def make_withdrawal(self, amount):
      self.account_balance -= amount
      return self

   # display
   def display_user_balance(self):
      print(f"User: {self.name}, Balance {self.account_balance}")
      return self

   # transfer
   def transfer_money(self, other_user, amount):
      self.account_balance -= amount
      other_user.account_balance += amount
      print(f"{self.name} has transfered {amount} to {other_user.name}")
      print(f"{self.name} has a new balance of {self.account_balance}")

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
murphy = User("Murphy Merf", "murphy@merf.aol")

guido.make_deposit(100).make_deposit(200).make_deposit(50).make_withdrawal(25).display_user_balance()

monty.make_deposit(100).make_deposit(200).make_withdrawal(50).make_withdrawal(25).display_user_balance()

murphy.make_deposit(1000).make_withdrawal(100).make_withdrawal(100).make_withdrawal(40).display_user_balance()

murphy.transfer_money(guido, 100)
