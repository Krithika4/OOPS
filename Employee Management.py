#Employee Manangement
#Base class
class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def calculate_salary(self):
        return self.salary

#Subclass or Regular Employee
class RegularEmployee(Employee):
    def __init__(self,name,salary,bonus):
        super().__init__(name,salary)
        self.bonus = bonus
    def calculate_salary(self):
        return self.salary * self.bonus
    
#Subclass for contract employee
class ContractEmployee(Employee):
    def __init__(self,name,hourly_rate,hourly_worked):
        super().__init__(name,hourly_rate*hourly_worked)
        self.hourly_rate = hourly_rate
        self.hourly_worked = hourly_worked
    def calculate_salary(self):
        return self.hourly_rate * self.hourly_worked

#Subclass for Manager
class Manager(Employee):
    def __init__(self,name,salary,bonus,team_incentive):
        super().__init__(name,salary)
        self.bonus = bonus
        self.team_incentive = team_incentive
    def calculate_salary(self):
        return self.salary +self.bonus+self.team_incentive

regular =RegularEmployee("Linda",50000,5000)
contract =ContractEmployee("Alice",50,160)
manager = Manager("Charlie",80000,10000,5000)

print(f"{regular.name}'s Salary:${regular.calculate_salary()}")
print(f"{contract.name}'s Salary:${contract.calculate_salary()}")
print(f"{manager.name}'s Salary:${manager.calculate_salary()}")
