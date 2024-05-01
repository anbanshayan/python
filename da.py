class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):  # Add 'name' and 'salary' arguments
        super().__init__(name, salary)  # Pass 'name' and 'salary' to the parent class's constructor
        self.department = department

    def display(self):
        print(self.name, self.salary, self.department)

m1 = Manager("K.Anbalagan", "100000", "Management")
m1.display()
