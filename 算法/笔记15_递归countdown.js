// 法一：循环
function countdown(number) {
	for(var i = number; i >= 0; i--) {
		console.log(i);
	}
}

// 法二：递归
function countdown2(number) {
	console.log(number);

	// 加条件使不必打印负数
	
	if(number === 0) {
		return;
	} else {
		countdown2(number - 1);
	}
}