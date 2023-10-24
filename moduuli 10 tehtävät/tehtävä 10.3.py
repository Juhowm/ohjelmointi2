class Hissi:
    def __init__(self, floormin, floormax):
        self.floor = floormin
        self.floormin = floormin
        self.floormax = floormax

    def kerros_ylös(self):
        if self.floor < self.floormax:
            self.floor += 1
            print(f"Olet nyt kerroksessa {self.floor}")
        elif self.floor == self.floormax:
            print(f"Olet jo ylimmässä kerroksessa {self.floor}")

    def kerros_alas(self):
        if self.floor > self.floormin:
            self.floor -= 1
            print(f"Olet nyt kerroksessa {self.floor}")
        elif self.floor == self.floormin:
            print(f"Olet jo alimmasssa kerroksessa {self.floor}")

    def siirry_kerrokseen(self, kohde):
        if kohde > self.floormax or kohde < self.floormin:
            print("Tätä kerrosta ei ole")
        while self.floor > kohde >= self.floormin:
            self.kerros_alas()
        while self.floor < kohde <= self.floormax:
            self.kerros_ylös()


class Talo:
    def __init__(self, floormin, floormax, hissejä):
        self.floormin = floormin
        self.floormax = floormax
        self.hissejä = hissejä
        self.hissit = []
        for n in range(hissejä):
            self.hissit.append(Hissi(self.floormin, self.floormax))

    def aja_hissiä(self, hissi, kohde):
        liike = self.hissit[hissi]
        liike.siirry_kerrokseen(kohde)

    def palohälytys(self):
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(self.floormin)


alin = int(input("Mikä on talon alin kerros? "))
ylin = int(input("Mikä on talon ylin kerros? "))
mr = int(input("Kuinka monta hissiä talossa on? "))
talo = Talo(alin, ylin, mr)
while input("Haluatko liikkua hisseillä? Vastaa k jos kyllä. ") == "k":
    val = int(input(f"Millä hissillä haluat liikkua (välillä 1-{mr})? "))
    paik = int(input(f"Mihin kerrokseen haluat mennä (välillä {alin}-{ylin})? "))
    talo.aja_hissiä(val-1, paik)
else:
    print("Talossa on palohälytys! Kaikki hissit palaavat pohjakerrokseen!")
    talo.palohälytys()

