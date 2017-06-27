__author__ = "Daniel Gonzalez"

import json
import requests
from Connection import Connection

#Esta es la clase que se encarga de hacer las consultas hacia freshservice

class Ticket:

    connection = ""

    def __init__(self, connection):
        self.connection = connection


    #Metodo para obtener todos los tickets dentro de de nuestro helpdesk

    def GetTickets(self):

        respuesta = requests.get(str(self.connection.url)+'/helpdesk/tickets.json', auth=(self.connection.user, self.connection.password))

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

        respuesta = requests.post(str(self.connection.url)+'/helpdesk/tickets.json', auth=(self.connection.user, self.connection.password), json = data)

        if respuesta.status_code == 200:
            return True
        else:
            return False


m = Connection('https://gbdemo.freshdesk.com', 'daniel.gonzalez@gb-advisors.com', '','eduardo,.4052')
fresh = Ticket(m)

fresh.GetTickets()
