# decorator

# DRY  (Donot Repeat Yourself)

class student:
    def __str__(self,name,age):
        self.name=name
        self.age=age

    @property
    def get_name(self):

        return self.name
    @property
    def get_age(self):

        return self.age
    
obj=student("hari",25)

print(obj.get_name)
print(obj.get_age)