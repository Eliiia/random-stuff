using Discord.Commands;

namespace bot1.commands;

public class InfoModule : ModuleBase<SocketCommandContext>
{
    [Command("say")]
    [Summary("Echoes a message.")]
    public Task SayAsync([Remainder] [Summary("The text to echo")] string echo)
    {
        return ReplyAsync(echo);
    }
}
