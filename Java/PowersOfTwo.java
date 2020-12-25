// public class PowersOfTwo
// {
// 	public static void main(String[] args)
// 	{
// 		int n = Integer.parseInt(args[0]);
// 		int i = 0;
// 		int mult = 1;
// 		while (i <= n)
// 		{
// 			System.out.println(i + "as power, result is " + mult);
// 			i = i + 1;
// 			mult *= 2;
// 		}
// 	}
// }

// 不超过给定数的最大的power：
// int mult = 1;
// while (power <= n/2)
// {
// 	mult = mult * 2;
// 
public class PowersOfTwo
{
	public static void main(String[] args)
	{
		int n = Integer.parseInt(args[0]);
		int mult = 1;
		for (int i = 0; i <= n; i++)
		{
			System.out.println(i + " , " + mult);
			mult += mult; // same, mult = mult * 2
		}
	}
} 
