namespace Calculator;

internal class Program
{
    static void Main(string[] args)
    {
        string input = "";

        foreach (var s in args)
        {
            input += s;
        }

        foreach (var c in input)
        {
            if (!(new char[] { '/', '*', '+', '-', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0' }).Contains(c))
            {
                Console.WriteLine("you put something weird in :(");
                return;
            }
        }

        string[] numbers = input.Split(new char[] { '/', '*', '+', '-' });
        string[] operators = input.Split(new char[] { '1', '2', '3', '4', '5', '6', '7', '8', '9', '0' });

        operators = operators.Where(val => val != "").ToArray();

        if (numbers.Length < 2)
        {
            Console.WriteLine("u need at least two numbers lol");
            return;
        }
    }
}
