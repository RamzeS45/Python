class Gear:
    def __init__(self, smalkol, bigkol, rim, tire):
        self.smalkol = smalkol
        self.bigkol = bigkol
        self.rim = rim
        self.tire = tire

    @property
    def rash(self):
        return self.bigkol / self.smalkol

    @property
    def gear_inch(self):
        return self.rash * self.diam

    @property
    def diam(self):
        return self.rim + (self.tire * 2)

two = Gear(11, 52, 26, 1.5)
print(two.rash)
print(two.gear_inch)
print(two.diam)