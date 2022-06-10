# Add these methods to class Account - deposit, withdraw. Create two instances of account and verify they work as expected.
# Add a new attribute to the class Account called deposits which by default is an empty list.
# Add another attribute to the class Account called withdrawals which by default is an empty list.
# Modify the deposit method to append each successful deposit to self.deposits
# Modify the withdrawal method to append each successful withdrawal to self.withdrawals
# Add a new method called deposits_statement which prints each deposit in a new line
# Add a new method called withdrawals_statement which prints each withdrawal in a new line
class Account:
   def __init__(self,acc_no,acc_name):
      self.balance=0
      self.acc_no=acc_no
      self.acc_name=acc_name
      self.deposits=[]
      self.withdrawals=[]
      self.savings=0
      self.saved=[]
      self.withdrawn_savings=[]
      self.transaction=100

   def deposit(self,amount):
       if amount<=0:
            return f"deposit should be more than zero"
       else:
           if amount>0:
               self.balance+=amount
               self.deposits.append(amount)
               print(self.deposits)
               return f"you have deposited {amount},new balance is {self.balance}"


   def withdraw(self,amount):
       amount-=self.transaction
       if amount>self.balance:
            return f"your balance {self.balance} cannot withraw {amount}"
       elif amount<=0:
            return f"withdrawal should be more than zero"
       else:
           self.balance-=amount
           self.withdrawals.append(amount)
           print(self.withdrawals)
           return f"you have deposited {amount},new balance is {self.balance}"


   def deposits_statement(self):
       for i in self.deposits:
         print(f"You have deposited {i}")


   def withdrawals_statement(self):
       for j in self.withdrawals:
         print(f"You have withrawn {j}")

   def saving(self,amount):
       if amount<=0:
            return f"savings amount should be more than zero"
       else:
            self.savings+=amount
            self.saved.append(amount)
            print(self.saved)
            return f" You have saved {amount} in your savings account,your balance is {self.savings}."
            
   def savings_withdrawals(self,amount):

        if amount>self.savings:
            return f"Your savings is {self.savings} cannot withraw {amount}"
        elif amount<0:
            return f"withdrawal should be more than zero"
        else:
            if len(self.withdrawn_savings)<4:
                 self.savings-=amount
                 self.withdrawn_savings.append(amount)
                 print(self.withdrawn_savings) 
            else:
                return f"You can't withdraw {amount} because you have reached the maximun withdrawals,hence you cant withdraw from {self.savings}."

   def current_balance(self):
    return f' Your current balance is {self.balance} ,while you savings balance is {self.savings}'
   




           