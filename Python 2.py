class Gear():
    def __init__(self, smalkol, bigkol, diam, obod):
        self.smalkol = smalkol
        self.bigkol = bigkol
        self.diam = diam
        self.obod = obod

    @property
    def rash(self):
        return self.bigkol / self.smalkol

    @property
    def pered(self):
        return self.rash * (self.diam + (self.obod * 2))


one = Gear(11, 52, 26, 1.5)
print("=>", one.pered)
two = Gear(11, 52, 24, 1.25)
print("=>", two.pered)