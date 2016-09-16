class Coin:

    def __init__(self):

        self.unique_reps = 0

        self.p200 = 0
        self.p100 = 0
        self.p50 = 0
        self.p20 = 0
        self.p10 = 0
        self.p5 = 0
        self.p2 = 0
        self.p1 = 0

    def tab_all(self):

        return 200 * self.p200 + 100 * self.p100 + 50 * self.p50 + 20 * self.p20 + \
               10 * self.p10 + 5 * self.p5 + 2 * self.p2 + 1 * self.p1


    def add_1p(self):

        self.p1 += 1
        if self.tab_all() >= 200:
            self.unique_reps += 1


