__author__ = "Daniel Gonzalez"

import json
import requests

#Esta es la clase que se encarga de hacer las consultas hacia freshservice

class Freshservice:

    user = ""
    url = ""
    domain = ""
    password = ""

    def __init__(self, url, user, domain, password):
        self.user = user
        self.url = url
        self.domain = domain
        self.password = password

    #Metodo para obtener todos los tickets dentro de de nuestro helpdesk

    def GetTickets(self):

        respuesta = requests.get(str(self.url), auth=(self.user, self.password))

        if respuesta.status_code != 200:
            return 'Error response code: ' + str(respuesta.status_code)
        else:
            tickets = json.loads(respuesta.text)
            return tickets
    #Metodo para crear un ticket en freshdesk

    def CreateTicket(self, description, subject, email, priority, status, source, ticket_type, cc_email):

        data = {
            'helpdesk_ticket' : {
                'description': str(description),
                'subject': str(subject),
                'email': str(email),
                'priority': int(priority), 'status': int(status), 'source': int(source),'ticket_type': str(ticket_type),
            },
            'cc_emails': str(cc_email)
        }

        respuesta = requests.post(str(self.url), auth=(self.user, self.password), json = data)

        if respuesta.status_code == 200:
            return True
        else:
            return False



fresh = Freshservice('https://gbdemo.freshdesk.com/helpdesk/tickets.json', 'daniel.gonzalez@gb-advisors.com', '','eduardo,.4052')
fresh.CreateTicket('Ticket creado desde pyhton','Ticket creado por script de python','testsssss@gmail.com',2,2,2,'Incident', 'dgl452@gmail.com')
