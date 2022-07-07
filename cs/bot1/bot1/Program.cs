using System.Reflection;
using Discord;
using Discord.Commands;
using Discord.WebSocket;
using Log;

public class Program
{
    private readonly DiscordSocketClient client = new();

    private readonly CommandService commands =
        new(new CommandServiceConfig
        {
            CaseSensitiveCommands = false
        });

    private readonly IServiceProvider services;

    public static Task Main(string[] args)
    {
        return new Program().MainAsync();
    }

    private async Task MainAsync()
    {
        var logger = new LoggingService();
        await logger.Initialise(client, commands);

        await InitCommands();

        var token = Environment.GetEnvironmentVariable("TOKEN");

        await client.LoginAsync(TokenType.Bot, token);
        await client.StartAsync();

        await Task.Delay(-1); //waits infinitely
    }

    private async Task InitCommands()
    {
        await commands.AddModulesAsync(Assembly.GetEntryAssembly(), services);

        client.MessageReceived += CommandHandlerAsync;
    }

    private async Task CommandHandlerAsync(SocketMessage arg)
    {
        var msg = arg as SocketUserMessage;
        if (msg == null) return;

        if (msg.Author.IsBot) return;

        var pos = 0;

        if (msg.HasCharPrefix(';', ref pos)) return;

        var context = new SocketCommandContext(client, msg);
        var result = await commands.ExecuteAsync(context, pos, services);

        if (!result.IsSuccess && result.Error != CommandError.UnknownCommand)
            await msg.Channel.SendMessageAsync(result.ErrorReason);
    }
}