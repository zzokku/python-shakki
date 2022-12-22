from shakki import Shakki


shakki = Shakki()

shakki.pelilauta()
soturit = shakki.nappulaRyhma("m", "S")
ratsut = shakki.nappulaRyhma("v", "R")
print(shakki.rLailliset("v", ratsut))
print(shakki.dLailliset("v", shakki.nappulaRyhma("v", "D")))
