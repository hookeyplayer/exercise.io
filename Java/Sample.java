// args: m, n
public class Sample
{
	public static void main(String[] args)
	{
		int m = Integer.parseInt(args[0]);
		int n = Integer.parseInt(args[1]);
		int[] perm = new int [n];
		for (int j = 0; j < n; j++)
			perm[j] = j;
		for (int i = 0; i < m; i++)
		{
			// shuffling
			int r = i + (int) (Math.random() * (n-i));
			int t = perm[r];
			perm[r] = perm[i];
			perm[i] = t;
		}
		for (int i = 0; i < m; i++)
			System.out.print(perm[i] + " ");
		System.out.println();
	}
}