pyrequest project:

  它包含功能:
  * 测试数据初始化，并对数据的插入做了封装。
  * unittest单元测试框架运行测试
  * HTMLTestRunner生成接口测试报告

Python版本
  * python2.0.7+ :https://www.python.org/
 
简单数据准备

```MySQL
ALTER TABLE  `sign_event` CHANGE  `create_time`  `create_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
ALTER TABLE  `sign_guest` CHANGE  `create_time`  `create_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
```
