from selenium.webdriver.common.by import By


class ProjectHelper:

    def __init__(self, app):
        self.app = app


    def add(self, project):
        wd = self.app.wd
        self.app.navigation.open_project_management()
        wd.find_element(By.XPATH, "//button[text() = 'Создать новый проект']").click()
        self.fill_project_form(project)
        wd.find_element(By.CSS_SELECTOR, "input[value='Добавить проект']").click()


    def delete_project_by_id(self, project_id):
        wd = self.app.wd
        self.app.navigation.open_project_management()
        self.open_project_by_id(project_id)
        wd.find_element(By.CSS_SELECTOR, "button[formaction='manage_proj_delete.php']").click()
        wd.find_element(By.CSS_SELECTOR, "input[value='Удалить проект']").click()


    def fill_project_form(self, project):
        self.change_field_value("name", project.name)
        self.change_field_value("description", project.description)


    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, field_name).click()
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).send_keys(text)


    def open_project_by_id(self, project_id):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//td/a[contains(@href, 'id=%s')]" % project_id).click()