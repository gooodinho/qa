from selenium.webdriver.common.by import By


class MainPageLocators(object):
    INPUT_PLACEHOLDER = (By.CLASS_NAME, "new-todo")
    ACTIVE_TASKS = (By.CLASS_NAME, "todo-count")

    @staticmethod
    def get_remove_button(name, number):
        return ((By.XPATH, f"//label[contains(.,'{name}')]"),
                (By.XPATH, f"/html/body/ng-view/section/section/ul/li[{number}]/div/button"))

    @staticmethod
    def get_complete_button(name, number):
        return ((By.XPATH, f"//label[contains(.,'{name}')]"),
                (By.XPATH, f'/html/body/ng-view/section/section/ul/li[{number}]/div/input'))

    @staticmethod
    def get_switch_active_button():
        return (By.XPATH, '/html/body/ng-view/section/footer/ul/li[2]/a')

    @staticmethod
    def get_switch_completed_button():
        return (By.XPATH, '/html/body/ng-view/section/footer/ul/li[3]/a')

    @staticmethod
    def get_switcher_button():
        return (By.XPATH, '/html/body/ng-view/section/section/label')

    @staticmethod
    def get_clear_all_button():
        return (By.XPATH, '/html/body/ng-view/section/footer/button')