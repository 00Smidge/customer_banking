""" Create a Account class with methods"""

class Account:
  """Creating an Account class with methods"""
  def __init__(self, balance, interest, maturity, account_type): 
    self.balance = balance
    self.interest = interest
    self.maturity = maturity
    self.account_type = account_type

  @property
  def balance(self):
    return  self.balance
  
  @property
  def interest(self):
    return  self.interest
  
  @property
  def maturity(self):
    return  self.maturity
  
  @property
  def account_type(self):
    return  self.account_type

  @balance.setter
  def balance(self, balance):
    self.balance = balance
  
  @interest.setter
  def interest(self, interest):
    self.interest = interest
  
  @maturity.setter
  def maturity(self, maturity):
    self.maturity = maturity
  
  @account_type.setter
  def account_type(self, account_type):
    self.account_type = account_type

  