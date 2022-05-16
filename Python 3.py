class Ink:
    def __init__(self):
        self.data = data

    def diam(self):
        # 0 - rim, 1 - tire
        self.data.collect(self.for_fun)

    def for_fun(self, data_val):
        return data_val * 2

    def collect(self, formul):
        for i, value in enumerate(self.data):
            value = formul(value)