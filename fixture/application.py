from selenium import webdriver

from fixture.james import JamesHelper
from fixture.navigation import NavigationHelper
from fixture.project import ProjectHelper
from fixture.session import SessionHelper

class Application:

    def __init__(self, browser, config):

        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser: %s" % browser)
        self.wd.implicitly_wait(10)
        self.session = SessionHelper(self)
        self.config=config
        self.base_url = config['web']['baseUrl']
        self.navigation = NavigationHelper(self)
        self.project = ProjectHelper(self)
        self.james = JamesHelper(self)


    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False                    


    def destroy(self):
        self.wd.quit()