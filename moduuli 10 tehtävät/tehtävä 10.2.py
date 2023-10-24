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
            print(self.hissit)

    def aja_hissiä(self, hissi, kohde):
        liike = self.hissit[hissi]
        liike.siirry_kerrokseen(kohde)


talo = Talo(1, 5, 3)
talo.aja_hissiä(1, 4)
