from shakki import Shakki

shakki = Shakki()

def peli():
    shakki.pelilauta()
    vuoro = "v"
    while True:
        try:
            siirrettava = input("syötä siirrettävän koordinaatti: ")
            k1 = shakki.shakkiKoordinaatit[siirrettava] 
            print(shakki.indeksitKoordinaateiksi(shakki.lMetodit[shakki.lauta[k1][1]](vuoro, [k1])))

            siirto = input("syötä siirron koordinaatti: ")
            k2 = shakki.shakkiKoordinaatit[siirto]

            shakki.siirto(k1, k2)
            vuoro = shakki.vastVari(vuoro)
            shakki.pelilauta()
        except:
            print("Siirto epäonnistui")
            continue

peli()


        