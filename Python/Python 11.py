class Gear:

    def __init__(self, smalkol, bigkol):
        self.smalkol = smalkol
        self.bigkol = bigkol

    def rash(self):
        return self.bigkol / self.smalkol

    def gear_inch(self, diam):
        return self.rash() * diam

class Whell:
    def __init__(self, rim, tire, smalkol, bigkol):
        self.rim = rim
        self.tire = tire
        self.gear = Gear(smalkol, bigkol)

    def diam(self):
        return self.rim + (self.tire * 2)

    def gear_inch(self):
        return self.gear.gear_inch(self.diam())

one = Whell(26, 1.5, 11, 52)
print(one.gear_inch())