/* If p > q, gcd of p and q = gcd of q and p % q.
 * gcd of p and q = gcd of q and p􏱃 - q or 
 * gcd of q and p - 2q or 
 * gcd of q and p - 3q 
 */
public class Euclid
{
	// 最大公约数
	public static int gcd(int p, int q) {
		if (q == 0) return p;
		return gcd(q, p % q);
	}
	public static void main(String[] args) {
		int p = Integer.parseInt(args[0]);
		int q = Integer.parseInt(args[1]);
		int divisor = gcd(p, q);
		System.out.println(divisor);
	}
}