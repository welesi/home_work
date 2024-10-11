class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
    def to_fahrenheit(self):
        return (self._celsius * 9/5) + 32
    def get_celsius(self):
        return self._celsius

temp = Temperature(25)
print(temp.to_fahrenheit())  # Выведет 77
print(temp.get_celsius())    # Выведет 25