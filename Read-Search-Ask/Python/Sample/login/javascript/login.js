$(function () {
    init();
});
var timeout = null;
var nowTime = null;
var timer = null;
var timerClock = null;
var timercodeClock = null;
//var uuidInfo = uuid();
var uuidInfo = getuuidInfo()
var qrcodeCreateInfo = null;
var loginType = "101";
var dCode = false;
var wait = 1000;
var failcount = 0;// 请求失败次数 轮询二维码
function init() {
 	var date=new Date();
    var formattedDate=""+date.getFullYear()+(date.getMonth()+1)+date.getDate()+date.getHours();
 	var passwordshow = document.getElementById("password")
 	var getKeyword = $('#getKeyword')//验证码登录（获取验证码）
 	var getCode = $('#getCode')//密码登录（获取验证码）
	var loginbyImg = $('.ifly-login-scanImg')//二维码登录
  	var loginbyPassword  = $('.ifly-loginbox-input')//密码登录
  	var loginbyCheckword = $('.ifly-login-checkword')//验证码登录	
	document.getElementById("qrcode").innerHTML = "";
	if(sessionStorage.getItem('loginType') && sessionStorage.getItem('loginType') === '100' ){
		changeLoginbyCheckword()
	} else if (sessionStorage.getItem('loginType') && sessionStorage.getItem('loginType') === '101' ) {
		changeLoginbyPassword()	
	} else if (sessionStorage.getItem('loginType') && sessionStorage.getItem('loginType') === '102' ) {
		changeScanlogin()	
	} else {
		changeLoginbyPassword()
		
	}
    $("#bgContainer").css("background-image","url(https://in.iflytek.com/static/loginImage/ifly-img.png?v="+formattedDate+")");
    if ($("#hasErrors").html()) {
        iflyLogin.ck($("#hasErrors").html(), 'icon-warning');
        $("#hasErrors").html("");
    }
    if($("#divConfirm").is(":visible")==true){
        changeCode();
    }
	// 密码的显示和隐藏
	$('.xiaoyanjing').on('click', function () {
		if ($(this).hasClass('active')) {
	      $(this).removeClass('active')
	      passwordshow.setAttribute('type', 'password')
	    } else {
	      $(this).addClass('active')
	      passwordshow.setAttribute('type', 'text')
	    }  
	})
	//获取验证码
	getCode.on('click', function () {
        $(this).prop('disabled', true).css('color', '#ccc')
        getVCode(1, getCode, timercodeClock)
    })
	getKeyword.on('click', function () {
        $(this).prop('disabled', true).css('color', '#ccc')
        getVCode(0, getKeyword, timerClock)
    })
  	function getVCode(type, el, time) { // 1密码登录界面的获取验证码  0验证码登录界面的获取验证码
        var Codetimer
        var checkwordtimer
	    getcheckword(function (res) {
            setTimeout( function () {
                if (res.tips) {
                    $('#question-tipone').css('display','block').attr('title',res.tips)
                    $('#question-tiptwo').css('display','block').attr('title',res.tips)
                }
            },1000);
            if (type) {
                Codetimer = res.countdown
                $('.checktip1').css('display','block').text(res.text)
            } else {
                checkwordtimer = res.countdown
                $('.checktip').css('display','block').text(res.text)
            }
            time = setInterval(function () {
                if (Codetimer > 1) {
                    Codetimer--;
                    el.text(Codetimer + '秒后重新获取').css('color', '#ccc').attr("disabled", true)
                } else if (checkwordtimer > 1) {
                    checkwordtimer--;
                    el.text(checkwordtimer + '秒后重新获取').css('color', '#ccc').attr("disabled", true)
                } else {
                    el.text("获取验证码");
                    el.css('color', '#4080FF')
                    el.attr("disabled", false)
                    $('#question-tipone').css('display','none')
                    $('#question-tiptwo').css('display','none')
                    clearInterval(time)
                }
            }, wait);
        })
	  }
	// 切换成二维码登录
	// login-tip  login-tip-checkword login-byscanImg  login-byscanImg-incheckword 
	$('.login-tip').on("click", function () {changeScanlogin()})
	$('.login-tip-checkword').on("click", function () {changeScanlogin()})
	$('.login-byscanImg').on("click", function () {changeScanlogin()})
	$('.login-byscanImg-incheckword').on("click", function () {changeScanlogin()})
    //$('.change-scanImg-login').on("click", function () {changeScanlogin()})
    //$('.login-byscanImg-incheckword').on('click', function () {changeScanlogin()})
    function changeScanlogin () {
        clearInterval(timer)
        loginType = '102'
        uuidInfo = uuid()
		loginbyImg.addClass('active')
      	loginbyCheckword.removeClass('active')
      	loginbyPassword.removeClass('active')
        $('.ifly-loginbox-btn').css('display','none')
      	$('#qrcode-invaild').css('display','none')
		
        document.getElementById("qrcode").innerHTML = "";
        getqrcodeCreate(function (res) {
            qrcodeRender('qrcode', res)
            qrcodePolling($('#qrcode'), res)
        })
		sessionStorage.setItem('loginType', loginType)
		sessionStorage.setItem('uuidInfo',uuidInfo)
		
    }
	// 切换成验证码登录
    $('.ifly-login-by-checkkeyword').on("click", function () { changeLoginbyCheckword() })
 	function changeLoginbyCheckword() {
		if($("#username").val()){
			$('#username1').val($("#username").val())
		}
	 	loginType = '100'
        $('.checktip')[0].style.display = 'none'
        $("#password").val('');
        $("#checkword").val('');
        loginbyPassword.removeClass('active')
      	loginbyCheckword.addClass('active')
      	loginbyImg.removeClass('active')
		$('.ifly-loginbox-btn').css('display','block')
		sessionStorage.setItem('loginType', loginType)
		sessionStorage.setItem('uuidInfo',uuidInfo)
	}
	// 切换成密码登录
	// login-bypassword login-tip-scanImg
    $('.ifly-login-by-password').on('click', function () { changeLoginbyPassword() })
	$('.login-bypassword').on('click', function () { changeLoginbyPassword() })
    $('.login-tip-scanImg').on('click', function () { changeLoginbyPassword() })
    function changeLoginbyPassword() {
		if($("#username1").val()){
			$('#username').val($("#username1").val())
		}
        loginType = '101'
		loginbyPassword.addClass('active')
      	loginbyCheckword.removeClass('active')
      	loginbyImg.removeClass('active')
        $('.ifly-loginbox-btn').css('display','block')
		sessionStorage.setItem('loginType', loginType)
		sessionStorage.setItem('uuidInfo',uuidInfo)
    }
	// 点击刷新二维码
    $('.needRefresh').on('click', Refreshqrcode)
    $('#qrcode-invaild').on('click', Refreshqrcode)
    function Refreshqrcode () {
        clearInterval(timer)
        document.getElementById("qrcode").innerHTML = "";
        $('#qrcode-invaild')[0].style.display="none"
        getqrcodeCreate(function (res) {
            qrcodeRender('qrcode', res)
            qrcodePolling($('.qrcode'), res)
        })
    }

}

