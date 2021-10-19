from enum import Enum

class WithdrawalStatus(Enum):
    Ok = 0,
    SaldoTooLow = 1,
    AmountTooBig = 2


class Account:
    def __init__(self, kontonummer : str): # Constructor = en helt vanlig metod. VALID STATE
        self._kontonummer = ""
        self._saldo = 0
        if self.setKontonummer(kontonummer) == False:
            raise ValueError("10 tecken tack")
        

    
    def setKontonummer(self,kontonummer: str) -> bool:
        if(len(kontonummer) != 10):
            return False
        self._kontonummer = kontonummer
        return True

    def withdraw(self, belopp : int) -> WithdrawalStatus:
        # om måndag
        if belopp > 3000:
            return WithdrawalStatus.AmountTooBig
        if belopp > self._saldo:
            return WithdrawalStatus.SaldoTooLow
        self._saldo = self._saldo - belopp
        return  WithdrawalStatus.Ok


while True:
    try:
        knr = input("Ange kontonummer:")
        acc = Account(knr)
        break
    except:
        print("Åhh felaktigt kontonummer")


status = acc.withdraw(100)
if(status == WithdrawalStatus.Ok):
    print("japp uttaget")
elif (status == WithdrawalStatus.AmountTooBig):
    print("Max 3000 pert dag")
elif(status == WithdrawalStatus.SaldoTooLow):    
    print("Max 3000 pert dag")

