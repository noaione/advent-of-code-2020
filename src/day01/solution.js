const utils = require("../utils/utils");

let in_data = utils.readInput("input", true, true);

// Part A
let found = false;
for (let i = 0; i < in_data.length - 1; i++) {
    for (let j = i + 1; j < in_data.length; j++) {
        if (in_data[i] + in_data[j] == 2020) {
            console.log(`Part A: ${in_data[i] * in_data[j]}`);
            found = true;
            break;
        }
    }
    if (found) {
        break;
    }
}

// Part B
found = false;
for (let i = 0; i < in_data.length - 1; i++) {
    for (let j = i + 1; j < in_data.length; j++) {
        for (let k = j + 1; k < in_data.length; k++) {
            if (in_data[i] + in_data[j] + in_data[k] == 2020) {
                console.log(`Part B: ${in_data[i] * in_data[j] * in_data[k]}`);
                found = true;
                break;
            }
        }
        if (found) {
            break;
        }
    }
    if (found) {
        break;
    }
}