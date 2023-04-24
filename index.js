const addon = require('./build/Release/addon');


const fn = (msg) => {
	console.log(msg);
}
console.log(addon(fn));