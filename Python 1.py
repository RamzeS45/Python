class Pered:

    def __init__(self, smalkol, bigkol, vali):
        self.smalkol = smalkol
        self.vali = vali
        self.bigkol = bigkol

    @property
    def rash(self):
        return self.bigkol / self.smalkol

    @property
    def prim(self):
        return self.vali + 1


one = Pered(11, 52, 1)
print("=>", one.rash)
two = Pered(27, 30, 1)
print("=>", two.prim)
input()