// 发送请求到服务器之前校验
function checkLogin() {
	var passwordshow = document.getElementById("password")
	$('.xiaoyanjing').removeClass('active')
	passwordshow.setAttribute('type', 'password')
    var str = ':' + loginType + ':' + window.BASE64.encoder(navigator.appVersion) + ':' + window.BASE64.encoder(uuidInfo)
    // 扫码登录方式
    if(dCode) {
        $("#username").val(qrcodeCreateInfo.account)
        var key = window.BASE64.encoder(window.BASE64.encoder(qrcodeCreateInfo.token)+ ':' + window.BASE64.encoder(qrcodeCreateInfo.ticket))+str
        var base64 = window.BASE64.encoder(key)
        $("#password").val(base64);
        return true
    } else {
        var username = trim($("#username").val());
        var password = trim($("#password").val());
        var username1 = trim($("#username1").val());
        var checkword = trim($("#checkword").val());
        var passwordPack = trim($("#password").val());
        // 账号密码登录 loginType 101
        if (loginType === '101') {
            if (username == "") {
                iflyLogin.ck("域账号不能为空", 'icon-warning');
                $("#username").focus()
                return false;
            }
            if (password == "") {
                iflyLogin.ck("密码不能为空", 'icon-warning');
                $("#password").focus()
                return false;
            }
            // 是否有验证码
            if ($("#divConfirm").is(":visible") == true) {
                var codeisneed = $("#code").val()
                if (codeisneed == "") {
                    iflyLogin.ck("验证码不能为空", 'icon-warning');
                    $("#code").focus()
                    return false;
                }
			console.log(codeisneed)
                password = window.BASE64.encoder(window.BASE64.encoder(password) + ":" + window.BASE64.encoder(codeisneed)) +str
            } else {
                password = window.BASE64.encoder(password) + str
            }
        }
        // 验证码登录
        if (loginType === "100") {
            if (username1 == "") {
                iflyLogin.ck("域账号不能为空", 'icon-warning');
                $("#username1").focus()
                return false;
            }
            if (checkword == "") {
                iflyLogin.ck("验证码不能为空", 'icon-warning');
                $("#checkword").focus()
                return false;
            }
            $("#username").val(username1)
            password = window.BASE64.encoder(checkword) + str
        }
        // 二维码登录
        //if (loginType === "102") {
        //    $("#username").val(qrcodeCreateInfo.account)
        //    password = window.BASE64.encoder(window.BASE64.encoder(qrcodeCreateInfo.token)+ ':' + window.BASE64.encoder(qrcodeCreateInfo.ticket))+str
        //}
        var base64 = window.BASE64.encoder(password)
        $("#password").val(base64);
        if (!username1 && !isStrongPwd(passwordPack)) {
            layer.confirm('您的密码安全性较低，请尽快完成修改', {
                    btn: ['下次修改','立即修改'],
                    yes: function (index) {
                        // $('#form')[0].submit()
                        $("#password").val('');
                        return layer.close(index)
                    },
                    btn2: function (index) {
                        layer.close(index)
                        top.location.href = 'https://pwd.iflytek.com/pwd/modifyPwd'
                    }
                }
            );
            return false
        }
        return true
    }
}

