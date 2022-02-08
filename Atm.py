class Atm:

    def __init__(self, atmCardNumber, pinNumber):
        self.atmCardNumber = atmCardNumber
        self.pinNumber = pinNumber

    def CashWithdrawl(self):
        print("CashWithDrawl")

    def Balance_enquiry(self):
        print("BalanceEnquiry")

def main():
     
     atmpin = Atm("pin = xyz", "balance = 1500" )

     atmpin.CashWithdrawl()
     atmpin.Balance_enquiry()

main()
