# hiding implimentation detials 


from abc import ABC,abstractmethod

class car(ABC):
    @abstractmethod
    def start (self):
        pass
    
    @abstractmethod
    def stop(self):
        pass


    @abstractmethod
    def accelerated(self):
        pass

class swift(car):

    def start(self):
        print("swift starts")

    def accelerated(self):
        print("swift accelerated")
    
    def stop(self):
        print("swift stop")

obj=swift()
obj.start()
obj.accelerated()
obj.stop()
