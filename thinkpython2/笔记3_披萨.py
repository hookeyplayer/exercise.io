# 存储所点比萨的信息 
pizza = {
'crust': 'thick',
'toppings': ['mushrooms', 'extra cheese'],
}
# 概述所点的比萨
print("You ordered a " + pizza['crust'] + "-crust pizza " +
"with the following toppings:")
# 字典中嵌套了列表，一个键关联多个值
for topping in pizza['toppings']:
	print("\t" + topping)