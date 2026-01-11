class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


my_car = Car("Tata", "Mahindra")
print(my_car.brand)
print(my_car.model)

my_new_car = Car("Toyata", "Audi")
print(my_new_car.brand)
print(my_new_car.model)
