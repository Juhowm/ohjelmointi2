class Auto:
    def __init__(self, rek, top, cur=0, dis=0):
        self.rek = rek
        self.top = top
        self.cur = cur
        self.dis = dis

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


newcar = Auto("ABC-123", 142)
print(f"Auton rekkari on {newcar.rek}, maksiminopeus {newcar.top} km/h, nykyinen nopeus {newcar.cur} km/h"
      f" ja kuljettu etäisyys {newcar.dis} km")

newcar.kiihdytä(30)
newcar.kiihdytä(70)
newcar.kiihdytä(50)
print(f"Auton nopeus on nyt {newcar.cur} km/h")
newcar.kiihdytä(-200)
print(f"Auton nopeus on nyt {newcar.cur} km/h")
