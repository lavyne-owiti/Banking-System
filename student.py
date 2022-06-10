# Add these methods to class student - full_name, year_of_birth, initials. Create two instances and verify the work as expected

class Student:
    school="AkiraChix"
    def __init__(self,first_name,last_name,age,country):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.country=country
    def greet(self):
        return f"Hello {self.first_name} from {self.country}.Welcome to {self.school} "
    def full_name(self):
        return f"Helllo I am {self.first_name} {self.last_name}."
    def year_of_birth(self):
        x=2022- self.age
        return f"I was born in {x}."
    def initials(self):
        y=self.first_name[0]+self.last_name[0]
        return f"My initials are {y.upper()}."
