class Connection:

    user = ""
    url = ""
    domain = ""
    password = ""

    def __init__(self, url, user, domain, password):
        self.user = user
        self.url = url
        self.domain = domain
        self.password = password