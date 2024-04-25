class Vehicle():
    def __init__(self, a, b):
        self.pavadinimas = a
        self.rida = b

class Car(Vehicle):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.vietos = c
    def GetSeats(self):
        return f'{self.pavadinimas} turi {self.vietos} sėdimų vietų'
    
class Bus(Vehicle):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.vietos = c
    def GetSeats(self):
        return f'{self.pavadinimas} turi {self.vietos} sėdimų vietų'
    
class Train(Vehicle):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.vietos = c
    def GetSeats(self):
        return f'{self.pavadinimas} turi {self.vietos} sėdimų vietų'