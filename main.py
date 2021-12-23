class Employees:
    #Above is the class
    def __init__(self, name, age):
        #this basically acts as a blueprint if i wanted to make a new employee.
        #so if I wanted to make a new employee I would have to pass in a name and an age for each new employee.
        self.name = name
        self.age = age


    def get_name(self):
        return self.name


    def plusone(self, add):
        #above is a defined method
        return add + 1
    #this method adds 1 everytime you pass in a value when you print it
    def speak(self):
        print('you have spoken')

e = Employees('Employee1', 24)
print(e.get_name())
print(e.age)
e2 = Employees('Employee2', 23)
print(e2.get_name())
print(e2.age)



