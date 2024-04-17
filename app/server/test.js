const { createServer } = require('http');

const HOST = 'localhost';
const PORT = '8080';

const server = createServer((req, resp) => {
  // the first param is status code it returns
  // and the second param is response header info
  resp.writeHead(200, { 'Content-Type': 'text/plain' });

  console.log('server is working...');

  // call end method to tell server that the request has been fulfilled
  resp.end('hello nodejs http server');
});

server.listen(PORT, HOST, (error) => {
  if (error) {
    console.log('Something wrong: ', error);
    return;
  }

  console.log(`server is listening on http://${HOST}:${PORT} ...`);
});

作者：草帽Plasticine
链接：https://juejin.cn/post/7109744726495985677
来源：稀土掘金
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。