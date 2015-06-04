/*
SPOJ Problem Set (classical)
2. Prime Generator
Problem code: PRIME1

Peter wants to generate some prime numbers for his cryptosystem.
Help him! Your task is to generate all prime numbers between two
given numbers!

Input:
The input begins with the number t of test cases in a single
line (t<=10). In each of the next t lines there are two numbers
m and n (1 <= m <= n <= 1000000000, n-m<=100000) separated by a
space.

Output:
For every test case print all prime numbers p such that
m <= p <= n, one number per line, test cases separated by an
empty line.

Example

Input:
2
1 10
3 5

Output:
2
3
5
7

3
5
*/

import java.util.*;

class PRIME1 {

	// enough, since 37813 is the 3500th prime and 37813^2 > 1000000000
	private static final int NPRIMES = 3500;

	private static int[] primes = new int[NPRIMES];

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		long start = System.currentTimeMillis();
		
		generateSmallPrimes();
		System.err.println("Largest: " + primes[primes.length - 1]);
		System.err.println("Time 1 = " + (System.currentTimeMillis() - start));
		
		int cases = sc.nextInt();
		for (int i = 0; i < cases; i++) {
			if (i > 0)
				System.out.println("");
			int m = sc.nextInt();
			int n = sc.nextInt();
			printPrimes(m, n);
		}
		
		System.err.println("Time 2 = " + (System.currentTimeMillis() - start));
	
	}
	
	private static void printPrimes(int m, int n) {

		// Print small primes first
		if (m <= primes[primes.length - 1]) {
			for (int i = 0; i < primes.length; i++) {
				if (primes[i] > n)
					return;
				if (primes[i] >= m)
					System.out.println(primes[i]);
			}
			
			// begin printing large primes after last small prime
			m = primes[primes.length - 1] + 2;
		}
		
		if (m % 2 == 0) // check only odds
			m++;
	
		// Now print the larger primes checking againts the smaller
		for (; m <= n; m += 2) {
			if (isLargePrime(m))
				System.out.println(m);
		}
	}
	
	private static boolean isLargePrime(int n) {
		for (int i = 0; i < primes.length; i++) {
			if (primes[i] * primes[i] > n) // TODO: Calculating sqrt(n) once should be faster...
				break;
			if (n % primes[i] == 0)
				return false;
		}
		return true;
	}
	
	private static void generateSmallPrimes() {
		// should probably use a sieve...
		// but this is fast enough for not too many primes	
		primes[0] = 2;
		int i = 1;
		int n = 3;
		while (i < primes.length) {
			if (isPrime(n))
				primes[i++] = n;
			n += 2;
		}
	}

	private static boolean isPrime(int n)
	{
		int r, f;
		
		if (n == 1)
			return false;
		else if (n < 4)
			return true;  // 2 and 3 are prime
		else if (n % 2 == 0)
			return false;
		else if (n < 9)
			return true;  // 4, 6 and 8 have been excluded
		else if (n % 3 == 0)
			return false;
		else {
			r = (int)Math.floor(Math.sqrt(n));  // r * r <= n
			f = 5;	
			while (f <= r) {
				if (n % f == 0)
				   return false;
				else if (n % (f + 2) == 0)
				   return false;
				f = f + 6;
			}
			return true;
		}
	}	
}
