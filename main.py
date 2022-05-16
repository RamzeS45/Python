class Gear:
    def __init__(self, smalkol, bigkol):
        self.smalkol = smalkol
        self.bigkol = bigkol

    @property
    def rash(self):
        return self.bigkol / self.smalkol

    @property
    def gear_inch(self):
        return self.rash * Whell.diam

class Whell:
    def __init__(self, rim, tire, gear):
        self.rim = rim
        self.tire = tire
        self.gear = gear

    @property
    def diam(self):
        return self.rim + (self.tire * 2)

    @property
    def gear_inch(self):
        return self.gear.gear_inch

one = Whell(26, 1.5, Gear(11, 52))
print(one.gear_inch)