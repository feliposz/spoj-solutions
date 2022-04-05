T reverse(T)(T number)
{
	T result = 0;
	while (number > 0)
	{
		result = result * 10 + number % 10;
		number /= 10;
	}
	return result;
}

bool isPalindrome(T)(T number)
{
	return number == reverse(number);
}

void main()
{
	import std.stdio: readf, readln, writefln;
    import std.bigint;
    import std.string: strip;
    import std.conv: to;

	int numCases = to!int(readln().strip());

	foreach (i; 0..numCases)
	{
		auto number = BigInt(readln().strip());
		BigInt test = number + 1;
		while (!isPalindrome(test))
		{
			test++;
		}
		writefln("%s", test);
	}
}