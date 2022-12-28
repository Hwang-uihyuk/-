// 일단 node js가 있어야 된다.
// 터미널에서 node -v로 확인하기.


// .문제 1000번 A+B


var fs = require('fs');
// 파일을 읽어오기 위해 Node.js의 built-in file system
// module fs 사용하기.

var input = fs.readFileSync('./test.txt').toString().split(' ');
// input을 읽어봐 변수로 선언 & 할당 Array로 저장된다.

var a = parseInt(input[0]);
// input에서 지정한 value를 읽어와 다른 변수로 선언하고 활용한다.
var b = parseInt(input[1]);
// toString메소드로 지금은 string이기 때문에, parseInt로 숫자로 형태변환을 해준다.
console.log(a + b);


//실행방법
// terminal에서 node test.js 입력..!