class City
	attr_accessor :name, :routes
	def initialize(name)
		@name = name
		# 不同于social network的边（数组），此处是散列表，
		@routes = {boston => 100,
			denver => 160}
	end
	# 城市间的航线标价
	def add_route(city, price)
		@routes[city] = price_info
	end
end

atlanta = City.new("Atlanta") 
boston = City.new("Boston") 
chicago = City.new("Chicago") 
denver = City.new("Denver") 
el_paso = City.new("El Paso")
atlanta.add_route(boston, 100) 
atlanta.add_route(denver, 160) 
boston.add_route(chicago, 120) 
boston.add_route(denver, 180) 
chicago.add_route(el_paso, 80) 
denver.add_route(chicago, 40) 
denver.add_route(el_paso, 140)

def dijkstra(starting_city, other_cities)
	# 散列表用来保存从給定城市到其他所有城市到价格
	# {终点城市 => [价格, 到达终点城市前所要经过的那个城市]}
	routes_from_city = {}
	routes_from_city[starting_city] = [0, starting_city]
	# 此时其他城市都未知，设为无限
	other_cities.each do |city|
		routes_from_city[city] = [Float::INFINITY, nil]
	end
	visited_cities = []
	current_city = starting_city
	# 循环访问每个城市
	while current_city
		# 访问当前城市
		visited_cities << current_city
		current_city.routes.each do |city, price_info|
			# 如果起点城市到其他城市的价格比 routes_from_city 所记录的更低，则更新记录
			if routes_from_city[city][0] > price_info +
				routes_from_city[current_city][0], current_city]
				routes_from_city[city] = [price_info +
					routes_from_city[current_city][0], current_city]
			end
		end
		# 决定下一个要访问的城市
		current_city = nil
		cheapest_route_from_current_city = Float::INFINITY
		# 检查所有已记录的路线
		routes_from_city.each do |city, price_info|
			# 在未访问的城市中找出最便宜的那个，设为下个待访问
			if price_info[0] < cheapest_route_from_current_city &&
				!visited_cities.include?(city)
				cheapest_route_from_current_city = price_info[0]
				current_city = city
			end
		end
	end
	return routes_from_city
end

routes = dijkstra(atlanta, [boston, chicago, denver, el_paso]) 
routes.each do |city, price_info|
	p "#{city.name}: #{price_info[0]}"
end