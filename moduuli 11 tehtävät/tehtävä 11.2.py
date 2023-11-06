class Auto:
    def __init__(self, rek, top):
        self.rek = rek
        self.top = top
        self.cur = top
        self.dis = 0

    def kulje(self, hours):
        self.dis += self.cur * hours


class Sähköauto(Auto):
    def __init__(self, rek, top, batcap):
        super().__init__(rek, top)
        self.batcap = batcap


class Polttomoottoriauto(Auto):
    def __init__(self, rek, top, tank):
        super().__init__(rek, top)
        self.tank = tank


autot = []
autot.append(Sähköauto("ABC-15", 180, 52.5))
autot.append(Polttomoottoriauto("ACD-123", 165, 32.3))
for auto in autot:
    auto.kulje(3)
    print(f"Auto {auto.rek} on kulkenut {auto.dis}km")
