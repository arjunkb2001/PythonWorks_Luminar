class student:
    id:int
    name:str
    department:str
    gender:str


    def create(self,id,name,dept,gender):
        self.id=id
        self.name=name
        self.department=dept
        self.gender=gender

    def display_std(self):
     
     print(self.id,self.name,self.department,self.gender)

obj=student()
obj.create(100,"hari","hr","male")
obj.display_std()