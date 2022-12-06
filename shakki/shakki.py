class Shakki:

    """ 
    Merkkijonon ensimmäinen kirjain kertoo shakkinappulan värin 
    esim. m tarkoittaa mustaa. Toinen / kolmas kirjain taas kertoo shakkinappulan nimen esim. 
    kg = kuningas, k = kuningatar, l = lähetti ja r = ratsu.
    """

    lauta = [
        ["mt", "mr", "ml", "mkg", "mk", "ml", "mr", "mt"],
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

    def __siirronPatevyys(self, koordinaatti1: int, koordiaatti2: int):
        pass

    # Siirtää shakkinappulan
    def siirto(self, koordinaatti1: int, koordinaatti2: int) -> bool:
        if self.siirronPatevyys:
            return True
        return False
    
    # Palauttaa listan kaikista värin laillisista siirroista
    def __laillisetSiirrot(self, vari: str) -> list:
        pass

    # Ratsun lailliset siirrot värin ja koordinaatin perusteella
    def __rLailliset(self, vari: str, koordinaatti: int) -> list:
        pass

    def __lLailliset(self, vari: str, koordinaatti: int) -> list:
        pass

    def __tLailliset(self, vari: str, koordinaatti: int) -> list:
        pass

    def __sLailliset(self, vari: str, koordinaatti: int) -> list:
        pass

    def kgLailliset(self, vari: str, koordinaatti: int) -> list:
        pass

        

