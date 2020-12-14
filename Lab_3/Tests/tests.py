import time
import unittest
from selenium import webdriver
from Lab_3.Page.page import MainPage

PATH = 'C:\Program Files (x86)\chromedriver.exe'
SITE = "http://todomvc.com/examples/angularjs/#/"


class TodoTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(PATH)
        self.driver.get(SITE)

    def test_add_task(self):
        main_page = MainPage(self.driver)
        main_page.add_new_task("test_task")
        active_tasks = main_page.get_active_tasks()
        self.assertEqual(active_tasks, 1)

    def test_remove_task(self):
        main_page = MainPage(self.driver)
        main_page.add_new_task("make a dinner")
        main_page.add_new_task("go for a walk")
        main_page.add_new_task("make homework")
        active_tasks = main_page.get_active_tasks()
        self.assertEqual(active_tasks, 3)
        main_page.remove_task("go for a walk", 2)
        active_tasks = main_page.get_active_tasks()
        self.assertEqual(active_tasks, 2)

    def test_complete_task(self):
        main_page = MainPage(self.driver)
        main_page.add_new_task("make a dinner")
        main_page.add_new_task("go for a walk")
        active_tasks = main_page.get_active_tasks()
        self.assertEqual(active_tasks, 2)
        main_page.complete_task("go for a walk", 2)
        active_tasks = main_page.get_active_tasks()
        self.assertEqual(active_tasks, 1)

    def test_switch_to_active(self):
        main_page = MainPage(self.driver)
        main_page.add_new_task("make a dinner")
        main_page.add_new_task("go for a walk")
        main_page.add_new_task("make homework")
        main_page.add_new_task("check facebook")
        main_page.add_new_task("buy some food")
        active_tasks = main_page.get_active_tasks()
        self.assertEqual(active_tasks, 5)
        main_page.complete_task("buy some food", 5)
        main_page.complete_task("make homework", 3)
        main_page.switch_to_active()
        active_tasks = main_page.get_active_tasks()
        self.assertEqual(active_tasks, 3)

    def test_switch_to_completed(self):
        main_page = MainPage(self.driver)
        main_page.add_new_task("make a dinner")
        main_page.add_new_task("go for a walk")
        main_page.add_new_task("make homework")
        main_page.add_new_task("check facebook")
        main_page.add_new_task("buy some food")
        active_tasks = main_page.get_active_tasks()
        self.assertEqual(active_tasks, 5)
        main_page.complete_task("buy some food", 5)
        main_page.complete_task("make homework", 3)
        main_page.switch_to_completed()

    def test_switch_all(self):
        main_page = MainPage(self.driver)
        main_page.add_new_task("make a dinner")
        main_page.add_new_task("go for a walk")
        main_page.add_new_task("make homework")
        main_page.add_new_task("check facebook")
        main_page.add_new_task("buy some food")
        active_tasks = main_page.get_active_tasks()
        self.assertEqual(active_tasks, 5)
        main_page.switch_all()
        active_tasks = main_page.get_active_tasks()
        self.assertEqual(active_tasks, 0)
        main_page.switch_all()
        active_tasks = main_page.get_active_tasks()
        self.assertEqual(active_tasks, 5)

    def test_clear_all(self):
        main_page = MainPage(self.driver)
        main_page.add_new_task("make a dinner")
        main_page.add_new_task("go for a walk")
        main_page.add_new_task("make homework")
        main_page.add_new_task("check facebook")
        main_page.add_new_task("buy some food")

        main_page.complete_task("buy some food", 5)
        main_page.complete_task("make homework", 3)

        active_tasks = main_page.get_active_tasks()
        self.assertEqual(active_tasks, 3)

        main_page.clear_all()

    def tearDown(self):
        time.sleep(2)
        self.driver.close()


if __name__ == "__tests__":
    unittest.main()
