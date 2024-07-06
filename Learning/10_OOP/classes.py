class Car:
    total_cars = 0
    def __init__(self, name, model, color):
        self.name = name
        self.model = model
        self.color = color
        Car.total_cars += 1

    def info(self):
        return f"Car details are: {self.name}, {self.model}, {self.color}"


class ElectricCar(Car):
    def __init__(self, name, model, color, battery_size):
        super().__init__(name, model, color)
        self.battery_size = battery_size

    def info(self):
        return f"Electric Car details are: {self.name}, {self.model}, {self.color}, {self.battery_size}"

    def fuel_type(self):
        return "Electric"

# Creating instances of Car and ElectricCar
car1 = Car("BMW", "X5", "Black")
print(car1.info())

car2 = ElectricCar("BMW", "iX", "White", "2000KAh")
print(car2.info())

print(Car.total_cars)