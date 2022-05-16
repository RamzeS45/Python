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
        two = Whell(self.rim, self.tire)
        return self.rash * two.diam

class Whell:
    def __init__(self, rim, tire):
        self.rim = rim
        self.tire = tire

    @property
    def diam(self):
        return self.rim + (self.tire * 2)

one = Gear(11, 52, 26, 1.5)
print(one.gear_inch)