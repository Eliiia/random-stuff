const fs = require("fs");

var showdown  = require('showdown'),
    converter = new showdown.Converter(),
    text      = fs.readFileSync("./testfile.md").toString(),
    html      = converter.makeHtml(text);


console.log(html)