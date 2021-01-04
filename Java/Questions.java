import java.util.Scanner;
public class Questions {
	public static int binarySearch(int low, int high) {
		if (high - low == 1) return low;
		int mid = low + (high - low) / 2;
		System.out.print("≥ " + mid + "? ");
		//input
		Scanner n = new Scanner(System.in);
        boolean bn = n.nextBoolean();
		if (bn)
			return  binarySearch(mid, high);
		else
			return binarySearch(low, mid);
	}
	public static void main(String[] args) {
		int k = Integer.parseInt(args[0]);
		int n = (int) Math.pow(2, k);
		System.out.print("Thinkof number ");
		System.out.println("between 0 and " + (n-1));
		int guess = binarySearch(0, n);
		System.out.println("Your number is" + guess);
	}
}