class Henkilo:

    def __init__(self, nimi):
        self.splitted = nimi.split(" ")       
        self.etunimi = self.splitted[0]
        self.sukunimi = self.splitted[1]

    def anna_etunimi(self):        
        return self.etunimi

    def anna_sukunimi(self):        
        return self.sukunimi











