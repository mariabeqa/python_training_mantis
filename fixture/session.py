from selenium.webdriver.common.by import By


class SessionHelper:

    def __init__(self, app):
        self.app = app


    def logout(self):
        wd = self.app.wd
        wd.find_element(By.CSS_SELECTOR, "span.user-info").click()
        wd.find_element(By.LINK_TEXT, "Выход").click()


    def ensure_logout(self):
        wd = self.app.wd
        if self.is_logged_in():
            wd.find_element(By.CSS_SELECTOR, "span.user-info").click()
            wd.find_element(By.PARTIAL_LINK_TEXT, "Выход").click()


    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements(By.CSS_SELECTOR, "span.user-info")) > 0


    def is_logged_in_as(self, username):
        return self.get_logged_user() == username


    def get_logged_user(self):
        wd = self.app.wd
        return wd.find_element(By.CSS_SELECTOR, "span.user-info").text


    def login(self, username, password):
        wd = self.app.wd
        wd.get(self.app.base_url)
        wd.find_element(By.NAME, "username").click()
        wd.find_element(By.NAME, "username").clear()
        wd.find_element(By.NAME, "username").send_keys(username)
        wd.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        wd.find_element(By.NAME, "password").click()
        wd.find_element(By.NAME, "password").clear()
        wd.find_element(By.NAME, "password").send_keys(password)
        wd.find_element(By.CSS_SELECTOR, "input[type='submit']").click()


    def ensure_login(self, username, password):
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)