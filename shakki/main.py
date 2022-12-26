from shakki import Shakki

shakki = Shakki()
def peli():
    shakki.pelilauta()
    vuoro = "v"
    while True:
        
            print(vuoro)
            siirrettava = input("syötä siirrettävän koordinaatti: ")
            k1 = shakki.shakkiKoordinaatit[siirrettava] 
            print(shakki.sLailliset(vuoro, [k1], True))
           
            siirto = input("syötä siirron koordinaatti: ")
            k2 = shakki.shakkiKoordinaatit[siirto]

            shakki.siirto(k1, k2, False)
            vuoro = shakki.vastVari(vuoro)
            shakki.pelilauta()

       


peli()


        