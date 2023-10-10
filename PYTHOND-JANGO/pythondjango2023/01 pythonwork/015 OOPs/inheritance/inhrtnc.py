class parent:

    phone="iphone"
    vechile="RC390"

    def mobile(self):
        print(self.phone)

    def bike(self):
        print(self.vechile)

class child(parent):
    pass
obj=child()
obj.mobile()
obj.bike()