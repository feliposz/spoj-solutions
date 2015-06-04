/*
SPOJ Problem Set (classical)

3442. The last digit

Problem code: LASTDIG




Nestor was doing the work of his math class about three days but he is tired of make operations a lot and he should deliver his task tomorrow. His math’s teacher gives two numbers a and b. The problem consist in find the last digit of the potency of base a and index b. Help Nestor with his problem. You are given two integer numbers: the base a (0 <= a <= 20) and the index b (0 <= b <= 2,147,483,000), a and b both are not 0. You have to find the last digit of a^b.

Input

The first line of input contains an integer t, the number of test cases (t <= 30). t test cases follow. For each test case will appear a and b separated by space.

Output

For each test case output an integer per line representing the result.

Example

Input:
2
3 10
6 2

Output:
9
6
*/

#include <stdio.h>

// http://en.wikipedia.org/wiki/Exponentiation_by_squaring
unsigned int fast_expt(unsigned int x, unsigned int n)
{
    if (n == 0)
        return 1;
    if (n == 1)
        return x;
    if (n % 2 == 0)
        return fast_expt(x*x, n/2);
    else
        return x * fast_expt(x*x, (n-1)/2);
}

// http://en.wikipedia.org/wiki/Modular_exponentiation
int modular_pow(int base, int exponent, int modulus)
{
    int result = 1;
    base = base % modulus;
    while (exponent > 0) {
        if (exponent & 1) { // exponent % 2 == 1
           result = (result * base) % modulus;
        }
        exponent = exponent >> 1; // exponent / 2
        base = (base * base) % modulus;
    }
    return result;
}

int main()
{
    int t, x, a, b;

    scanf("%d", &t);

    while (t-- > 0) {
        scanf("%d %d", &a, &b);
        x = modular_pow(a, b, 10);
        printf("%d\n", x);
    }

    return 0;
}
