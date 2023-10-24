class Auto:
    def __init__(self, rek, top, cur=0, dis=0):
        self.rek = rek
        self.top = top
        self.cur = cur
        self.dis = dis


newcar = Auto("ABC-123", 142)
print(f"Auton rekkari on {newcar.rek}, maksiminopeus {newcar.top} km/h, nykyinen nopeus {newcar.cur} km/h"
      f" ja kuljettu etäisyys {newcar.dis} km")
