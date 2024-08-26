""" Create a Account class with methods"""

class Account:
  """Creating an Account class with methods"""
  def __init__(self, balance, interest, maturity, account_type): 
    self.balance = balance
    self.interest = interest
    self.maturity = maturity
    self.account_type = account_type

  # This method sets the balance of the account.
  def set_balance(self, balance):
    """Sets the balance for the for the account"""
    self.balance = balance

  # The method sets the interest gained for the account.
  def set_interest(self, interest):
    """Sets the interest gained for the the account"""
    self.interest = interest

  def set_account_type(self, account_type):
    """Sets the account type the users is currently using"""
    self.account_type = account_type

  def set_maturity(self, maturity):
    """Sets the maturity rate for the account"""
    self.maturity = maturity