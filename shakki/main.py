from shakki import Shakki

shakki = Shakki()

def peli():
    shakki.pelilauta()
    vuoro = "v"
    while True:

        siirrettava = input("syötä siirrettävän koordinaatti: ")
        siirto = input("syötä siirron koordinaatti: ")

        k1 = shakki.shakkiKoordinaatit[siirrettava] 
        k2 = shakki.shakkiKoordinaatit[siirto]
        
        if not shakki.siirto(k1, k2):
            if shakki.lauta[k1][0] != vuoro:
                print("Siirto epäonnistui.")
                continue

        vuoro = shakki.vastVari(vuoro)
        shakki.pelilauta()

peli()


        