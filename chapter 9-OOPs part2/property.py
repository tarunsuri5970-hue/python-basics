class student:
    def __init__(self,math,phy,chem):
        self.math=math
        self.phy=phy
        self.chem=chem
    @property
    def percentage(self):
        
        return str((self.math+self.phy+self.chem)/3)+"%"
s1 = student(78,98,76)
print(s1.percentage)
s1.chem=100
print(s1.percentage)