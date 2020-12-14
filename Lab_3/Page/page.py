from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Lab_3.Locator.locator import *


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    def add_new_task(self, task_name):
        holder = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.INPUT_PLACEHOLDER)
        )
        holder.send_keys(task_name)
        holder.send_keys(Keys.RETURN)

    def get_active_tasks(self):
        active_tasks_holder = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.ACTIVE_TASKS)
        )
        if active_tasks_holder.find_element_by_tag_name("strong").text == '':
            return 0
        else:
            active_tasks = int(active_tasks_holder.find_element_by_tag_name("strong").text)
            return active_tasks

    def remove_task(self, name, number):
        holder, button = MainPageLocators.get_remove_button(name, number)
        holder = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(holder)
        )
        button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(button)
        )

        action = ActionChains(self.driver)
        action.move_to_element(holder).perform()
        button.click()

    def complete_task(self, name, number):
        holder, button = MainPageLocators.get_complete_button(name, number)
        holder = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(holder)
        )
        complete_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(button)
        )
        action = ActionChains(self.driver)
        action.move_to_element(holder).perform()
        complete_button.click()

    def switch_to_active(self):
        switch_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.get_switch_active_button())
        )
        action = ActionChains(self.driver)
        action.move_to_element(switch_button).perform()
        switch_button.click()

    def switch_to_completed(self):
        switch_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.get_switch_completed_button())
        )
        action = ActionChains(self.driver)
        action.move_to_element(switch_button).perform()
        switch_button.click()

    def switch_all(self):
        switcher = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.get_switcher_button())
        )
        action = ActionChains(self.driver)
        action.move_to_element(switcher).perform()
        switcher.click()

    def clear_all(self):
        clear_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.get_clear_all_button())
        )
        action = ActionChains(self.driver)
        action.move_to_element(clear_button).perform()
        clear_button.click()
