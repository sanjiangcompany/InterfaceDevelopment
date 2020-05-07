import unittest
import requests
import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from db_fixture import test_data
from parameterized import parameterized


class AddEventTest(unittest.TestCase):
    ''' 添加发布会 '''

    def setUp(self):
        self.base_url = "http://127.0.0.1:8000/api/add_event/"

    def tearDown(self):
        print(self.result)

    @parameterized.expand([
        ('all_null', '', '', '', '', '',10021,'parameter error'),
        ('eid_exist',1, '一加4发布会', 2000, '深圳宝体', '2018',10022, 'event id already exists'),
        ('name_exist', 12, '红米Pro发布会', 2000, '深圳宝体', '2018', 10023, 'event name already exists'),
        ('start_time_error', 11, '一加5手机发布会', 2000, '深圳宝体', '2018', 10024, 'start_time format error'),
        ('add_success', 13, '一加5手机发布会', 2000, '深圳宝体', '2018-05-10 12:00:00', 200, 'add event success'),
    ])
    def test_add_event(self,name, eid, ename, limit, address, start_time, assert_status, assert_message):
        ''' 添加发布会测试 '''
        payload = {'eid':eid,'name':ename,'limit':limit,'address':address,'start_time':start_time}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        if assert_status == 10024:
            self.assertIn(assert_message, self.result['message'])
        else:
            self.assertEqual(self.result['status'], assert_status)
            self.assertEqual(self.result['message'], assert_message)


if __name__ == '__main__':
    test_data.create_data() # 初始化接口测试数据
    unittest.main()

