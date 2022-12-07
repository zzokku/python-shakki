class Shakki:

    """ 
    Merkkijonon ensimmäinen kirjain kertoo shakkinappulan värin 
    esim. m tarkoittaa mustaa. Toinen / kolmas kirjain taas kertoo shakkinappulan nimen esim. 
    k = kuningas, d = daami = kuningatar = , l = lähetti ja r = ratsu.
    """

    lauta = [
        ["mt", "mr", "ml", "md", "mk", "ml", "mr", "mt"],
        ["ms", "ms", "ms", "ms", "ms", "ms", "ms", "ms"],
        ["", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", ""],
        ["vs", "vs", "vs", "vs", "vs", "vs", "vs", "vs"],
        ["vt", "vr", "vl", "vk", "vkg", "vl", "vr", "vt"]
    ]

    def __init__(self) -> None:
        pass

    # Tulostaa pelihetkeä vastaavan laudan "väärinpäin"
    def tulostaVaarinpain(self) -> str:
        return self.lauta

    # Tulostaa pelihetkeä vastaavan laudan
    def tulostaLauta(self) -> str:
        return str(self.lauta)

    # str metodi tulostaa saman kuin metodi tulostaLauta
    def __str__(self) -> str:
        return self.tulostaLauta

    def ulosLaudalta(self, koordinaatti1: tuple, koordiaatti2: tuple) -> bool:
        for alkio in koordinaatti1+koordiaatti2:
            if not -1 < alkio < 8:
                return True
        return False

    # Siirtää shakkinappulan laudalla
    def siirto(self, koordinaatti1: tuple, koordinaatti2: tuple) -> None:
        self.board[koordinaatti2[0]][koordinaatti2[1]] = self.board[koordinaatti1[0]][koordinaatti1[1]]
        self.board[koordinaatti1[0]][koordinaatti1[1]] = ""
        
    
    # Palauttaa listan kaikista värin laillisista siirroista
    def __laillisetSiirrot(self, vari: str) -> list:
        pass

    # Ratsun lailliset siirrot värin ja koordinaatin perusteella
    def __rLailliset(self, vari: str, koordinaatti: tuple) -> list:
        pass

    # Lähetin lailliset siirrot värin ja koordinaatin perusteella
    def __lLailliset(self, vari: str, koordinaatti: tuple) -> list:
        pass

    # Tornin lailliset siirrot värin ja koordinaatin perusteella
    def __tLailliset(self, vari: str, koordinaatti: tuple) -> list:
        pass

    # Soturin lailliset siirrot värin ja koordinaatin perusteella
    def __sLailliset(self, vari: str, koordinaatti: tuple) -> list:
        pass

    # Kuninkaan lailliset siirrot värin ja koordinaatin perusteella
    def kLailliset(self, vari: str, koordinaatti: tuple) -> list:
        pass

    # Daamin lailliset siirrot värin ja koordinaatin perusteella
    def dLailliset(self, vari: str, koordinaatti: tuple) -> list:
        pass

        

