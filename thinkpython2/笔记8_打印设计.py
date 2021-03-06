# 排队打印是queue队列问题
# 首先创建一个列表，包含要打印的设计
# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron'] 
# completed_models = []
# # 模拟打印每个设计，直到没有未打印的设计为止
# # 打印每个设计后，都将其移到列表completed_models中 
# while unprinted_designs:
# 	current_design = unprinted_designs.pop()
# 	print("Printing model: " + current_design) 
# 	completed_models.append(current_design)

# print("\nThe following models have been printed:") 
# for completed_model in completed_models:
# 	print(completed_model)

# def printing_model(designs):
# 	for design in designs:
# 		info = "Printing model:" + design.title()
# 		print(info)

# printing_model(['iphone case', 'robot pendant', 'dodecahedron'])

def print_models(unprinted_designs, completed_models):
	while unprinted_designs:
		current_design = unprinted_designs.pop()
		print("Printing model: " + current_design) 
		completed_models.append(current_design)

def show_completed_models(completed_models): 
	print("\nThe following models have been printed:")
	for completed_model in completed_models:
		print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs[:], completed_models) #副本
show_completed_models(completed_models)
