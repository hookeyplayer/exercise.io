# 存储所点比萨的信息 
pizza = {'crust': 'thick', 'toppings': ['mushrooms', 'extra cheese'],}

print("You ordered a " +
	pizza['crust'] + "-crust pizza " +
	"with the following toppings:")
# 字典中嵌套了列表，一个键关联多个值
for topping in pizza['toppings']:
	print("\t" + topping)

一、单变量披萨配料：创建形参空元组 *toppings
def make_pizza(*toppings):
	print("\nMaking a pizza with the following toppings:")
	for topping in toppings:
		print("- " + topping)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# 二、多变量：披萨尺寸和配料
def make_pizza2(size, *toppings):
	print("Your " + str(size) +" inch pizza with toppings:")
	for topping in toppings:
		print('\t' + topping.title())

make_pizza2(12, 'pepperoni', 'green onions')