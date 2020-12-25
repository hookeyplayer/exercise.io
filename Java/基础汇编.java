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

// Math.random() // [0,1)
// Math.round(3.14159)
// double exp(double b)
// double pow(double a, double b)
// print(double E)
// double PI 
// double sin(double theta) // cos(),tan()

// casting to get random integer
public class RandomInt
{
	public static void main(String[] args)
	{
		int n = Integer.parseInt(args[0]);
		double r = Math.random();
		int value = (int) (n * r); // cast
		System.out.println(value);
	}
}

// char <-> double/int
int Integer.parseInt(String s)
double Double.parseDouble(String s)
long Long.parseLong(String s)

public class Ruler
{
	public static void main(String[] args)
	{
		// String a = "1";
		// int b = 3;
		// String c = a + b;
		// System.out.print(a + "+" + b + "=" + c);
		// Integer.parseInt("123") 字符串转数字
		double b = Double.parseDouble(args[0]);
		double c = Double.parseDouble(args[1]);
		double discriminant = b*b - 4.0*c;
		double d = Math.sqrt(discriminant);
		System.out.println((-b + d) / 2.0);
		System.out.println((-b - d) / 2.0);
	}
}

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
