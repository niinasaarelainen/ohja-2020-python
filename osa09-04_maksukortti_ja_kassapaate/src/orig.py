# TEE RATKAISUSI TÄHÄN:

class Maksukortti:
    def __init__(self, saldo: float):
        self.saldo = saldo
    def lataa_rahaa(self, lisays: float):
        self.saldo += lisays
    def ota_rahaa(self, maara: float):
        pass
        # toteuta metodi siten että se ottaa kortilta rahaa vain jos saldo on vähintään maara
        # onnistuessaan metodi palauttaa True ja muuten False
class Kassapaate:
    def __init__(self):
        # kassassa on aluksi 1000 euroa rahaa
        self.rahaa = 1000
        self.edulliset = 0
        self.maukkaat = 0
    def syo_edullisesti(self, maksu: float):
        # edullinen lounas maksaa 2.50 euroa.
        # kasvatetaan kassan rahamäärää edullisen lounaan hinnalla ja palautetaan vaihtorahat
        # jos parametrina annettu maksu ei ole riittävän suuri, ei lounasta myydä ja metodi palauttaa koko summan
        pass
    def syo_maukkaasti(self, maksu: float):
        # maukas lounas maksaa 4.30 euroa.
        # kasvatetaan kassan rahamäärää maukkaan lounaan hinnalla ja palautetaan vaihtorahat
        # jos parametrina annettu maksu ei ole riittävän suuri, ei lounasta myydä ja metodi palauttaa koko summan
        pass
    def syo_edullisesti_kortilla(self, kortti:Maksukortti):
        # edullinen lounas maksaa 2.50 euroa.
        # jos kortilla on tarpeeksi rahaa, vähennetään hinta kortilta ja palautetaan True
        # muuten palautetaan False
        pass
    def syo_maukkaasti_kortilla(self, kortti:Maksukortti):
        # maukas lounas maksaa 4.30 euroa.
        # jos kortilla on tarpeeksi rahaa, vähennetään hinta kortilta ja palautetaan True
        # muuten palautetaan False
        pass
    def lataa_rahaa_kortille(self, kortti: Maksukortti, summa: float):
        pass
    def __repr__(self):
        return f"kassassa rahaa {self.rahaa} edullisia lounaita myyty {self.edulliset} maukkaita lounaita myyty {self.maukkaat}"
