// 点乘
public static double dot(double[] a, double[] b)
{
	double sum = 0.0;
	for (int i = 0; i < a.length; i++)
		sum += a[i] * b[i]; 
	return sum;
}

// exchange
public static void exchange(String[] a, int i, int j)
{
	String temp = a[i];
	a[i] = a[j];
	a[j] = temp;
}

// read matrix in row-major order
public static double[][] readDouble2D()
{
	int m = System.in.readInt();
	int n = System.in.readInt();
	double [][] a = new double[m][n];
	for (int i = 0; i < m; i++)
		for (int j = 0; j < n; j++)
			a[i][j] = System.in.readDouble();
	return a;

}
// combination of a few
public class Stats {
	//max
	public static double max(double[] a) {
		//static final field, -1.0 / 0.0
		double max = Double.NEGATIVE_INFINITY; 
		for (int i = 0; i < a.length; i++)
			if (a[i] > max) max = a[i];
		return max;
	}

	//average
	import java.util.*;
	public static double mean(double[] a) {
		double sum = 0.0;
		for (int i = 0; i < a.length; i++)
			sum += a[i];
		return sum / a.length;
	}

	//variance
	public static double var(double[] a) {
		double avg = mean(a);
		double sum = 0.0;
		for (int i = 0; i < a.length; i++)
			sum += (a[i] - avg) * (a[i] - avg);
		return sum / (a.length - 1);
	}
	 // standard deviation
	public static double stddev(double[] a) 
	{
		return Math.sqrt(var(a));
	}

	public static void main(String[] args) {
		/* I/O */
	}
}

//Others
public class Flip
{
	public static void main(String[] args)
	{if (Math.random() < 0.5) 
		System.out.println("Head");
	else 
		System.out.println("Tail");

	}
}

public class isLeapYear
{
	public static void main(String[] args)
	{
		int year = Integer.parseInt(args[0]);
		boolean isLeapYear;
		isLeapYear = (year % 4 == 0);
		isLeapYear = isLeapYear && (year % 100 != 0);
		isLeapYear = isLeapYear || (year % 400 == 0);
		System.out.println(isLeapYear);
	}
}
