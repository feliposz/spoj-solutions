int reverse(int number)
{
	int result = 0;
	while (number > 0)
	{
		result = result * 10 + number % 10;
		number /= 10;
	}
	return result;
}

bool isPalindrome(int number)
{
	return number == reverse(number);
}

void main()
{
	import std.stdio: readf, writefln;

	int numCases;
	readf(" %d", &numCases);

	foreach (i; 0..numCases)
	{
		int number;
		readf(" %d", &number);
		int test = number + 1;
		while (!isPalindrome(test))
		{
			test++;
		}
		writefln("%d", test);
	}
}