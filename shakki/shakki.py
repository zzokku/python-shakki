class Shakki:

    """ 
    Merkkijonon ensimmäinen kirjain kertoo shakkinappulan värin 
    esim. m tarkoittaa mustaa. Toinen kirjain taas kertoo shakkinappulan nimen esim. 
    K = kuningas, D = daami = kuningatar, L = lähetti ja R = ratsu.

    Merkkijono ("x") tarkoittaa, että ruutu on laudan ulkopuolella
    Tyhjä merkkijono välilyönnillä (" ") tarkoittaa tyhjää ruutua.
    """

    lauta = [
        "x", "x", "x", "x", "x", "x", "x", "x", "x","x",
        "x", "x", "x", "x", "x", "x", "x", "x", "x","x",
        "x", "mT", "mR", "mL", "mK", "mD", "mL", "mR", "mT","x",
        "x", "mS", "mS", "mS", "mS", "mS", "mS", "mS", "mS","x",
        "x", " ", " ", " ", " ", " ", " ", " ", " ","x",
        "x", " ", " ", " ", " ", " ", " ", " ", " ","x",
        "x", " ", " ", " ", " ", " ", " ", " ", " ","x",
        "x", " ", " ", " ", " ", " ", " ", " "," ","x",
        "x", "vS", "vS", "vS", "vS", "vS", "vS", "vS", "vS","x",
        "x", "vT", "vR", "vL", "vD", "vK", "vL", "vR", "vT","x",
        "x", "x", "x", "x", "x", "x", "x", "x", "x", "x",
        "x", "x", "x", "x", "x", "x", "x", "x", "x", "x",
    ]

    # Alkuperäinen lauta johon verrata tietyissä tilanteissa
    alkuperainen_lauta: list

    # Kirjanpito laudalla tapahtuineista siirroista
    siirrot: list

    lMetodit: list

    shakkiKoordinaatit = {}


    def __init__(self) -> None:
        # Asetetaan alkuperäinen lauta
        self.alkuperainen_lauta = self.lauta

        # Metodit eri nappuloiden laillisille siirroille
        self.lMetodit = {
            "S": self.sLailliset,
            "L": self.lLailliset,
            "R": self.rLailliset,
            "T": self.tLailliset,
            "K": self.kLailliset,
            "D": self.dLailliset
        }
        # Koordinaatisto
        self.koordinaatit()
       
    

    def koordinaatit(self) -> None:
        # Lisätään koordinaatisto sanakirjaan
        a = 91
        k = 0
        for s in "abcdefgh":
            for i in range(1, 9):
                self.shakkiKoordinaatit[s+str(i)] = a
                a-=10
            k += 1
            a = 91 + k


    # Tulostaa pelihetkeä vastaavan laudan "väärinpäin"
    # TODO: logiikka
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

    # Tulostaa pelitilannetta vastaavan pelilaudan
    def pelilauta(self) -> None:
        self.tulostaLauta(self.lauta)
    
    # Tarkistaa onko nappula ulos laudalta
    def laudanSisalla(self, koordinaatti: int) -> bool:
        return self.lauta[koordinaatti] != "x"

    # Tarkistaa onko lauta vielä siirron jälkeen pelisääntöjen mukainen
    def laillinenLauta() -> None:
        pass

    # Palauttaa listan, joka sisältää tietyn nappularyhmän nappuloiden koordinaatit
    def nappulaRyhma(self, vari: str, tyyppi: str) -> list:
        return [i for i in range (20, len(self.lauta)-19) if self.lauta[i] == (vari+tyyppi)]
    
    # Selvitetään onko koordinaatin nappula liikkunut
    def __eiLiikkunut(self, koordinaatti: int) -> list:
        return self.lauta[koordinaatti] == self.alkuperainen_lauta[koordinaatti]

    # Siirtää shakkinappulan laudalla
    # TODO: pseudo laillisen siirron tarkistus
    def siirto(self, koordinaatti1: int, koordinaatti2: int) -> None:
        if koordinaatti2 in self.lMetodit[self.lauta[koordinaatti1][1]](self.lauta[koordinaatti1][0], [koordinaatti1]):
            self.lauta[koordinaatti2] = self.lauta[koordinaatti1]
            self.lauta[koordinaatti1] = " "

        
    # Palauttaa vastakkaisen varin
    def vastVari(self, vari: str) -> str:
        return "v" if vari == "m" else "m"


    # Palauttaa listan kaikista värin laillisista siirroista
    def __laillisetSiirrot(self, vari: str) -> list:
        pass

    # TODO: korjauksia
    # 
    def ruutuHyokatty(self, vari: str, koordinaatti: int) -> bool:
        koords = self.varinNappulat(vari)
        for i in koords:
            if koordinaatti in self.lMetodit[self.lauta[i][1]](vari, [i]):
                return True
        return False

    
    # Palauttaa listan kaikista ruuduista, mikä on hyökätty liukuvan nappulan toimesta.
    def liukuvatHyokkaajat(self, vari: str) -> list:
        ruudut = []
        return ruudut


    # Ratsun lailliset siirrot värin ja koordinaatin perusteella
    # ratsun loikat: [21, -21, 8,-8,-13, 13, 19, -19, -12, 12]
    def rLailliset(self, vari: str, koordinaatit: list) -> list:
        lailliset = []
        vastavari = self.vastVari(vari)

        for k in koordinaatit:
            for l in [21, -21, 8,-8,-13, 13, 19, -19, -12, 12]:
                if self.lauta[k+l][0] in [" ", vastavari]:
                    lailliset.append(k+l)
        return lailliset
            

    # TODO: yleinen metodi liukuville nappuloille ???
    # Lähetin lailliset siirrot värin ja koordinaatin perusteella

    def lLailliset(self, vari: str, koordinaatit: list) -> list:
        lailliset = []
        suunnat = [-11, 11, -9, 9]
        for i in koordinaatit:
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

    def tLailliset(self, vari: str, koordinaatit: list) -> list:
        lailliset = []
        suunnat = [1, -1 , -10, 10]
        for i in koordinaatit:
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
    def sLailliset(self, vari: str, koordinaatit: list) -> list:

        """ 
        Asetetaan siirtoja varten kerroin k, joko positiiviseksi (nappulaa siirretään eteenpäin listassa)
        tai negatiiviseksi (nappulaa siirretään taaksepäin listassa).
        """
        k = 1
        if vari == "v":
            k = -1

        lailliset = [i for i in koordinaatit if self.lauta[i+(11*k)][0] == self.vastVari(vari) or self.lauta[i+(9*k)][0] == self.vastVari(vari)]

        for j in koordinaatit:
            if self.lauta[j+(10*k)] == " ":
                lailliset.append(j+(10*k))
                if self.__eiLiikkunut(j):
                    lailliset.append(j+(20*k))
        return lailliset
            
    # Kuninkaan lailliset siirrot värin ja koordinaatin perusteella
    # TODO: tarkista onko ruutu, johon kuningas siirretään hyökätty.
    def kLailliset(self, vari: str, koordinaatit: list) -> list:
        lailliset = []
        vastavari = self.vastVari()
        for k in koordinaatit:
            for s in [10, -10, 11, -11, 1, -1, 9, -9]:
                if self.lauta[k+s][0] in [" ", vastavari] and not self.ruutuHyokatty(k+s):
                    lailliset.append(k+s)
        return lailliset

    # Daamin lailliset siirrot värin ja koordinaatin perusteella
    def dLailliset(self, vari: str, koordinaatti: list) -> list:
        return self.lLailliset(vari, koordinaatti) + self.tLailliset(vari, koordinaatti)

    def linnoitusTarkistus(self, vari: str) -> int:
        pass
    
    def linnoitus(self, vari: str, puoli: int) -> None:
        pass

    def indeksitKoordinaateiksi(self, indeksit):
        return [i for i in list(self.shakkiKoordinaatit.keys()) if self.shakkiKoordinaatit[i] in indeksit]

    def varinNappulat(self, vari: str):
        return [i for i in range(21, 90) if self.lauta[i][0] == vari]
