
//js에 내장된 패키지 http를 불러옴.
const http = require('http');

function handleRequest(request,response){
    // /domain address
    if (request.url ==='/currentTime'){
        response.statusCode=200;
        response.end('<h1>'+ new Date().toISOString() +'</h1>')
    }else{   
    //성공 num = 200, error = 404 etc...
    response.statusCode=200;
    //response 할 준비가 end
    response.end('<h1>html code,file</h1>')
    }

}
//server 객체 생성.
const server = http.createServer(handleRequest);

const portNum = 3000;
//client의 요청을 기다림. 
server.listen(portNum);

/*
    EntryPoint
    port : default 80(암호화 x code), 443(암호화 코드)

*/