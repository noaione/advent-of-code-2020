const utils = require("../utils/utils");

let in_data = utils.readInput("input", true);

let remapped_data = [];
for (let index = 0; index < in_data.length; index++) {
    let element = in_data[index];
    let [policy, passwd] = element.split(": ");
    let [rangenum, code] = policy.split(" ");
    let [start, end] = rangenum.split("-");
    remapped_data.push({
        code: code,
        pass: passwd.trimRight(),
        s: parseInt(start),
        e: parseInt(end)
    });
}

// Part A
let valid_a = 0;
let valid_b = 0;
remapped_data.forEach((data) => {
    let total_char = data.pass.length;
    let total_char_rep = data.pass.replace(new RegExp(utils.escapeRegExp(data.code), "g"), "").length;
    let diff = total_char - total_char_rep;
    let fn_val = data.pass.charAt(data.s - 1) == data.code;
    let ln_val = data.pass.charAt(data.e - 1) == data.code;
    if (diff >= data.s && diff <= data.e) {
        valid_a++;
    }
    if (fn_val && !ln_val) {
        valid_b++;
    } else if (ln_val && !fn_val) {
        valid_b++;
    }
})

console.log(`Part A: ${valid_a}`);
console.log(`Part B: ${valid_b}`);
