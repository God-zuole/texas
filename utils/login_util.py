import requests

class Login_Util():

    def __init__(self):
        pass

    def login(self, username, password):
        url = "http://100.102.177.124:8080/texas/login"
        data = {"username": username, "password": password}
        response = requests.post(url, json=data)
        if response.status_code == 200:
            return response.text
        else:
            return "Login failed"


