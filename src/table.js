/* @docStart
### Table In JavaScript
@docEnd */

// @codeStart

function Table(x) {
    const res = [];
    for (let i = x; i <= x * 10; i += x) {
        res.push(i);
    }
    return res;
}
console.log(Table(5));

// [
//     5, 10, 15, 20, 25,
//    30, 35, 40, 45, 50
//  ]

const table = (x) =>
    Array(10)
        .fill(0)
        .map((v, i) => (1 + i) * x);

console.log(table(9));
// [
//     9, 18, 27, 36, 45,
//    54, 63, 72, 81, 90
//  ]

// @codeEnd
