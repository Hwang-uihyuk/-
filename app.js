var fs = require('fs')
var input = fs.readFileSync('./input.txt').toString().split('')

if (input === input.reverse().join("")) console.log('1')
else console.log('0')


// 입력값이 : levelsdf 일때 
//split 까지만 쪼개면 ['l', 'e', 'v','e', 'l', 's','d', 'f']
//reverse 하면 ['f', 'd', 's','l', 'e', 'v','e', 'l']
//join 해주면 fdslevel