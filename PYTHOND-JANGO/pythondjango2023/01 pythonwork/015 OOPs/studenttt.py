class student:
    id:int
    name:str
    age:int
    course:str

    def __init__(self,id,name,age,course):
        self.id=id
        self.name=name
        self.age=age
        self.course=course


    def display_studet(self):
        print(self.name,self.age)

    def __str__(self) -> str:
        return self.name

obj1=student(100,"hari",25,"bca")
# obj1.display_studet()

print(obj1)