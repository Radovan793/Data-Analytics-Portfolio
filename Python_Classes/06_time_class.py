# 06_time_class.py

class TimeClass:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    def get_time(self):
        return f"{self.hour}:{self.minute}"


# Example usage
t1 = TimeClass(5, 10)
print(t1.get_time())  # 5:10
