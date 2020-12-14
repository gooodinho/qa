import unittest
from Lab_1.main import ExceptionManager


class TestExceptionManagerCheckCritical(unittest.TestCase):
    def setUp(self):
        self.manager = ExceptionManager()

    def test_check_critical_exception(self):
        self.assertFalse(self.manager.check_critical(BaseException))
        self.assertFalse(self.manager.check_critical(IndexError))
        self.assertTrue(self.manager.check_critical(ZeroDivisionError))

    @unittest.expectedFailure
    def test_check_critical_another_type(self):
        self.assertEqual(self.manager.check_critical("Exception"), True)


class TestExceptionManagerCountExceptions(unittest.TestCase):
    def setUp(self):
        self.manager = ExceptionManager()

    def test_count_exceptions_exception(self):
        self.assertEqual(self.manager.critical, 0)
        self.assertEqual(self.manager.non_critical, 0)

        self.manager.count_exceptions(ZeroDivisionError)
        self.manager.count_exceptions(KeyError)
        self.manager.count_exceptions(TypeError)

        self.assertEqual(self.manager.critical, 3)

        self.manager.count_exceptions(IndexError)
        self.manager.count_exceptions(SyntaxError)

        self.assertEqual(self.manager.non_critical, 2)

    @unittest.expectedFailure
    def test_count_exceptions_another_type(self):
        self.manager.count_exceptions(404)


if __name__ == '__test_main__':
    unittest.main()
