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


autot = []
voitto = False
for n in range(1, 11):
    uusauto = Auto(f"ABC-{n}", random.randint(100, 200))
    autot.append(uusauto)
while voitto is False:
    for auto in autot:
        auto.kiihdytä(random.randint(-10, 15))
        auto.kulje(1)
        if auto.dis >= 10000:
            voitto = True
            print("|{:^20}|{:^20}|{:^20}|{:^20}|".format("rekisteri", "max. nopeus (km/h)", "nykynopeus (km/h)"
                                                         , "etäisyys (km)"))
            for auto in autot:
                print("|{:20}|{:<20}|{:<20}|{:<20}|".format(vars(auto)["rek"], vars(auto)["top"],
                                                            vars(auto)["cur"], vars(auto)["dis"]))