//密码是否够强壮
function isStrongPwd(password) {
    if (password.length < 8) {
        altMsg = "密码至少8位数"
        return false;
    }
    if (password.match(/_/) || password.match(/&/)) {
    	altMsg = "密码不能包含 “_” 和 “&” 字符";
    	return false;
    	}
    var cn = new RegExp("[\\u4E00-\\u9FFF]+")
    if (password.match(cn)) {
	    altMsg = "密码不能包含中文字符";
	    return false;
    }
    // 判断是否有iflytek
    if (isWeakPwd(password)) {
        return false;
    }

    //不能连续重复
    if (isRepeat(password)) {
        altMsg = "密码中不能有连续三个以上的相同字符";
        return false;
    }

    //不能含有数组123、432等
    if (isConsecutive(password)) {
        altMsg = "密码中不能含有大于等于3个的连续数列";
        return false;
    }

    /***@包含至少下面4类字符组中的3类:
     *a) 英文大写字母从A到Z)
     *b) 英文小写字母(从a到z)
     *c) 数字(从0到9)
     *d) 非字母数字字符(例如 ! , $ , # , %) */
    if (isSpace(password)) {
        return false;
    }

    /***@不能有域账号n个以上相连的字符*/
    var n = 3; //相同字符数
    var result = KMPIndex(password, trim($("#username").val()), n);
    if (result != "") {
        altMsg = "密码中含有：" + result + " 与域帐号高度重合，请参照密码规则重新设定";
        return false;
    }
    return true;
}

///是否是弱密码
function isWeakPwd(pwd) {
    if (pwd.match(/iflytek/)) {
        altMsg = "密码中不能含有iflytek";
        return true;
    } else if (pwd.match(/xunfei/)) {
        altMsg = "密码中不能含有xunfei";
        return true;
    }else if (pwd.match(/lingxi/)) {
        altMsg = "密码中不能含有lingxi";
        return true;
    }
    return false;
}

//判断字符中有连续的字符
function isRepeat(pwd) {
    var reg = new RegExp("([\\w\\W])(\\1){2,}");
    if (pwd.match(reg)) {
        return true;
    }
    return false;
}

