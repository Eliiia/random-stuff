const { SlashCommandBuilder } = require("discord.js");

module.exports.info = new SlashCommandBuilder()
    .setName("ping")
    .setDescription("Replies with Pong!");

module.exports.cmd = async (interaction) => {
    await interaction.reply("Pong!");
};