import unittest
import requests
import sys
from os.path import dirname, abspath
parentdir = dirname(dirname(abspath(__file__)))
sys.path.insert(0, parentdir)
from db_fixture import test_data
from parameterized import parameterized


class UserSignTest(unittest.TestCase):
    ''' 用户签到 '''

    def setUp(self):
        self.base_url = "http://127.0.0.1:8000/api/user_sign/"

    def tearDown(self):
        print(self.result)

    @parameterized.expand([
        ("all_null", "", "", 10021, "parameter error"),
        ("eid_error", 901, 13711001100, 10022, "event id null"),
        ("status_close", 3, 13711001100, 10023, "event status is not available"),
        ("time_start", 4, 13711001100, 10024, "event has started"),
        ("phone_error", 1, 10100001111, 10025, "user phone null"),
        ("eid_phone_error", 1, 13511001102, 10026, "user did not participate in the conference"),
        ("has_sign_in", 1, 13511001101, 10027, "user has sign in"),
        ("success", 1, 13511001100, 200, "sign success"),
    ])
    def test_user_sign(self, name, eid, phone, status, msg):
        payload = {'eid':eid, 'phone':phone}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        if status == 200:
            self.assertEqual(self.result['message'], msg)
        else:
            self.assertEqual(self.result['status'], status)
            self.assertEqual(self.result['message'], msg)


if __name__ == '__main__':
    test_data.create_data() # 初始化接口测试数据
    unittest.main()
