function intersection(first_array, second_array) {
	var result = [];

	// 外部循环遍历第1个数组
	// 在遇到每个值时，发起内部循环，检查第2个数组有没有值与其相同，插入到result
	// 效率：O(N^2)

	for(var i = 0; i < first_array.length; i++) {
		for(var j = 0; j <second_array.length; j++) {
			if(first_array[i] == second_array[j]) {
				result.push(first_array[i]);

				// break中断内部循环，余下的不必检查了，节省步数

				break;
			}
		}
	}
	return result;
}

first_array = [3, 1, 4, 2]
second_array = [4, 5, 3, 6]
intersection(first_array, second_array)