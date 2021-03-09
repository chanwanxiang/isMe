# 装饰器的执行时机:当当前模块加载完成之后,装饰器会立即执行,对已有函数进行装饰

import myDecorator

myDecorator.comment()  #登录验证完成\r\n 发表评论 结果并非comment()函数