// Convert a Number to a String!

using System;

class Kata
{
	public static int StringToNumber(String str)
	{
		return Convert.ToInt32(str);
	}

	// Для локального запуска
	static void Main(string[] args)
	{
		string test = "123";
		Console.WriteLine(StringToNumber(test));
		Console.ReadKey();
	}
}