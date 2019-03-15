class Time:
    def __init__(self):
        self.hr = 00
        self.m = 00

    def get_time(self, hr, m):
        self.hr = hr
        self.m = m

    def show_time(self):
        print("hours:", self.hr)
        print("minutes:", self.m)

t = Time()
t.get_time(12, 18)
t.show_time()

