const handle = require('./handler');
const logger = require('../libs/Logger');
const { LOG_LEVEL_TYPE } = require('../libs/Consts');

function route(request, response) {
    // 简易版路由处理，只适用单层路由
    const pathname = request.url.replace(/\//g, '');
    if (typeof handle[pathname] === 'function') {
        let postbody = '';
        request.on('data', function (data) {
            postbody += data;
        });
        request.on('end', function () {
            logger.verbose(postbody, LOG_LEVEL_TYPE.VERBOSE.HTTP_REQUEST_BODY);
            handle[pathname](postbody, response);
        });
        return;
    }

    response.writeHead(404);
    response.end('not found', 'utf8');
}

module.exports = route;
