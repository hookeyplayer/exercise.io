// public class HarmonicNumber
// {
// 	public static void main(String[] args)
// 	{
// 		int n = Integer.parseInt(args[0]);
// 		double sum = 0.0;
// 		for (int i = 1; i <= n; i++) sum += 1.0 / i;
// 		System.out.println(sum);
// 	}
// }

//combination of module as whole using main() & recursion
public class HarmonicNumber
{
// 	public static double harmonic(int n)
// 	{
// 		double sum = 0.0;
// 		for (int i = 1; i <= n; i++) sum += 1.0 / i;
// 		return sum;
// 	}
	
	public static double harmonic(int n)
	{
		if (n == 1) return 1.0;
		return harmonic(n-1) + 1.0/n;
	}
	
	public static void main(String[] args)
	{
		for (int i = 0; i < args.length; i++)
		{
			int arg = Integer.parseInt(args[i]);
			double value = harmonic(arg);
			System.out.println(value);
		}
	}
}
