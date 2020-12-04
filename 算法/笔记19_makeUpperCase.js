// 法一:O(N)，结束时内存里有两个数组
// function makeUpperCase(array) {
// 	var newArray = [];
// 	for(var i = 0; i < array.length; i++) {
// 		newArray[i] = array[i].toUpperCase();
// 	}
// 	return newArray;
// }

// 法二:不消耗额外空间, O(1),constant speed
// 空间复杂度是根据额外需要的内存空间（辅助空间）来算
function makeUpperCase(array) {
	for(var i = 0; i < array.length; i++) {
		array[i] = array[i].toUpperCase();
	}
	return newArray;
}