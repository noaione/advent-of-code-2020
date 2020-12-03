const utils = require("../utils/utils");

let in_data = utils.readInput("input", true);

function walkthrough(input_data, xmove, ymove) {
    let currx, curry, trees;
    currx = curry = trees = 0;
    while (curry < input_data.length - 1) {
        if (input_data[curry][currx % (input_data[0].length - 1)] == "#") {
            trees++;
        }
        currx += xmove;
        curry += ymove;
    }
    return trees;
}

let r3d1, r1d1, r5d1, r7d1, r1d2;
r3d1 = walkthrough(in_data, 3, 1);
r1d1 = walkthrough(in_data, 1, 1);
r5d1 = walkthrough(in_data, 5, 1);
r7d1 = walkthrough(in_data, 7, 1);
r1d2 = walkthrough(in_data, 1, 2);

console.log(`Part A: ${r3d1}`)
console.log(`Part B: ${r3d1 * r1d1 * r5d1 * r7d1 * r1d2}`)
