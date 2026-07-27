from selenium.webdriver.common.by import By

class NavigationHelper:

    def __init__(self, app):
        self.app = app


    def open_login_page(self):
        wd = self.app.wd
        wd.get(self.app.base_url)


    def open_project_management(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//span[text() =' Управление ']").click()
        wd.find_element(By.LINK_TEXT, "Проекты").click()