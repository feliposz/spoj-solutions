void main()
{
	import std.stdio : readf, writefln;
	import core.stdc.stdio: fflush, stdout;
	while(true)
	{
		int number;
		readf(" %d", &number);
		writefln("%d", number);
		fflush(stdout);
		if (number == 42)
		{
			break;
		}
	}
}