//拼接url
var crypto = require('crypto'); //引入cypto模块 提供通用的加密和哈希算法
var appId = 'example';
var appId = '5a4adf47';//leiqiao账号的
// var appId = '5a61a970';//iflytek账号的 
 var deviceId = '12312';
 var appKey = '88bb5bcee9bf475fa852018305dd1dd3';//leiqiao账号的
// var appKey = '6c62000baaa5496492f34e142c6eebdb';//iflytek账号的 
var timestamp = Date.now();//时间戳
var md5 = crypto.createHash('md5');//加密方式
md5.update(appId+appKey+timestamp);
var token = md5.digest('hex');//加密的编码方式
var date = '12-11';
var url = 'http://content.xfyun.cn/v1/history/today?timestamp='+timestamp+'&appId='+appId+'&token='+token+'&deviceId='+deviceId+'&date='+date;
console.log(url);//打印输出url