class Car:
    total_no_of_object = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_no_of_object += 1

    def get_brand(self):
        return self.__brand + "!!"

    def show_Car_details(self):
        return f"{self.__brand} {self.__model}"

    @staticmethod
    def general_description():
        return "Cars are vehicles with four wheels."

    @property
    def model(self):
        return self.__model


# Inhertiance Example
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size


# my_car = Car("Tata", "Mahindra")
# print(my_car.__brand)
# print(my_car.model)
# print(Car.total_no_of_object)

# my_car = Car("Tata", "Safari")
# print("Print Model:- ", my_car.model)
# my_tata_car = Car("Tata", "Nexon")
# print("Class Level:- ", Car.general_description())


# creating another object of electric car class
# my_electricCar = ElectricCar("Tesla", "Model S", 100)
# print(isinstance(my_electricCar, ElectricCar))
# print(isinstance(my_electricCar, Car))
# print(my_electricCar.show_Car_details())

# my_new_car = Car("Toyata", "Audi")
# print(my_new_car.brand)
# print(my_new_car.model)


# these are the decorator used to enhace the functionality of method
# It is just like the anntation usied in java language
# they are used for the follwong purposes
# 1. @staticmethod --> it is used to define a method which is not bound to the
# object of the class
# 2. @classmethod --> it is used to define a method which is bound to the
# class not the object of the class


# Multiple inheritance in python is possible


class Battery:
    def battery_info(self):
        return "This is battery info"


class Engine:
    def engine_info(self):
        return "This is engine info"


class ElectricCarTwo(Battery, Engine, Car):
    pass


my_tesla_car = ElectricCarTwo("Tesla", "Model")
print(my_tesla_car.battery_info())
print(my_tesla_car.engine_info())
