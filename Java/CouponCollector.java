// public class CouponCollector {
// 	public static void main(String[] args) {
// 		int n = Integer.parseInt(args[0]);
// 		boolean[] isCollected = new boolean[n];
// 		int count = 0;
// 		int distinct = 0; 
// 		while (distinct < n) {
// 			int r = (int) (Math.random()*n);
// 			count ++;
// 			if (!isCollected[r]) {
// 				distinct++;
// 				isCollected[r] = true;
// 			}
// 		}
// 	}
// 	System.out.println(count);
// }

public class CouponCollector {
	//抽取
	public static int getCoupon(int n) {
		return (int) (Math.random()*n);
	}

	public static int collectCoupons(int n) {
		boolean[] isCollected = new boolean[n];
		int count = 0;
		int distinct = 0; 
		while (distinct < n) {
			int r = getCoupon(n);
			count ++;
			if (!isCollected[r]) {
				distinct++;
				isCollected[r] = true;
			}	
		}
		return count;
	}
	public static void main(String[] args) {
		int n = Integer.parseInt(args[0]);
		int count = collectCoupons(n);
		System.out.println(count);
	}
	
}