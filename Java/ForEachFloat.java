import java.util.*;
public class ForEachFloat 
{
	public static void main(String[] args)
	{
		Random rand = new Random(47);
		float f[] = new float[10];
		for (int i = 0; i < 10; i++) f[i] = rand.nextFloat();
		// foreach用法，将每一个f的元素赋值给x
		// 任何返回一个数组的方法都可以用foreach
		for (float x : f) System.out.println(x);
	}
}

// for (int i : range(10)) printnb(i + " ")
// for (char c : "An African Swallow".toCharArray()) System.out.print(c + " ")
