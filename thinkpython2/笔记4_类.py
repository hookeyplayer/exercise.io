# 一、父类，superclass
class Car():

	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self): 
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()

	def update_odometer(self, mileage):
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!") # 禁止回调里程数字

	def increment_odometer(self, miles):
		self.odometer_reading += miles # 递增

	def read_odometer(self):
		print("This car has " + str(self.odometer_reading) + " miles on it.")

# my_new_car = Car('audi', 'a4', 2016) 
# print(my_new_car.get_descriptive_name())
# # 修改里程信息
# # my_new_car.odometer_reading = 23
# my_new_car.update_odometer(23)
# my_new_car.increment_odometer(10)
# my_new_car.read_odometer()

# 二、子类
class Battery():
	def __init__(self, battery_size=70):
		self.battery_size = battery_size

	def describe_battery(self):
		print("This car has a " + str(self.battery_size) + "-kWh battery.")

	def get_range(self):
		if self.battery_size == 70:
			range = 240
		elif self.battery_size == 85:
			range = 270
			
		message = "This car can go approximately " + str(range) 
		message += " miles on a full charge."
		print(message)


class ElectricCar(Car):
	def __init__(self, make, model, year):
		super().__init__(make, model, year)
		# self.battery_size = 70
		self.battery = Battery()

	# def describe_battery(self):
	 	# print("This car has a " + str(self.battery_size) + "-kWh battery.")

	def fill_gas_tank():
		print("This car doesn't need a gas tank!") # 子类没有油箱，重写父类

my_tesla = ElectricCar('tesla', 'model s', 2016)
# 父类老的属性
print(my_tesla.get_descriptive_name())
# 子类新的属性
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

