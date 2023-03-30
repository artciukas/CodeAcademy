
class Employee:
    def __init__(self, name, age, exp) -> None:
        self.name = name
        self.age = age
        self.exp = exp
        

    def print(self):
        print(self.name, self.age, self)
        print(self.exp)





class Engineer(Employee):
    def __init__(self, name, age, exp, level) -> None:
        self.level = level
        self.exp = exp
        super().__init__(name, age, exp=self.exp)
    def show(self):
        super().print()
        print(self.level)
    





engineer_01 = Engineer('Tim', 35, 3000, "Junior")
engineer_01.show()
# name,age,exp,positiona