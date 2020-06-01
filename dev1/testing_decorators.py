# class Celsius:
#     def __init__(self, temperature=0):
#         self.set_temperature(temperature)
#
#     def to_fahrenheit(self):
#         return (self.get_temperature() * 1.8) + 32
#
#     """ replaced temperature with _temperature to make it private """
#     def set_temperature(self, value):
#         if value < -273.5:
#             raise ValueError("Temperature below -273.5 is not possible")
#         self._temperature = value
#
#     # getter method
#     def get_temperature(self):
#         return self._temperature
#
#
# # create a new object
# human = Celsius(37)
#
# # get the temp
# print(human.get_temperature())
#
# print(human.to_fahrenheit())
#
# # No restriction to privates in python. We can set temperature to -300
# # This will bypass our value error
# human._temperature = -300
# print(human.to_fahrenheit())

# class Celsius:
#     def __init__(self, temperature=0):
#         self.set_temperature(temperature)
#
#     def to_fahrenheit(self):
#         return (self.get_temperature() * 1.8) + 32
#
#     """ replaced temperature with _temperature to make it private """
#     def set_temperature(self, value):
#         print("Setting value")
#         if value < -273.5:
#             raise ValueError("Temperature below -273.5 is not possible")
#         self._temperature = value
#
#     # getter method
#     def get_temperature(self):
#         print("Getting value")
#         return self._temperature
#
#     """ We can create a property object in this way as well """
#     temperature = property(get_temperature, set_temperature)
#
#
# """ Any code that sets the value of temperature will call setters
#     and any code that retrieves the value of temperature will call getters"""
# human = Celsius(37)
# print(human.temperature)
# print(human.to_fahrenheit())
# human.temperature = -300


class Celsius:
    """ In this class we use our temperature name
    while using @property. Also this is the most efficient
    and recommend way ---------------------------------"""
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        print("Setting value")
        if value < -273.5:
            raise ValueError("Temperature below -273.5 is not possible")
        self._temperature = value




# create a new object
human = Celsius(37)

print(human.temperature)
print(human.to_fahrenheit())
coldest_ever = Celsius(-300)

