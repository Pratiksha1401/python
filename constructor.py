class rectangle:
    def __init__(self, length=1, breadth=1):
        self.ln=length
        self.br=breadth
    def calcarea(self, ob):
        area=ob.ln*ob.br
        print(area)
a=rectangle(5, 10)
b=rectangle()
b.calcarea(a)
