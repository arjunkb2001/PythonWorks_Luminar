# def add(self,n1,n2):
#     return n1+n2
    
# def add(self,n1,n2,n3):
#     return n1+n2+n3
    
# def add(self,n1,n2,n3,n4):
#     return n1+n2+n3+n4
    


#   python dosent support method overloading 



# same method namw different number of parameters:





class calculator:

    # def add(self,n1,n2):
    #     return n1+n2
    
    # def add(self,n1,n2,n3):
    #     return n1+n2+n3
    
    # def add(self,n1,n2,n3,n4):
    #     return n1+n2+n3+n4
    
    def add(self,*args):
        return sum(args)
obj=calculator()

print(obj.add(200,400))