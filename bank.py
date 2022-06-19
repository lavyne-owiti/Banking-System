# Add these methods to class Account - deposit, withdraw. Create two instances of account and verify they work as expected.
# Add a new attribute to the class Account called deposits which by default is an empty list.
# Add another attribute to the class Account called withdrawals which by default is an empty list.
# Modify the deposit method to append each successful deposit to self.deposits
# Modify the withdrawal method to append each successful withdrawal to self.withdrawals
# Add a new method called deposits_statement which prints each deposit in a new line
# Add a new method called withdrawals_statement which prints each withdrawal in a new line
from datetime import datetime
from re import A


class Account:
   def __init__(self,acc_no,acc_name):
      self.balance=0
      self.loan_balance=0
      self.acc_no=acc_no
      self.acc_name=acc_name
      self.deposits=[]
      self.withdrawals=[]
      self.savings=0
      self.saved=[]
      self.fullsatement=[]
      self.withdrawn_savings=[]
      self.transaction=100
      self.list_transfer=[]
      self.date=datetime.now().strftime("%x %X")

   def deposit(self,amount):
       if amount<=0:
            return f"deposit should be more than zero"
       else:
           if amount>0:
               self.balance+=amount
               deposit_details={}
               self.deposits.append(amount)
               deposit_details['date']=self.date
               deposit_details['amount']=amount
               deposit_details['narration']=f'you deposited and balance is {self.balance}' 
               self.fullsatement.append(deposit_details)
               print(self.deposits)
               print(self.fullsatement)
               return deposit_details


   def withdraw(self,amount):
       amount-=self.transaction
       if amount>self.balance:
            return f"your balance {self.balance} cannot withraw {amount}"
       elif amount<=0:
            return f"withdrawal should be more than zero"
       else:
           self.balance-=amount
           withdraw_details={}
           self.withdrawals.append(amount)
           withdraw_details['date']=self.date
           withdraw_details['amount']=amount
           withdraw_details['narration']=f'you withdrew and balance is {self.balance}'
           self.fullsatement.append(withdraw_details)
           print(self.fullsatement)
           return withdraw_details
    
   def full_statement(self):
    for items in self.fullsatement:
        date=items['date']
        amount=items['amount']
        narrate=items['narration']
        print(f"On {date}---------{narrate}---------{amount}")

   def borrow(self,amount):
    count=sum(self.deposits)
    qualification=count*1/3
    interest=0.03*amount
    if len(self.deposits)<10 :
        return f"Deposits made must be more than 10"    
    elif amount<100:
        return f"Can,t borrow less than a 100 "
    elif  amount>=qualification:
        return f"Can't borrow more than your borrowing limit {qualification}" 
    elif self.loan_balance>0:
        return f"Can,t borrow another loan,till you pay {self.loan_balance}"
    else:
        self.loan_balance+=amount
        self.loan_balance+=interest
        return f"You have borrowed {amount} and your 3% interest will amount to {self.loan_balance}"


   def loan_repayment(self,amount):
     
     if amount<self.loan_balance:
        self.loan_balance-=amount
        return f"you have paid {amount} and you loan balance is {self.loan_balance}"
    
     else:
        overpay=amount-self.loan_balance
        self.balance+=overpay
        return f"you have overpaid {overpay} and you current balance is {self.balance}"
          
   
   def deposits_statement(self):
       for i in self.deposits:
         print(f"You have deposited {i}")


   def withdrawals_statement(self):
       for j in self.withdrawals:
         print(f"You have withrawn {j}")

   def transfer(self,amount,name_account):
    total=amount+self.transaction
    if total<self.balance:
        self.balance-=total
        name_account.deposit(amount)
        the_trasfer={'date':self.date,'amount':amount,'narration':'you trasfered'}
        self.list_transfer.append(the_trasfer)
        return f"you have trasfered {amount} to {name_account.acc_name}.Your new balance is {self.balance}"

     
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

