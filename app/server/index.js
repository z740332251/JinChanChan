const http = require("http");
const route = require('./router/router');
const logger = require('./libs/Logger');
const { LOG_LEVEL_TYPE } = require('./libs/Consts');
const serverConfig = require('./config').server;

// http server 3000 监听来自php的3000 post 请求
const httpServerPort = serverConfig.http_server_port || 3000;
const server = http.createServer(function(request, response) {
    route(request, response);
});
server.listen(httpServerPort, function() {
    logger.info(
        `Server is listening on port ${httpServerPort}`,
        LOG_LEVEL_TYPE.INFO.HTTP_SERVER,
    );
    console.log(`Server is listening on port ${httpServerPort}`);
});