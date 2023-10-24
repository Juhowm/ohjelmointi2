import random


class Auto:
    def __init__(self, rek, top):
        self.rek = rek
        self.top = top
        self.cur = 0
        self.dis = 0

    def kiihdytä(self, addcur):
        if addcur >= 0:
            if self.cur + addcur <= self.top:
                self.cur += addcur
            else:
                self.cur = self.top
        else:
            if self.cur + addcur < 0:
                self.cur = 0
            else:
                self.cur += addcur

    def kulje(self, hours):
        self.dis += self.cur * hours


class Kilpailu:
    def __init__(self, nimi, pituus, osat):
        self.nimi = nimi
        self.pituus = pituus
        self.osallistujat = []
        for n in range(1, osat+1):
            self.osallistujat.append(Auto(f"ABC-{n}", random.randint(100, 200)))

    def tunti_kuluu(self):
        for auto in self.osallistujat:
            auto.kiihdytä(random.randint(-10, 15))
            auto.kulje(1)

    def tulosta_tilanne(self):
        print("|{:^20}|{:^20}|{:^20}|{:^20}|".format("rekisteri", "max. nopeus (km/h)", "nykynopeus (km/h)"
                                                     , "etäisyys (km)"))
        for auto in self.osallistujat:
            print("|{:20}|{:<20}|{:<20}|{:<20}|".format(vars(auto)["rek"], vars(auto)["top"],
                                                        vars(auto)["cur"], vars(auto)["dis"]))

    def kilpailu_ohi(self):
        for auto in self.osallistujat:
            if auto.dis >= self.pituus:
                tulo = True
                break
            else:
                tulo = False
        return tulo


voitto = False
kilpailu = Kilpailu("Suuri romuralli", 8000, 10)
tunti = 0
while voitto is False:
    kilpailu.tunti_kuluu()
    tunti += 1
    voitto = kilpailu.kilpailu_ohi()
    if voitto is True:
        print("")
        print(f"Kilpailu loppui tunnilla {tunti}")
        kilpailu.tulosta_tilanne()
        break
    if tunti % 10 == 0:
        print("")
        print(f"Tunnilla {tunti} tilanne näyttää tältä: ")
        kilpailu.tulosta_tilanne()
