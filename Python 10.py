class Gear:
    def __init__(self, smalkol, bigkol, whell):
        self.smalkol = smalkol
        self.bigkol = bigkol
        self.whell = whell

    @property
    def rash(self):
        return self.bigkol / self.smalkol

    @property
    def gear_inch(self):
        return self.rash * self.whell.diam


class Whell:
    def __init__(self, rim, tire):
        self.rim = rim
        self.tire = tire

    @property
    def diam(self):
        return self.rim + (self.tire * 2)

one = Gear(
    11,
    52,
    Whell(26, 1.5)
)
print(one.gear_inch)