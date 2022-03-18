using System;

namespace FizzBuzz
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("welcome to fizzbuzz or something");

            for (int i = 1; i <= 100; i++)
            {
                string outp = i.ToString();

                if (i % 3 == 0 && i % 5 == 0) outp = "FizzBuzz";
                else if (i % 3 == 0) outp = "Fizz";
                else if (i % 5 == 0) outp = "Buzz";

                if (i%25 == 0)
                {
                    Console.WriteLine(outp);
                }
                else
                {
                    Console.Write(outp + " ");
                }
            }
        }
    }
}