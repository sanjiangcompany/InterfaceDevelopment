import time, sys
sys.path.append('./interface')
sys.path.append('./db_fixture')
from HTMLTestRunner import HTMLTestRunner
from unittest import defaultTestLoader
from db_fixture import  test_data


"""
设计：
1、连接数据库：MySQL(PyMysql)
2、数据初始化，保证可以重复执行， db_fixture/
3、设计接口测试用：unttest + request + 参数化
4、批量 discover 匹配测试文件，+ HTMLTestRunner 生成测试报告

"""
# 指定测试用例为当前文件夹下的 interface 目录

test_dir = './interface'
testsuit = defaultTestLoader.discover(test_dir, 
	pattern='user_sign_test.py')

if __name__ == "__main__":
    test_data.create_data() # 初始化接口测试数据

    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = './report/' + now + '_result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='系统接口自动化测试',
                            description='运行环境：MySQL(PyMySQL), Requests, unittest ')
    runner.run(testsuit)
    fp.close()
