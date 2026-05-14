# Car with fuel management and driving simulation.

class Car:
    def __init__(self, manufacturer, speed=0, fuel_level=100):
        self.manufacturer = manufacturer
        self.speed = speed
        self.fuel_level = fuel_level

    def display_info(self):
        print(f"Manufacturer: {self.manufacturer}")
        print(f"Speed: {self.speed} km/h")
        print(f"Fuel Level: {self.fuel_level}%")

    def accelerate(self, increase_by):
        self.speed += increase_by
        print(f"Accelerated by {increase_by} km/h. New speed: {self.speed} km/h")

    def brake(self, decrease_by):
        self.speed = max(0, self.speed - decrease_by)
        print(f"Braked by {decrease_by} km/h. New speed: {self.speed} km/h")

    def refuel(self, amount):
        self.fuel_level = min(100, self.fuel_level + amount)
        print(f"Refueled by {amount}%. Current fuel level: {self.fuel_level}%")

    def drive(self, distance):
        fuel_needed = distance / 10
        if fuel_needed <= self.fuel_level:
            self.fuel_level -= fuel_needed
            print(f"Drove {distance} km. Fuel used: {fuel_needed}%. Fuel left: {self.fuel_level:.1f}%")
        else:
            max_distance = self.fuel_level * 10
            print(f"Not enough fuel to drive {distance} km. You can drive up to {max_distance:.1f} km.")


# Example usage
if __name__ == "__main__":
    my_car = Car("Toyota", speed=50)
    my_car.display_info()
    my_car.accelerate(30)
    my_car.brake(60)
    my_car.refuel(20)
    my_car.drive(100)
    my_car.display_info()
