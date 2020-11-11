aliens = []
# 创建30个外星人
for alien_number in range(30):
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)
# 将前三个外星人修改为黄色的、速度为中等且值10个点
for alien in aliens[:3]:
	# new_alien['color'] = 'yellow'
	# new_alien['speed'] = 'medium'
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10
	elif alien['speed'] == 'slow':
		alien['color'] = 'red'
		alien['speed'] = 'fast'
		alien['points'] = 15

		
# 显示前5个外星人
# print(aliens[:5])
for alien in aliens[:5]:
	print(alien)