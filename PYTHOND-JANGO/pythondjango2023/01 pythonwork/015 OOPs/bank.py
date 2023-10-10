from datetime import datetime


class  bank:
    bank_name:str
    accno:str
    person_name:str
    ac_type:str
    balance:int

    def create(self,b_name,acno,p_name,ac_type,bal):
        self.bank_name=b_name
        self.accno=acno
        self.person_name=p_name
        self.ac_type=ac_type
        self.balance=bal

    def deposit(self,amount):
        self.balance+=amount
        print(f"your {self.bank_name} has been credited with {amount} avl bal is {self.balance}")

    def witdraw(self,amount):
        if amount<self.balance:
            print("transaction faild insufficient balance")
        else:
            self.balance-=amount
            print(f"your {self.bank_name} has been debited with {amount} avl bal is {self.balance}")
    def get_balanace(self):
        print(f"your {self.bank_name} A/C {self.accno} bal on {datetime.today} is  {self.balance}")
    



obj1=bank()

obj1=bank()
obj1.create("sbi","10234","vijay","savings",4000)
obj1.get_balanace()
# obj1.deposit(2000)

obj2=bank()
obj2.create("sbi","10236","jhon","savings",5000)

# obj2.witdraw(5000)