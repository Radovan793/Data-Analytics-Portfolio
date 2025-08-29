# Car with auto-incremented ID.

class Car:
    _next_id = 1

    def __init__(self, manufacturer, speed=0, is_started=False):
        self.id = Car._next_id
        Car._next_id += 1
        self.manufacturer = manufacturer
        self.speed = speed
        self.is_started = is_started

    def start(self):
        self.is_started = True

    def speedup_by(self, value):
        self.speed += value

    def speeddown_by(self, value):
        self.speed = max(0, self.speed - value)

    def get_info(self):
        return (f"Car ID: {self.id}, Manufacturer: {self.manufacturer}, "
                f"Speed: {self.speed}, Started: {self.is_started}")


# Example usage
car1 = Car("Toyota")
car2 = Car("Honda", speed=30)
car3 = Car("Ford", speed=50, is_started=True)

car1.start()
car1.speedup_by(20)
car2.speeddown_by(10)

print(car1.get_info())
print(car2.get_info())
print(car3.get_info())
