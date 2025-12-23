#    Abtraction (hiding the implement details of a class and only showing the essential feature to the user )
class car:
     def __init__(self):
      self.acc=False
      self.brk=False
      self.clutch=False
      def start(self):
         self.clutch=True
         self.acc=True
         print("car started..")
         car1=car()
         car1.start()
         # Encapsulation(wrapping data and function into a single unit(object))
# Create Aaccount class with 2 attribute - blance and account no 
# create method for debit,credit and printing the blance.
class Account:
   def __init__(self,bal,acc):
      self.balance=bal
      self.account_no=acc
      #debit method
      def debit(self,amount):
         self.balance-=amount
         print("Rs.",amount,"was debited")
         print("total balance=",self.get_balance())
      def credit(self,amount):
         self.balance+=amount
         print("Rs.",amount,"was credited")
         print("total balance=",self.get_balance())
         def get_balance(self):
            return self.balance

      acc1=Account(10000,12345)
      acc1.debit(1000)
      acc1.credit(500)
      acc1.credit(40000)
      acc1.debit(10000)
      print(acc1.balance)
      print(acc1.account_no)