bool isPalindrome(string s)
{
	for (int i = 0; i < s.length / 2; i++)
	{
		if (s[i] != s[s.length - i - 1])
			return false;
	}
	return true;
}

unittest
{
	assert(isPalindrome("aabbaa"));
	assert(isPalindrome("aba"));
	assert(isPalindrome("aa"));
	assert(isPalindrome("a"));
	assert(isPalindrome(""));
	assert(!isPalindrome("abab"));
	assert(!isPalindrome("abb"));
	assert(!isPalindrome("ab"));
	assert(!isPalindrome("ba"));
	assert(!isPalindrome("Aa"));
	assert(!isPalindrome("aa"));
}

void main()
{
	import std.stdio: readln, writefln, writeln;
	import std.string: strip;
	import std.conv: to;

	auto cases = readln().strip();
	auto numCases = to!int(cases.strip);

	while(numCases-- > 0)
	{
		string input = readln().strip();
		writeln(input);
	}
}
