class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi


class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumäärä):
        super().__init__(nimi)
        self.kirj = kirjoittaja
        self.sm = sivumäärä

    def tulosta_tiedot(self):
        print(f"Kirjan nimi on {self.nimi}, sen kirjoittaja on {self.kirj}, ja siinä on {self.sm} sivua")


class Lehti(Julkaisu):
    def __init__(self, nimi, päätoimittaja):
        super().__init__(nimi)
        self.pt = päätoimittaja

    def tulosta_tiedot(self):
        print(f"Lehden nimi on {self.nimi}, ja sen päätoimittaja on {self.pt}")


julkaisut = []
julkaisut.append(Lehti("Aku Ankka", "Aki Hyyppä"))
julkaisut.append(Kirja("Hytti n:o 6", "Rosa Liksom", 200))
for k in julkaisut:
    k.tulosta_tiedot()
