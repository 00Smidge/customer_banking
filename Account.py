""" Create a Account class with methods"""

class Account:
  """Creating an Account class with methods"""
  def __init__(self, balance, interest_rate, maturity): 
    self._balance = balance
    self._interest_rate = interest_rate
    self._maturity = maturity

  @property
  def balance(self):
    return  self._balance
  
  @property
  def interest_rate(self):
    return  self._interest_rate
  
  @property
  def maturity(self):
    return  self._maturity

  @balance.setter
  def balance(self, balance):
    self._balance = balance
  
  @interest_rate.setter
  def interest_rate(self, interest_rate):
    self._interest_rate = interest_rate
  
  @maturity.setter
  def maturity(self, maturity):
    self._maturity = maturity

  