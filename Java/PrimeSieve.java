// import java.util.*;
// import static net.mindview.util.Print.*;
// Random rand = new Random(47);
// /* choose from 1 to 100 */
// j = rand.nextInt(100) + 1; 
// k = rand.nextFloat();
public class PrimeSieve
{
	public static void main(String[] args)
	{
		int n = Integer.parseInt(args[0]);
		/* boolean array 记录哪些是质数 */
		boolean[] isPrime = new boolean[n+1];
		for (int i = 2; i <= n; i++)
			isPrime[i] = true;
		for (int i = 2; i <= n/i; i++)
		{
			if (isPrime[i])
			{
				for (int j = i; j <= n/i; j++)
					isPrime[i*j] = false;
			}
		}
		int primes = 0;
		for (int i = 2; i <= n; i++)
			if (isPrime[i]) primes++;
		System.out.println(primes);
	}
}