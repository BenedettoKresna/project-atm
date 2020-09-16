# Code sebagai kartu ATM

class ATMCard:
    def __init__(defaultPin, defaultBalance):
        self.defaultPin = defaultPin
        self.defaultBalance = defaultBalance

    def pin_awal(self):
        return self.defaultPin

    def saldo_awal(self):
        return self.defaultBalance

    
