using bot1;
using Discord;
using Discord.Commands;
using Discord.WebSocket;

public class Program
{
    public static Task Main(string[] args)
    {
        return new Program().MainAsync();
    }

    public async Task MainAsync()
    {
        var client = new DiscordSocketClient();
        var logger = new LoggingService();

        await logger.Initialise(client, new CommandService());

        var token = Environment.GetEnvironmentVariable("TOKEN");

        await client.LoginAsync(TokenType.Bot, token);
        await client.StartAsync();

        await Task.Delay(-1);
    }

    private Task Log(LogMessage msg)
    {
        Console.WriteLine(msg.ToString());
        return Task.CompletedTask;
    }
}