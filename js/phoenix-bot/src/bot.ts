"use strict";

import { Client } from "@amelix/phoenix.js"

const bot = new /*Phoenix.*/Client("5e-GGL-zH6LUDTlISUjl01MUr9zoaOEWjq4kp58rLViPA_h-Z4cy2x_qFeeGT2RIHtjTBRdQ0RotDC5W")

bot.on("ready", () => {
    console.log(`Logged in as ${bot.user.username}`)
})

bot.on("message", message => {
    if(message.content === "ping") {
        message.channel.send("pong lmao")
    }
})