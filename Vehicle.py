#Vehicle
#Base class
class Vehicle:
    def __init__(self,model,rental_rate):
        self.model = model
        self.rental_rate = rental_rate #Rate per hour
    def calculate_rental(self,hours):
        return self.rental_rate * hours

#Subclass1
class Car(Vehicle):
    def __init__(self,model,rental_rate,fuel_type):
        super().__init__(model,rental_rate)
        self.fuel_type = fuel_type
    
    def calculate_rental(self, hours):
        return self.rental_rate * hours

#SubClass2
class Bike(Vehicle):
    def __init__(self,model,rental_rate,helmet_required=True):
        super().__init__(model,rental_rate)
        self.helmet_required = helmet_required
    
    def calculate_rental(self, hours):
        return self.rental_rate * hours * 0.9 #10% discount for bike
    
#Subclass3
class Truck(Vehicle):
    def __init__(self,model,rental_rate,load_capacity):
        super().__init__(model,rental_rate)
        self.load_capacity = load_capacity
    
    def calculate_rental(self, hours):
        return self.rental_rate * hours *1.2 #20% surcharge for trucks
    
car = Car("Verna",50,"Diesel")
bike = Bike("Hyundai",30)
truck= Truck("Heavy Truck",100,5000)

print(f"Car rental for 5 hours: ${car.calculate_rental(5)}")
print(f"Bike rental for 5 hours: ${bike.calculate_rental(5)}")
print(f"Truck rental for 5 hours: ${truck.calculate_rental(5)}")