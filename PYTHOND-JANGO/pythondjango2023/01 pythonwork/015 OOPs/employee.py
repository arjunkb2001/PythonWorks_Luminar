class employee:
    id:int
    name:str
    department:str
    gender:str


    def create(self,id,name,dept,gender):
        self.id=id
        self.name=name
        self.department=dept
        self.gender=gender

    def display_emp(self):
     
     print(self.id,self.name,self.department,self.gender)

    def __str__(self) -> str:
       return self.name
    

obj=employee()
obj.create(100,"hari","hr","male")
obj.display_emp()

print(obj)

