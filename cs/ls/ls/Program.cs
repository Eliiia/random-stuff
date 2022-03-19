using System.IO;

if (args.Length == 0)
{
    Console.WriteLine("You need to actually give me something to look at smh\n");
    System.Environment.Exit(0); // wrong code but whatever
}

if (Directory.Exists(args[0]))
{
    // if file
    
    // else (if directory)
    
    // temporarily:
    int i = 0;

    Console.ForegroundColor = ConsoleColor.DarkGreen;
    // make bold
    string[] subdirs = Directory.GetDirectories(args[0]);
    foreach (string dir in subdirs)
    {
        if (i == 5) 
        { 
            Console.WriteLine(dir);
            i = 0;
        }
        else Console.Write(dir + "\t");
        i++;
    }

    Console.ForegroundColor = ConsoleColor.Green;
    // get rid of boldness
    string[] fileEntries = Directory.GetFiles(args[0]);
    foreach (string fileName in fileEntries)
    {
        if (i == 5) 
        { 
            Console.WriteLine(fileName);
            i = 0;
        }
        else Console.Write(fileName + "\t");
        i++;
    }
}

Console.ResetColor();