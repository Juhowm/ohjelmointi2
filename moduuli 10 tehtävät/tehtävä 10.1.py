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


hissi = Hissi(1, 5)
hissi.siirry_kerrokseen(5)
hissi.siirry_kerrokseen(1)
