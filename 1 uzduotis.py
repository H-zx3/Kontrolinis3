# Pirma užduotis - OOP #1:
# Susikurti klasę “BankoSąskaita”, kuri saugotų sąskaitos numerį ir balansą. Klasė turi turėti metodus
# pinigų pridėjimui prie balanso, pinigu išėmimui bei balanso grąžinimui.
#
# Susikurti “BankoSąskaita” klasės objektą ir išbandyti visus metodus bent po vieną kartą.
#
#
# # Create a bank account object
# account = BankAccount("1234567890")
#
# # Deposit funds
# print(account.deposit(1000))
#
# # Withdraw funds
# print(account.withdraw(500))
#
# # Check account balance
# balance = account.get_balance()
# print("Account Balance:", balance)

class Bankosaskaita:                                   #bus iskviesas kai sukursiu banko saskaita
    def __init__(self, saskaitos_numeris):
        self.saskaitos_numeris = saskaitos_numeris
        self.balansas = 0                              #pradinis balansas

    def prideti_pinigus(self, kiekis):
        self.balansas += kiekis                         # prideda pinigus  'kiekis' ir pridedu prie balanso
        return f'Prideta {kiekis} vienetu. Naujas balansas: {self.balansas}'

    def isimti_pinigus(self, kiekis):
        if self.balansas >= kiekis:
           self.balansas -= kiekis                      # isemu pinigus is balanso
           return f'Isimta {kiekis} vienetu. Naujas balansas: {self.balansas}'
        else:
            return 'Nepakanka lesu'

    def parodyti_balansa(self):
        return f'Balansas: {self.balansas}'

saskaita = Bankosaskaita("LT1234567890")   #aktyvuoju class Bankosaskaita

#Pridedu lesas
print(saskaita.prideti_pinigus(1000))

#Issimti lesas
print(saskaita.isimti_pinigus(200))

#Patikrinti balansa
print(saskaita.parodyti_balansa())