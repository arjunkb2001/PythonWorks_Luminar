class bike:

    def start(self):
        print("kicker start")
    
    def breaking(self):
        print("drum break")

class herohondaspelender(bike):
    def start(self):
        print("self start")
    def breaking(self):
        print("abs break")

hobj=herohondaspelender()

hobj.start()