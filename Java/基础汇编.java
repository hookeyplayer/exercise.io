// find max
public static double max(double[] a) 
{
	//static final field, -1.0 / 0.0
	double max = Double.NEGATIVE_INFINITY; 
	for (int i = 0; i < a.length; i++)
		if (a[i] > max) max = a[i];
	return max;
}

// 点乘
public static double dot(double[] a, double[] b)
{
	double sum = 0.0;
	for (int i = 0; i < a.length; i++)
		sum += a[i] * b[i]; 
	return sum;
}

// 求平均
import java.util.*;
public class Average
{
	public static void main(String[] args)
	{
		double sum = 0.0;
		int n = 0;
		while (! System.in.isEmpty())
		{
			double value = System.in.readDouble();
			sum += value;
			n++;
		}
		double average = sum / n;
		System.out.println("Avg is " + average);
	}
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