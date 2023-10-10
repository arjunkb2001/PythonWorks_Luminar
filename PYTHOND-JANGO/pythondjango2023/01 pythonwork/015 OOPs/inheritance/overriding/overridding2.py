class parent():
    vechile=["rc390","lancer"]
    
    def properties(self):
        return  self.vechile
    
class child(parent):

    def properties(self):
        self.vech=super().properties()
        self.vech.append("duke200")
        return self.vech


ch=child()
print(ch.properties())