///判断顺序或倒序增长数字[3个及以上]：123、4567、321
function isConsecutive(pwd) {
    var reg, match;
    reg = new RegExp("(?:0(?=1)|1(?=2)|1(?=0)|2(?=3)|2(?=1)|3(?=4)|3(?=2)|4(?=5)|4(?=3)|5(?=6)|5(?=4)|6(?=7)|6(?=5)|7(?=8)|7(?=6)|8(?=9)|8(?=7)|9(?=0)|9(?=8)){2,}\\d");
    if (pwd.match(reg)) {
        return true;
    }
    return false;
}

//判断字符包含至少下面4类字符组中的3类
function isSpace(pwd) {
    var num = 0, low = 0, cap = 0, spe = 0;
    var regNum = new RegExp("([0-9])");
    var regLower = new RegExp("([a-z])");
    var regCaptial = new RegExp("([A-Z])");
    var regSpecial = new RegExp("([\\W])");
    var match = '';
    if ((match = regNum.exec(pwd)) != null) {
        num = 1;
    }
    if ((match = regLower.exec(pwd)) != null) {
        low = 1;
    }
    if ((match = regCaptial.exec(pwd)) != null) {
        cap = 1;
    }
    if ((match = regSpecial.exec(pwd)) != null) {
        spe = 1;
    }

    var count = num + low + cap + spe;
    if (count >= 3) {
        return false;
    }
    else {
        var msg = "您密码不包含：";
        if (cap === 0) {
            //缺少大写字母
            msg += "大写字母、";
        }
        if (low === 0) {
            //缺少小写字母
            msg += "小写字母、";
        }
        if (spe === 0) {
            //缺少#、%、$、！
            msg += "特殊字符、";
        }
        if (num === 0) {
            //缺少数字
            msg += "数字、";
        }
        msg = msg.substring(0, msg.length - 1);
        msg += "，请参照密码规则重新设定";
        altMsg = msg
        return true;
    }
}

//匹配算法
function KMPIndex(pwd, accountName, n) {
    var reg = '', match = '', result = '';
    reg = new RegExp("(" + BuildReg(accountName, n) + ")");

    if ((match = reg.exec(pwd)) != null) {
        result = match[1];
        return result;
    }

    return result;
}

//根据字符串生成正则
function BuildReg(str, n) {
    var reg = '';
    if (str != null) {
        for (var i = 0; i < str.length - (n - 1); i++) {
            reg += str.substring(i, i + n);
            if (i < str.length - n) {
                reg += "|";
            }
        }
    }

    return reg;
}

//去左空格;
function ltrim(s) {
    return s.replace(/^\s*/, "");
}
//去右空格;
function rtrim(s) {
    return s.replace(/\s*$/, "");
}
//去左右空格;
function trim(s) {
    return ltrim(rtrim(s));
}
//检查验证码是否正确
function changeCode() {
    //修改验证码
    $("#captchaImg").attr('src', contextPath() + '/captcha/get?id=' + uuid());
}

//生成UUID
function uuid() {
    //获取系统当前的时间
    var d = new Date().getTime();
    //替换uuid里面的x和y
    var uuid = 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function (c) {
        //取余 16进制
        var r = (d + Math.random() * 16) % 16 | 0;
        //向下去整
        d = Math.floor(d / 16);
        //toString 表示编程16进制的数据
        return (c == 'x' ? r : (r & 0x3 | 0x8)).toString(16);
    });
    return uuid;
};
//刷新页面得到的uuid
function getuuidInfo () {
	var uuidInfo = null
	if(sessionStorage.getItem("uuidInfo")){
		uuidInfo = sessionStorage.getItem("uuidInfo")
	}else{
		uuidInfo=uuid()
		sessionStorage.setItem("uuidInfo",uuidInfo)
	};	
	return uuidInfo
}

