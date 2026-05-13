Python_Classes/01_car_basics.py

class Car:
    def __init__(self, manufacturer, speed):
        self.manufacturer = manufacturer
        self.speed = speed

    def display_info(self):
        print(f"Manufacturer: {self.manufacturer}")
        print(f"Speed: {self.speed} km/h")


# Example usage
if __name__ == "__main__":
    my_car = Car("Toyota", 180)
    my_car.display_info()
