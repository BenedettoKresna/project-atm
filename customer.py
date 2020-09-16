from atm_card import ATMCard

class Customer:
    def __init__(self, id, custPin = 1234, custBalance = 10000):
        self.id = id
        self.custPin = custPin
        self.custBalance = custBalance

    def check_id_customer(self):
        return self.id
    
    def check_pin_customer(self):
        return self.custPin

    def check_balance_customer(self):
        return self.custBalance

    def menu_debet(self, nominal):
        self.custBalance -= nominal

    def menu_simpan(self, nominal):
        self.custBalance += nominal