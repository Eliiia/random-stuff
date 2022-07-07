using Discord;
using Discord.Commands;
using Discord.WebSocket;

namespace Log;

public class LoggingService
{
    public Task Initialise(DiscordSocketClient client, CommandService command)
    {
        client.Log += LogAsync;
        command.Log += LogAsync;
        return Task.CompletedTask;
    }

    private Task LogAsync(LogMessage message)
    {
        if (message.Exception is CommandException cmdException)
            Console.WriteLine(
                $"[Command/{message.Severity}] {cmdException.Command.Aliases.First()}"
                + $" failed to execute in {cmdException.Context.Channel}");

        else Console.WriteLine($"[General/{message.Severity}] {message}");

        return Task.CompletedTask;
    }
}