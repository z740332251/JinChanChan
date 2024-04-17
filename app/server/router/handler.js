const os = require('os');
const logger = require('../libs/Logger');
const { LOG_LEVEL_TYPE, RESTAPI_ERROR_MESSAGE } = require('../libs/Consts');
const Util = require('../libs/Util');

/**
 * 处理/execsync路由的功能逻辑
 * @param {*} body
 * @param {*} response
 */
async function execsyncHandler(body, response) {
    response.setHeader('Content-Type', 'application/json');
    return response.end(httpResponse, 'utf8');
}

/**
 * 处理/ping路由的功能逻辑
 * @param {*} body
 * @param {*} response
 */
function pingHandler(body, response) {
    response.setHeader('Content-Type', 'application/json');
    try {
        let interfaces = os.networkInterfaces();
        let ip_list = [];
        for (let ifname in interfaces) {
            interfaces[ifname].forEach((iface) => {
                if (!iface.internal && iface.family === 'IPv4') {
                    ip_list.push({
                        name: ifname,
                        address: iface.address,
                    });
                }
            });
        }
        response.end(`{"result":"OK", "ip":${JSON.stringify(ip_list)}}`);
    } catch (error) {
        logger.error(error, LOG_LEVEL_TYPE.ERROR.HTTP_HANDLER);
        response.writeHead(500);
        response.end('server error!');
    }
}

/**
 * 健康检查，直接返回结果
 * @param {*} body
 * @param {*} response
 */
function lbCheck(body, response) {
    response.end();
}

module.exports = {
    execsync: execsyncHandler,
    ping: pingHandler,
};