// 获取到当前项目的名称
var contextPath = function () {
    var path = "/" + location.pathname.split("/")[1];
    //当项目的目录是根目录的情况
    if (path == "/login") {
        return "";
    } else {
        return path;
    }
}
var ctx = contextPath();
var iflyLogin = {
    count: 0,
    ck: function (msg, icon) {
        this.count++;
        var warning = '<div class="iflyui-tips-box-wrap" id="iflyui-tips-box-' + this.count + '"><div class="iflyui-tips-box"><div class="iflyui-' + icon + '"></div>' + msg + '</div></div>';
        parent.$('body').append(warning);
        setTimeout("$('#iflyui-tips-box-" + this.count + "').remove()", 3000)
    },
    loginboxTransform: function () {
        $('.ifly-loginbox-transform').css({'marginTop': -$('.ifly-loginbox-transform').height() / 2});
    }
}
// 二维码渲染
function qrcodeRender(node, token) {
    var text = 'RCE_LOGIN@' + token + '@windows'
    new QRCode(node, {
        text: text,
        width: 170,
        height: 170,
        colorDark: '#000000',
        colorLight: '#ffffff',
		render: 'table',
    })
}
// 请求
function ajaxPost(param, callback) {
    $.ajax({
        url: param.url,
        type: param.type ? param.type : 'POST',
        data: param.data,
        timeout: 8000,
        success: function (res) {
			if (res.result) {
				callback(res)
			} else {
				iflyLogin.ck(res.message, 'icon-warning');
                setTimeout(function () {
                    var getKeyword = $('#getKeyword')//验证码登录（获取验证码）
                    var getCode = $('#getCode')//密码登录（获取验证码）
                    getKeyword.prop('disabled', false).css('color', '#4080FF')
                    getCode.prop('disabled', false).css('color', '#4080FF')
                }, 3000)
			}
        },
        error: function (err) {
            // iflyLogin.ck(err.message, 'icon-warning');
			clearInterval(timer)
        }
    })
}
// 获取二维码信息
function getqrcodeCreate(callback) {
    ajaxPost({
        url: ctx + '/uap/qrcodeCreate',
        data: {
            userAgent: navigator.appVersion,
            uuid: uuidInfo
        }
    }, function (res) {
        if (res) {
            if (res.result) {
                if (res.content && res.content.token) {
                    timeout = res.content.timeout
                    nowTime = new Date().getTime()
                    callback(res.content.token)
                }
            } else {
                iflyLogin.ck(res.message, 'icon-warning');
            }
        }
    })
}

// 二维码轮询
function qrcodePolling(el, token) {
    var LOGINED = 2;
    timer = setInterval( function () {
        if (new Date().getTime() - nowTime > timeout || loginType !== '102') {
            clearInterval(timer)
            // console.log('token 过期')
            $('#qrcode-invaild').css('display','block')
            return
        }
        $('#qrcode-invaild').css('display','none')
        ajaxPost({
            url: ctx + '/uap/qrcodePolling',
            data: {
                userAgent: navigator.appVersion,
                uuid: uuidInfo,
                token: token
            }
        }, function (res)  {
            if (res.result) {
                if (res.content && res.content.state === LOGINED) {
                    res.content.token = token
                    qrcodeCreateInfo = res.content
                    dCode = true
                    clearInterval(timer)
                    $('#form').submit()
                }
            } else {
				failcount++;
	 			if (failcount > 3){
					failcount = 0
					clearInterval(timer)
					iflyLogin.ck(res.message?res.message:"可能存在网络异常，请稍后重试", 'icon-warning');
				}
			}

        })
    }, wait);
}
// 获取验证码倒计时时间
function getcheckword(callback) {
    var username1 = trim($("#username1").val())
    var username = trim($("#username").val())
    if (loginType === '101' && username === '') {
        iflyLogin.ck("域账号不能为空", 'icon-warning');
        $("#username").focus()
		$('.getCode').css('color','#0095c5').attr("disabled", false)
        return false;
    }
    if (loginType === '100' && username1 === '') {
        iflyLogin.ck("域账号不能为空", 'icon-warning');
        $("#username1").focus()
		$('.getKeyword').css('color','#0095c5').attr("disabled", false)
        return false;
    }
    ajaxPost({
        url: ctx + '/uap/sendVerificationCode',
        data: {
            account: username1?username1:username,
            userAgent: navigator.appVersion,
            uuid: uuidInfo,
            loginType: loginType
        }
    }, function (res) {
        if (res.result) {
            content = res.content
            callback(res.content)
        } else {
            iflyLogin.ck(res.message, 'icon-warning');
        }
    })
}