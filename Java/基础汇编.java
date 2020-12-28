public class HelloWorld
{
	public static void main(String[] args)
	{
		System.out.print("Hello, ");
		System.out.print(args[0]);
		System.out.print(".Good morning.");
	}
}

public class Flip
{
	public static void main(String[] args)
	{if (Math.random() < 0.5) 
		System.out.println("Head");
	else 
		System.out.println("Tail");

	}
}

// Math.round(3.14159)
// double exp(double b)
// double pow(double a, double b)

// char <-> double/int
int Integer.parseInt(String s)
double Double.parseDouble(String s)
long Long.parseLong(String s)

// leapyear verification(本应另开一个文件)
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
