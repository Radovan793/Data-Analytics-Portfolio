# Example of class vs instance methods.

class MyClass:
    class_variable = "I am static!"

    def instance_method(self):
        print(MyClass.class_variable)


# Example usage
if __name__ == "__main__":
    obj = MyClass()
    obj.instance_method()
