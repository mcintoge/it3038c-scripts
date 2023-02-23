
const os = require('os');
const totalRAM = os.totalmem();
console.log(totalRAM / (1024 * 1024));