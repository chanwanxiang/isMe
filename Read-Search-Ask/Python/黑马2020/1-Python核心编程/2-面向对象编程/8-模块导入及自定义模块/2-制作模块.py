# 制作模块
#     在python中,每个python文件都可以作为一个模块,模块的名字就是文件的名字,也就是说自定义模块名必须要符合标识符命名规则

# 定义模块

# 测试模块

# 使用模块

print(__name__)  #如果运行在当前文件,输出结果为__main__,如果是被导入模块执行的,输出结果为导入的模块名

if __name__ == '__main__':
    print('如果运行在当前文件,输出结果为__main__,如果是被导入模块执行的,输出结果为导入的模块名')