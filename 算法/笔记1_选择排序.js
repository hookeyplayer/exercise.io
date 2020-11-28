// 从左至右找出值最小的，记录其索引，将该格与本次检查的起点交换
function selectionSort(array) {

	// 外层循环代表每一轮检查
	// 每一轮检查之初，记住目前的最小值的索引

	for(var i = 0; i < array.length; i++) {
		var lowest_number_index = i;

		// 发起i+1开始的内层循环
		// 逐个检查数组未排序的格子，并更新最小格子的索引

		for(var j = i + 1; j < array.length; j++) {
			if(array[j] < array[lowest_number_index]) {
				lowest_number_index = j;
			}
		}

		// 内层循环结束时得到未排序树值中最小值的索引
		
		if(lowest_number_index != i) {
			var temp = array[i];
			array[i] = array[lowest_number_index];
			array[lowest_number_index] = temp;
		}
	}
	return array;
}