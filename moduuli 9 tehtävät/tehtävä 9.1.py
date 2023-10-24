class Auto:
    def __init__(self, rek, top):
        self.rek = rek
        self.top = top
        self.cur = 0
        self.dis = 0


newcar = Auto("ABC-123", 142)
print(f"Auton rekkari on {newcar.rek}, maksiminopeus {newcar.top} km/h, nykyinen nopeus {newcar.cur} km/h"
      f" ja kuljettu etäisyys {newcar.dis} km")
