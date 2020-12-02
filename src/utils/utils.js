const fs = require("fs");

function splitInput(raw_data, parsenum = false) {
    let in_data = [];
    for (let index = 0; index < raw_data.length; index++) {
        let element = raw_data[index];
        if (parsenum) {
            element = parseFloat(element)
        }
        in_data.push(element);
    }
    return in_data;
}

function readInput(path, splitNL = true, parsenum = false) {
    let read_data = fs.readFileSync("input").toString();
    if (splitNL) {
        read_data = splitInput(read_data.split("\n"), parsenum);
    }
    return read_data;
}

function escapeRegExp(string) {
    return string.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
}

module.exports = {
    readInput,
    splitInput,
    escapeRegExp
};