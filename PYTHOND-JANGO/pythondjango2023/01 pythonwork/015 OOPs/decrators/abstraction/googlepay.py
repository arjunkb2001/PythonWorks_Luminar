# hiding implimentation detials 


from abc import ABC,abstractmethod

class bankapp(ABC):
    
    @abstractmethod
    def balanceenquiry (self):
        pass
    
    @abstractmethod
    def fundtranction(self):
        pass


    @abstractmethod
    def tranctionhistory(self):
        pass

class googlepay(bankapp):

    def balanceenquiry(self):
        print("your a/c balacnce...")

    def fundtranction(self):
        print("google pay money tranction ....")
    
    def tranctionhistory(self):
        print("your google pay tranction history....")

gpay=googlepay()
gpay.balanceenquiry()
gpay.fundtranction()
gpay.tranctionhistory()
