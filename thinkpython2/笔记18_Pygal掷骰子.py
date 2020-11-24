# pip install --user pygal
from random import randint 
# 生成一个掷骰子的类
class Die():
	def __init__(self, num_sides=6):
		self.num_sides = num_sides
# 方法roll()使用函数randint()来返回一个1、面数、和之间的随机整数
	def roll(self): 
		return randint(1, self.num_sides)

# 假设上述die.py
from die import Die
# 创建一个D8
die = Die()
results = []

for roll_num in range(100):
	result = die.roll()
	results.append(result) 

print(results)

# 分析结果
frequencies = []
for value in range(1, die.num_sides+1): #易错点
	frequency = results.count(value)
	frequencies.append(frequency)

print(frequencies) #[155, 167, 168, 170, 159, 181]

# 可视化
hist = pygal.Bar()
hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
# add()：包含了要给添加的值指定的标签、列表
hist.add('D6', frequencies) 
# 图表渲染为一个SVG文件
hist.render_to_file('die_visual.svg')