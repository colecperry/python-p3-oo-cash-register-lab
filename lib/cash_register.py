#!/usr/bin/env python3
import ipdb;

class CashRegister:
  def __init__(self, discount=0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.last_transaction = 0
    

  # creatting a class
  # 1: stub out known methods, plus init
  # 2: write any needed comments for later
  # 3: write and test each method

  def add_item(self, title, price, quantity=1):
    self.last_transaction = price * quantity
    self.total += self.last_transaction
    for num in range(quantity):
      self.items.append(title)

    


  def apply_discount(self):
    if(self.discount != 0):
      remaining_total = 1 - (self.discount/100)
      self.total = self.total * remaining_total
      display_total = self.total
      if(display_total.is_integer()):
        display_total = int(display_total)
      print(f"After the discount, the total comes to ${display_total}.")
    else:
      print("There is no discount to apply.")


  def void_last_transaction(self):
    self.total -= self.last_transaction