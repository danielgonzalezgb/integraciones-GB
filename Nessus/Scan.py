import json
import requests
import Scanner


class Scan:

    id=0
    name = ""
    vulnerabilities = []
    remediations = []
    hosts = []
    token = ""

    def __init__(self, id, name, vulnerabilities, remediations, hosts):
        if id:
            self.id = id

        if name:
            self.name = name
        if vulnerabilities:
            self.vulnerabilities = vulnerabilities
        if remediations:
            self.remediations = remediations
        if hosts:
            self.hosts = hosts

    def __init__(self, id, scanner):
        if id:
            self.id = id
            self.token = scanner.token
            self.url = scanner.url

    def GetScanDetails(self):

        headers = {'X-Cookie': 'token=' + self.token}

        request = requests.get(url=self.url + '/scans/'+str(self.id), headers=headers, verify=False)

        if request.status_code != 200:
            print "Server Error Code: " + str(request.status_code)
        else:
            parsed_json = json.loads(request.text)
            return parsed_json

    def SetScanDetails(self):

        headers = {'X-Cookie': 'token=' + self.token}

        request = requests.get(url=self.url + '/scans/'+str(self.id), headers=headers, verify=False)

        if request.status_code != 200:
            print "Server Error Code: " + str(request.status_code)
        else:
            parsed_json = json.loads(request.text)
            self.vulnerabilities = parsed_json ["vulnerabilities"]
            self.remediations = parsed_json["remediations"]
            self.hosts = parsed_json["hosts"]
            self.name = parsed_json["name"]
