import java.util.*;
public class Average
{
	public static void main(String[] args)
	{
		double sum = 0.0;
		int n = 0;
		while (! StdIn.isEmpty())
		{
			double value = StdIn.readDouble();
			sum += value;
			n++;
		}
		double average = sum / n;
		StdOut.println("Avg is " + average);
	}
}

