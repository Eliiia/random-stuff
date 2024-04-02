// yes i know this is in the python folder
// this was (is?) a temporary solution
// thanks wren

const data = require("./out.json");

const outdata = Object.entries(data).sort(([,a],[,b]) => a-b)
// Object.entries(data) splits each key/value into separate arrays within one
// e.g. [["a", 1], ["b", 12], ["c", 3]]
// .sort() sorts
// (([,a],[,b]) => a-b) function:
// - gets two values
// - checks whether they're in the right order
// - returns boolean which tells sort() whether to change their order
// - this function is called repeatedly
// also:
// - [,a] and [,b] tell it to disregard the key and only store the value

console.log(outdata)