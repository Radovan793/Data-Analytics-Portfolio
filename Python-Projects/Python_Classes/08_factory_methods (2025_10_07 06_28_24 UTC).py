#  Factory methods to create pre-configured car objects.

class Car:
    def __init__(self, manufacturer):
        self.manufacturer = manufacturer

    @classmethod
    def makeBMW(cls):
        return cls("BMW")

    @classmethod
    def makeAudi(cls):
        return cls("Audi")


# Example usage
if __name__ == "__main__": 
    car1 = Car.makeBMW()
    car2 = Car.makeAudi()

    print(car1.manufacturer)
    print(car2.manufacturer)
