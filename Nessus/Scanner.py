import requests
import json



class SSLException(Exception):
    pass

class Scanner:


    login = ""
    password = ""
    insecure = True
    url = ""
    token = ""

    def __init__(self, login, password, insecure, url):
        self.login = login
        self.password = password
        if insecure:
            self.insecure = insecure
        self.url = url

    ################################################################################
    def SetToken(self, token):
        self.token = str(token)

    ################################################################################
    def LoginScanner(self):

        extra = {"username": self.login, "password": self.password}

        request = requests.post(url = self.url+'/session', data=extra, verify=False)

        if request.status_code != 200:
            print "Server Error Code: " + str(request.status_code)
        else:
            parsed_json = json.loads(request.text)
            token = parsed_json["token"]
            self.SetToken(token)

    def GetScans(self):

        headers = {'X-Cookie': 'token=' + self.token }

        request = requests.get(url=self.url + '/scans', headers = headers, verify=False)

        if request.status_code != 200:
            print "Server Error Code: " + str(request.status_code)
        else:
            parsed_json = json.loads(request.text)
            scans = parsed_json["scans"]
            return scans


    ################################################################################



