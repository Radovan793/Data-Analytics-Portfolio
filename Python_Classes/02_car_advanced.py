# Car with start/stop functionality and speed control.

class Car:
    def __init__(self, manufacturer, speed=0):
        self.manufacturer = manufacturer
        self.speed = speed
        self.is_started = False

    def start(self):
        self.is_started = True
        print(f"{self.manufacturer} car started.")

    def speed_up_by(self, value):
        if self.is_started:
            self.speed += value
            print(f"{self.manufacturer} car speed increased by {value} km/h.")
        else:
            print(f"Start the {self.manufacturer} car before increasing speed.")

    def speed_down_by(self, value):
        if self.is_started:
            self.speed = max(0, self.speed - value)
            print(f"{self.manufacturer} car speed decreased by {value} km/h.")
        else:
            print(f"Start the {self.manufacturer} car before decreasing speed.")

    def get_info(self):
        status = "Started" if self.is_started else "Stopped"
        print(f"--- {self.manufacturer} Car Info ---")
        print(f"Status: {status}")
        print(f"Current Speed: {self.speed} km/h\n")


# Example usage
big_car = Car("Toyota")
big_car.start()
big_car.speed_up_by(5)
big_car.speed_down_by(10)
big_car.get_info()
