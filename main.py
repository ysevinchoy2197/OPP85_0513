#2-misol
class Hayvon:
    def __init__(self, nomi):
        self.nomi = nomi
    def ovoz(self):
        print("Noma'lum ovoz")

class It(Hayvon):
    def __init__(self, nomi, zoti):
        super().__init__(nomi)
        self.zoti = zoti

    def ovoz(self):
        print(f"Nomi: {self.nomi}")
        print(f"Zoti: {self.zoti}")
        print("Vov-vov")

i = It("Rex", "Ovchi")
i.ovoz()
