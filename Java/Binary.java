// 原理：用PowersOfTwo加总，分解一个数
public class Binary
{
	public static void main(String[] args)
	{
		int n = Integer.parseInt(args[0]);
		int mult = 1;
		// 找到单个最大的秤，其重量不会超过目标值
		while (mult <= n/2)
			mult *= 2;
		// decreasing order
		while (mult > 0)
		{
			// whether lighter， if so, remove the weight
			// if not, leave the weight and try next one
			// each weight corresponds to a bit
			if (n < mult) {System.out.print(0);}
			else {System.out.print(1); n -= mult;}
			mult /= 2;
		}
		System.out.println();
	}
}