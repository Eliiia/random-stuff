import * as http from "http"

http.createServer((req:any, res:any) => {
    res.setHeader("content-type", "application/json")
    res.end(["oki", "doki", "boomer"])
    // https://www.youtube.com/watch?v=dWNvlyycWzQ
}).listen(8080)

console.log("started ig")