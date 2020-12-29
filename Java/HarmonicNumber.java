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
public class HarmonicNumber
{
	public static double harmonic(int n)
	{
		double sum = 0.0;
		for (int i = 1; i <= n; i++) sum += 1.0 / i;
		return sum;
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