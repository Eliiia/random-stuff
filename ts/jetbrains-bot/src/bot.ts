import { Client } from "discord.js";
import { lol } from "./moment";

const client = new Client({ intents:  513 });

client.on('ready', () => {
    console.log(`Logged in as ${client.user.tag}!`);
});

client.on('messageCreate', msg => {
    if (msg.content === 'ping') {
        msg.reply(lol());
    }
});

client.login('OTQwMzIzMjc0NDkwMDAzNTQ4.YgFuSw.nkbSbYaOVVPAT-NDzsbBPtGEvZA');