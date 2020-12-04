// 法一：嵌套循环，时间复杂度O(N^2)，空间复杂度O(1)
function has_duplicate_value(array) {

	// var i 遍历数组元素；当i指向下一元素时发起第2个for循环，用var j遍历；
	// 第2个循环中检查i和j两个位置是否相同，若同，则有重复值；若无重复值则返回false；
	
	var steps = 0; // 跟踪步数

	for(var i = 0; i < array.length; i++) {
		for(var j = 0; j < array.length; j++) {
			steps++;
			if(i != j && array[i] == array[j]) {
				return true;
			}
		}
	}
	console.log(steps);
	return false;
}

// 法二：时间复杂度O(N)，但占用额外内存,O(N)
function has_duplicate_value2(array) {
	var existing_nums = [];

	// 只有1个循环；
	// array里每发现新数字，就以其为索引找出existing_nums中对应的格子并赋值1；
	
	for(var i = 0; i < array.length; i++) {
		if(existing_nums[array[i]] === undefined) {
			existing_nums[array[i]] = 1;
		} else {
			return true;
		}
	}
	return false;
}

//法三：散列表可以处理字符串,将字符串作为键
//O(N)
function has_duplicate_value3(array) {
	var existing_nums = {};
	for(var i = 0; i < array.length; i++) {
		if(existing_nums[i] === undefined) {
			existing_nums[array[i]] = 1;
		} else {
			return true;
		}
	}
	return false;
}
