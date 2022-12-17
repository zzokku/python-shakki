class Shakki:

    """ 
    Merkkijonon ensimmäinen kirjain kertoo shakkinappulan värin 
    esim. m tarkoittaa mustaa. Toinen kirjain taas kertoo shakkinappulan nimen esim. 
    K = kuningas, D = daami = kuningatar, L = lähetti ja R = ratsu.
    """

    lauta = [
        "mT", "mR", "mL", "mK", "mD", "mL", "mR", "mT",
        "mS", "mS", "mS", "mS", "mS", "mS", "mS", "mS",
        "", "", "", "", "", "", "", "",
        "", "", "", "", "", "", "", "",
        "", "", "", "", "", "", "", "",
        "", "", "", "", "", "", "", "",
        "vS", "vS", "vS", "vS", "vS", "vS", "vS", "vS",
        "vT", "vR", "vL", "vD", "vK", "vL", "vT", "vT"
    ]

    def __init__(self) -> None:
        pass

    # Tulostaa pelihetkeä vastaavan laudan "väärinpäin"
    def tulostaVaarinpain(self) -> str:
        return self.lauta

    # Tulostaa pelihetkeä vastaavan laudan
    def tulostaLauta(self, plauta: list) -> None:
        for i in range(0, len(plauta)):
            if plauta[i] != "":
                print(plauta[i], end="  ")
            else:
                print("·", end="   ")
            if (i+1) % 8 == 0:
                print("\n")

    def pelilauta(self) -> None:
        self.tulostaLauta(self.lauta)
    
    # Tarkistaa onko nappula ulos laudalta
    def ulosLaudalta(self, koordinaatti: int) -> bool:
        return -1 < koordinaatti < 64

    # Tarkistaa onko lauta vielä siirron jälkeen pelisääntöjen mukainen
    def laillinenLauta() -> None:
        pass

    # Palauttaa laudan, joka sisältää ainoastaan valitun nappularyhman nappulat.
    def nappulaRyhma(self, vari: str, ryhma: str) -> list:
        return [(vari+ryhma) if i == (vari+ryhma) else "" for i in self.lauta]
        

    # Siirtää shakkinappulan laudalla
    def siirto(self, koordinaatti1: int, koordinaatti2: int) -> None:
        self.lauta[koordinaatti2] = self.lauta[koordinaatti1]
        self.lauta[koordinaatti1] = ""
        
    
    # Palauttaa listan kaikista värin laillisista siirroista
    def __laillisetSiirrot(self, vari: str) -> list:
        pass

    # Ratsun lailliset siirrot värin ja koordinaatin perusteella
    def __rLailliset(self, vari: str, koordinaatti: int) -> list:
        pass

    # Lähetin lailliset siirrot värin ja koordinaatin perusteella
    def __lLailliset(self, vari: str, koordinaatti: int) -> list:
        pass

    # Tornin lailliset siirrot värin ja koordinaatin perusteella
    def __tLailliset(self, vari: str, koordinaatti: int) -> list:
        pass

    # Soturin lailliset siirrot värin ja koordinaatin perusteella
    def __sLailliset(self, vari: str, koordinaatti: int) -> list:
        pass

    # Kuninkaan lailliset siirrot värin ja koordinaatin perusteella
    def kLailliset(self, vari: str, koordinaatti: int) -> list:
        pass

    # Daamin lailliset siirrot värin ja koordinaatin perusteella
    def dLailliset(self, vari: str, koordinaatti: int) -> list:
        pass

        

