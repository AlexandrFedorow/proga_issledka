

def Masche(pol, scale, mode=1):#сетка (поле в которое надо добавить сетку)
    #горизонтальные линии
    if mode == 1:
        for x in range(21):
            k = scale * x
            pol.create_line(10, 10+k, 820, 10+k, width=1, fill='#191938', tag='ms')
        #вертикальные линии
        for y in range(28):
            k = scale * y
            pol.create_line(10+k, 610, 10+k, 10, width=1, fill='#191938', tag='ms')


class Point:
    def __init__(self, x, y, color, tagg, pol):
        self.x = x
        self.y = y
        self.color = color
        self.pol = pol
        self.tagg = tagg

    def create_point(self):
        self.pol.create_oval(self.x, self.y, self.x + 10, self.y + 10, fill=self.color, tag=self.tagg)


class Line:
    def __init__(self, x1, y1, x2, y2, color, tagg, pol):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = color
        self.tagg = tagg
        self.pol = pol

    def create_line(self):
        self.pol.create_line(self.x1+5, self.y1+5, self.x2+5, self.y2+5, fill=self.color, tag=self.tagg)

