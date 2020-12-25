// 牛顿方法：f(x) = x^2 - c，当f(x) = 0时的解
// f' = 2x
// 得到切线方程和x轴交点的值(c+ t^2)/(2*t)
public class Sqrt
{
	public static void main(String[] args)
	{
		double c = Double.parseDouble(args[0]);
		// ε: 误差范围小于该值，认为精确
		double eps = 1e-15;
		// t: estimate of √c
		double t = c;
		// 从 t = c 作为estimate开始，若t = c/t，则complete
		// 若否，则将t和c/t的平均值(通过切线方程和x轴相交求得)赋值给t
		// while (Math.abs(number - t*t) > err)
		while (Math.abs(t - c/t) > eps * t)
		{
			t = (c/t + t) / 2.0;
		}
		System.out.println(t);
	}
}
