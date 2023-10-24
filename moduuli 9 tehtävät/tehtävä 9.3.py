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


newcar = Auto("ABC-123", 142)
print(f"Auton rekkari on {newcar.rek}, maksiminopeus {newcar.top} km/h, nykyinen nopeus {newcar.cur} km/h"
      f" ja kuljettu etäisyys {newcar.dis} km")

newcar.kiihdytä(30)
newcar.kiihdytä(70)
newcar.kiihdytä(50)
print(f"Auton nopeus on nyt {newcar.cur} km/h")
newcar.kiihdytä(-200)
print(f"Auton nopeus on nyt {newcar.cur} km/h")
