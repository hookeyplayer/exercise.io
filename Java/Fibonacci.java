// 1. TopDown DP: store or cache subproblems
public class TopDownFibonacci {
	// f是cached values
	private static long[] f = new long[30];
	
	public static long fibonacci(int n) {
		if (n == 0) return 0;
		if (n == 1) return 1;
		if (f[n] > 0) return f[n]; // 返回cached value如果之前被算过
		f[n] = fibonacci(n-1) + fibonacci(n-2); // 计算并cache
		return f[n];
	}
}

// 2. BottomUp DP: 从最简单开始compute all subproblems
public class TopDownFibonacci {
	public static long fibonacci(int n) {
	long[] f = new long[n+1];
	f[0] = 0;
	f[1] = 1;
	for (int i = 2; i <= n; i++) 
		f[i] = f[i-1] + f[i-2];
	return f[n];
	}
	
}
