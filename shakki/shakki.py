class Shakki:

    """ 
    Merkkijonon ensimmäinen kirjain kertoo shakkinappulan värin 
    esim. m tarkoittaa mustaa. Toinen kirjain taas kertoo shakkinappulan nimen esim. 
    K = kuningas, D = daami = kuningatar, L = lähetti ja R = ratsu.

    Tyhjä merkkijono ("") tarkoittaa, että ruutu on laudan ulkopuolella
    Tyhjä merkkijono välilyönnillä (" ") tarkoittaa tyhjää ruutua.

    """

    lauta = [
        "", "", "", "", "", "", "", "", "", ""
        "", "mT", "mR", "mL", "mK", "mD", "mL", "mR", "mT","",
        "", "mS", "mS", "mS", "mS", "mS", "mS", "mS", "mS","",
        "", " ", " ", " ", " ", " ", " ", " ", " ","",
        "", " ", " ", " ", " ", " ", " ", " ", " ","",
        "", " ", " ", " ", " ", " ", " ", " ", " ","",
        "", " ", " ", " ", " ", " ", " ", " ", " ","",
        "", "vS", "vS", "vS", "vS", "vS", "vS", "vS", "vS","",
        "", "vT", "vR", "vL", "vD", "vK", "vL", "vR", "vT","",
        "", "", "", "", "", "", "", "", "", ""
    ]
    # Alkuperäinen lauta johon verrata tietyissä tilanteissa
    alkuperainen_lauta: list

    # Kirjanpito laudalla tapahtuineista siirroista
    siirrot: list

    def __init__(self) -> None:
        self.alkuperainen_lauta = self.lauta

    # Tulostaa pelihetkeä vastaavan laudan "väärinpäin"
    def tulostaVaarinpain(self) -> str:
        return self.lauta

    # Tulostaa pelihetkeä vastaavan laudan
    def tulostaLauta(self, plauta: list) -> None:
        for i in range(0, len(plauta)):
            if len(plauta[i]) > 1:
                print(plauta[i], end="  ")
            if plauta[i] == " ":
                print("·", end="   ")
            if (i+1) % 10 == 0:
                print("\n")

    def pelilauta(self) -> None:
        self.tulostaLauta(self.lauta)
    
    # Tarkistaa onko nappula ulos laudalta
    def laudanSisalla(self, koordinaatti: int) -> bool:
        return self.lauta[koordinaatti] != ""

    # Tarkistaa onko lauta vielä siirron jälkeen pelisääntöjen mukainen
    def laillinenLauta() -> None:
        pass

    # Palauttaa listan, joka sisältää tietyn nappularyhmän nappuloiden koordinaatit
    def nappulaRyhma(self, vari: str, tyyppi: str) -> list:
        return [i for i in range (0, len(self.lauta)) if self.lauta[i] == (vari+tyyppi)]
    
    # Selvitetään onko koordinaatin nappula liikkunut
    def __onkoLiikkunut(self, koordinaatti: int) -> list:
        return self.lauta[koordinaatti] == self.alkuperainen_lauta[koordinaatti]

    # Siirtää shakkinappulan laudalla
    def siirto(self, koordinaatti1: int, koordinaatti2: int) -> None:
        self.lauta[koordinaatti2] = self.lauta[koordinaatti1]
        self.lauta[koordinaatti1] = " "
    
    # Palauttaa vastakkaisen varin
    def vastVari(self, vari: str) -> str:
        if vari == "v":
            return "m"
        return "v"

    # Palauttaa listan kaikista värin laillisista siirroista
    def __laillisetSiirrot(self, vari: str) -> list:
        pass

    def hyokkaajatLauta(self, vari: str) -> list:
        pass

    # Ratsun lailliset siirrot värin ja koordinaatin perusteella
    def __rLailliset(self, vari: str) -> list:
        pass
    
    # TODO: yleinen metodi liukuville nappuloille ???
    # Lähetin lailliset siirrot värin ja koordinaatin perusteella

    def lLailliset(self, vari: str) -> list:
        lailliset = []
        suunnat = [-11, 11, -9, 9]
        for i in self.nappulaRyhma(vari, "L"):
            for j in suunnat:
                c = 1
                siirto = i+(c*j)
                while self.laudanSisalla(siirto):
                    siirto = i+(c*j)
                    c+=1
                    if self.lauta[siirto][0] == self.vastVari(vari):
                        lailliset.append(siirto)
                        break
                    if self.lauta[siirto] == " ":
                         lailliset.append(siirto)
                    else:
                        break
  
        return lailliset
    
    # TODO: yleinen metodi liukuville nappuloille ???
    # Tornin lailliset siirrot värin ja koordinaatin perusteella

    def tLailliset(self, vari: str) -> list:
        lailliset = []
        suunnat = [1, -1 , -10, 10]
        for i in self.nappulaRyhma(vari, "T"):
            for j in suunnat:
                c = 1
                siirto = i+(c*j)
                while self.laudanSisalla(siirto):
                    siirto = i+(c*j)
                    c+=1
                    if self.lauta[siirto][0] == self.vastVari(vari):
                        lailliset.append(siirto)
                        break
                    if self.lauta[siirto] == " ":
                        lailliset.append(siirto)
                    else:
                        break     
        return lailliset



        

    # Soturin lailliset siirrot värin ja koordinaatin perusteella

    # TODO: siirron TÄYDELLINEN laillisuus
    def sLailliset(self, vari: str) -> list:

        lailliset = []

        """ 
        Asetetaan siirtoja varten kerroin k, joko positiiviseksi (nappulaa siirretään eteenpäin listassa)
        tai negatiiviseksi (nappulaa siirretään taaksepäin listassa).
        """

        k = 1
        if vari == "v":
            k = -1

        for i in self.nappulaRyhma(vari, "S"):
            if self.lauta[i+(8*k)] == " " and self.laudanSisalla(i+(8*k)):
                lailliset.append(i+(8*k))
                if self.__onkoLiikkunut:
                    lailliset.append(i+(16*k))

        return lailliset
            


            

    # Kuninkaan lailliset siirrot värin ja koordinaatin perusteella
    def kLailliset(self, vari: str) -> list:
        pass

    # Daamin lailliset siirrot värin ja koordinaatin perusteella
    def dLailliset(self, vari: str) -> list:
        pass

        

