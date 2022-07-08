using System.Reflection;
using Discord;
using Discord.Commands;
using Discord.WebSocket;

namespace bot1;

public class Program
{
    private readonly DiscordSocketClient _client = new();

    private readonly CommandService _commands =
        new(new CommandServiceConfig { CaseSensitiveCommands = false });

    private readonly IServiceProvider services;

    public static Task Main(string[] args)
    {
        return new Program().MainAsync();
    }

    private async Task MainAsync()
    {
        LoggingService logger = new();
        await logger.Initialise(_client, _commands);

        await InitCommands();

        var token = Environment.GetEnvironmentVariable("TOKEN");

        await _client.LoginAsync(TokenType.Bot, token);
        await _client.StartAsync();

        await Task.Delay(-1); //waits infinitely
    }

    private async Task InitCommands()
    {
        await _commands.AddModulesAsync(Assembly.GetEntryAssembly(), services);

        _client.MessageReceived += CommandHandlerAsync;
    }

    private async Task CommandHandlerAsync(SocketMessage arg)
    {
        var msg = arg as SocketUserMessage;

        if (msg == null || msg.Author.IsBot)
            return;

        var pos = 0;

        if (!msg.HasCharPrefix(';', ref pos))
            return;

        var context = new SocketCommandContext(_client, msg);
        var result = await _commands.ExecuteAsync(context, pos, services);

        if (!result.IsSuccess && result.Error != CommandError.UnknownCommand)
            await msg.Channel.SendMessageAsync(result.ErrorReason);
    }
}
