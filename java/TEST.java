/*
SPOJ Problem Set (classical)
1. Life, the Universe, and Everything
Problem code: TEST

Your program is to use the brute-force approach in order to find the
Answer to Life, the Universe, and Everything. More precisely...
rewrite small numbers from input to output. Stop processing input after
reading in the number 42. All numbers at input are integers of one or
two digits.

Example

Input:
1
2
88
42
99

Output:
1
2
88
*/

import java.util.*;

class TEST {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n;
		
		while (true) {
			n = sc.nextInt();
			if (n == 42)
				break;
			System.out.println(n);
		}
	}
}