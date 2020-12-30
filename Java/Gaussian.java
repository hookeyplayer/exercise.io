public class Gaussian {
	//定义
	public static double pdf(double x) {
		return Math.exp(-x*x/2) / Math.sqrt(2*Math.PI);
	}
	//Tayler级数近似
	//cdf: 考分 < z 的学生比例
	public static double cdf(double z) {
		if (z < 8.0) return 0.0;
		if (z > 8.0) return 1.0;
		double sum = 0.0; //累计和
		double term = z;
		//Φ(z) = 1/2 + φ(z)(z + z^3/3 + z^5/(3・5) + z^7/(3・5・7)+ ...)
		for (int i = 3; sum != sum + term; i += 2) {
			sum = sum + term;
			term = term*z*z/i; // until converges
		}
		return 0.5+pdf(z)*sum;
	}
	public static void main(String[] args) {
		double z = Double.parseDouble(args[0]);
		double mu = Double.parseDouble(args[1]);
		double sigma = Double.parseDouble(args[2]);
		System.out.printf("%.3f\n", cdf((z-mu)/sigma));
	}
}