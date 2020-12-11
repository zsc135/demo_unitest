import unittest


# 使用TestCase
from login import get_username,get_password
version=2.0
class TestLogin(unittest.TestCase):



    # 类的初始化方法
    @classmethod
    def setUpClass(cls) -> None:
        print("执行类之前调用一次")

    # 类的清空方法
    @classmethod
    def tearDownClass(cls) -> None:
        print("执行类之后调用一次")

    # 初始化用例
    def setUp(self) -> None:
        print("每次执行测试用例前执行")

    # 清空方法
    def tearDown(self) -> None:
        print("每次执行用例后执行")

    def test_login_username(self):
        # 预期结果:自己的账号
        expect_username='test01'
        # 实际结果：显示在页面上的账号
        acutl_username=get_username()
        self.assertEqual(expect_username,acutl_username)
        #assert expect_username==acutl_username

    @unittest.skipIf(version>1.0,'执行此用例')
    def test_login_password(self):
        # 预期结果:自己的密码
        expect_password='test01'
        # 实际结果：显示在页面上的密码
        acutl_passwrd=get_password()
        self.assertEqual(expect_password,acutl_passwrd)
        #assert  expect_password==acutl_passwrd

#unittest.main()

#  1.通过TestSuite中的addTest去添加测试用例

# 创建一个测试套件，套件可以理解为一组用例的组合
# suite=unittest.TestSuite()

# 添加一条测试用例
# suite.addTest(TestLogin('test_login_username'))
# suite.addTest(TestLogin('test_login_password'))

# 添加多条测试用例：addTests
# lst=[TestLogin('test_login_username'),TestLogin('test_login_password')]
# suite.addTests(lst)



# 2使用TestLoader中的discover来执行测试用例
suite=unittest.TestLoader().discover('.',pattern='test*.py')

runner=unittest.TextTestRunner()
runner.run(suite)