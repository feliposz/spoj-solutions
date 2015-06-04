/*SPOJ Problem Set (classical)
24. Small factorials
Problem code: FCTRL2

You are asked to calculate factorials of some small positive
integers.

Input
An integer t, 1<=t<=100, denoting the number of testcases,
followed by t lines, each containing a single integer n,
1<=n<=100.

Output
For each integer n given at input, display a line with the value
of n!

Example

Sample input:
4
1
2
5
3
Sample output:

1
2
120
6
*/

import java.util.*;
import java.math.*;

class FCTRL2 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int t = sc.nextInt();
		
		while (t-- > 0) {
			int n = sc.nextInt();
			System.out.println(bigFactorial(n));
		}
	}
	
	private static BigInteger bigFactorial(int n) {
		BigInteger result = BigInteger.ONE;
		for (int f = 1; f <= n; f++) {
			result = result.multiply(BigInteger.valueOf(f));
		}
		return result;
	}
}
