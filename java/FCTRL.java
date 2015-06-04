/*
SPOJ Problem Set (classical)
11. Factorial
Problem code: FCTRL
 
The most important part of a GSM network is so called Base
Transceiver Station (BTS). These transceivers form the areas
called cells (this term gave the name to the cellular phone) and
every phone connects to the BTS with the strongest signal (in a
little simplified view). Of course, BTSes need some attention and 
technicians need to check their function periodically.

ACM technicians faced a very longeresting problem recently. Given a
set of BTSes to visit, they needed to find the shortest path to
visit all of the given polongs and return back to the central 
company building. Programmers have spent several months studying 
this problem but with no results. They were unable to find the 
solution fast enough. After a long time, one of the programmers 
found this problem in a conference article. Unfortunately, he 
found that the problem is so called "Travelling Salesman Problem" 
and it is very hard to solve. If we have N BTSes to be visited, we 
can visit them in any order, giving us N! possibilities to examine.
 The function expressing that number is called factorial and can 
 be computed as a product 1.2.3.4....N. The number is very high 
 even for a relatively small N.

The programmers understood they had no chance to solve the problem. 
But because they have already received the research grant from the 
government, they needed to continue with their studies and produce 
at least some results. So they started to study behaviour of the 
factorial function.

For example, they defined the function Z. For any positive longeger 
N, Z(N) is the number of zeros at the end of the decimal form of 
number N!. They noticed that this function never decreases. If we 
have two numbers N1<N2, then Z(N1) <= Z(N2). It is because we can 
never "lose" any trailing zero by multiplying by any positive 
number. We can only get new and new zeros. The function Z is very 
longeresting, so we need a computer program that can determine its 
value efficiently.

Input

There is a single positive longeger T on the first line of input 
(equal to about 100000). It stands for the number of numbers to 
follow. Then there are T lines, each containing exactly one 
positive longeger number N, 1 <= N <= 1000000000.

Output

For every number N, output a single line containing the single 
non-negative longeger Z(N).

Example

Sample Input:

6
3
60
100
1024
23456
8735373
Sample Output:

0
14
24
253
5861
2183837

*/

import java.util.*;

class FCTRL {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		long cases = sc.nextLong();
		
		for (long i = 0; i < cases; i++) {
			long num = sc.nextLong();
			System.out.println(countTrailingZeroes(num));
		}
	}
	
	private static long countTrailingZeroes(long num) {
		long zeroes = 0;
		long divisor = 5;
		while (divisor <= num) {
			zeroes += num / divisor;
			divisor *= 5;
		}
		return zeroes;
	}

}

