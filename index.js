const testAddon = require('./addon');

const helloWords = testAddon.hello();

console.log(helloWords);

const sumFromCpp = testAddon.add(2, 1);

console.log(sumFromCpp);