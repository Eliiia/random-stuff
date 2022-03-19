
if (args[0].Length >= 10)
{
    string x = "";
    
    for (int i=0; i<args[0].Length; i++)
    {
        if (i > 10)
        {
            x += Char.ToUpper(args[0][i]);
        }
        else x += args[0][i];
    }
    
    Console.WriteLine(x);
}
else
{
    char[] arr = args[0].ToCharArray();
    arr[0] = '$';
    arr[^1] = '@';

    string x = new string(arr);
    
    Console.WriteLine(x);
}