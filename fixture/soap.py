from suds.client import Client
from suds import WebFault


class SOAPHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client("https://localhost/mantisbt/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False