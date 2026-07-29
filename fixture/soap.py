from suds.client import Client
from suds import WebFault

from model.project import Project


class SOAPFixture:

    def __init__(self, url, username, password):
        self.client = Client(url)
        self.username = username
        self.password = password

    def can_login(self, username, password):
        try:
            self.client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_all_projects(self):
        projects = self.client.service.mc_projects_get_user_accessible(self.username, self.password)

        return [Project(id=str(project.id), name=project.name, description=str(project.description)) for project in projects]