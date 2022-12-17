class Shakki:

    """ 
    Merkkijonon ensimmäinen kirjain kertoo shakkinappulan värin 
    esim. m tarkoittaa mustaa. Toinen kirjain taas kertoo shakkinappulan nimen esim. 
    K = kuningas, D = daami = kuningatar, L = lähetti ja R = ratsu.
    """

    lauta = [
        "mT", "mR", "mL", "mK", "mD", "mL", "mR", "mT",
        "mS", "mS", "mS", "mS", "ms", "mS", "mS", "mS",
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
    def tulostaLauta(self) -> None:
        for i in range(0, len(self.lauta)):
            if self.lauta[i] != "":
                print(self.lauta[i], end="  ")
            else:
                print("·", end="   ")
            if (i+1) % 8 == 0:
                print("\n")


    
    # Tarkistaa onko nappula ulos laudalta
    def ulosLaudalta(self, koordinaatti: int) -> bool:
        return -1 < koordinaatti < 64

    # Tarkistaa onko lauta vielä siirron jälkeen pelisääntöjen mukainen
    def laillinenLauta() -> None:
        pass


    # Siirtää shakkinappulan laudalla
    def siirto(self, koordinaatti1: int, koordinaatti2: int) -> None:
        self.lauta[koordinaatti2] = self.lauta[koordinaatti1]
        self.lauta[koordinaatti1] = ""
        
    
    # Palauttaa listan kaikista värin laillisista siirroista
    def __laillisetSiirrot(self, vari: int) -> list:
        pass

    # Ratsun lailliset siirrot värin ja koordinaatin perusteella
    def __rLailliset(self, vari: int, koordinaatti: int) -> list:
        pass

    # Lähetin lailliset siirrot värin ja koordinaatin perusteella
    def __lLailliset(self, vari: int, koordinaatti: int) -> list:
        pass

    # Tornin lailliset siirrot värin ja koordinaatin perusteella
    def __tLailliset(self, vari: int, koordinaatti: int) -> list:
        pass

    # Soturin lailliset siirrot värin ja koordinaatin perusteella
    def __sLailliset(self, vari: int, koordinaatti: int) -> list:
        pass


    # Kuninkaan lailliset siirrot värin ja koordinaatin perusteella
    def kLailliset(self, vari: int, koordinaatti: int) -> list:
        pass

    # Daamin lailliset siirrot värin ja koordinaatin perusteella
    def dLailliset(self, vari: int, koordinaatti: int) -> list:
        pass

        

