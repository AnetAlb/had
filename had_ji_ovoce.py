'''
Přidej do hry hadí potravu. Tady jsou pravidla pro vegetariánského hada, ale můžeš si je změnit podle chuti:
Seznam ovoce obsahuje na začátku jedno ovoce na políčku, na kterém není had (například: [(2, 3)] znamená
jedno ovoce na pozici (2, 3)). Když had sežere ovoce, vyroste („nesmaže“ se mu ocas, tedy neprovede se to,
cos přidala v projektu 13), a pokud na mapě zrovna není další ovoce, na náhodném místě (kde není had) vyroste ovoce nové.
Každých 30 tahů vyroste nové ovoce samo od sebe.
Na mapě se toto tajemné ovoce zobrazuje jako otazník (?).
'''

souradnice = [(0, 0), (1, 0), (2, 0)]

tabulka  =   [['.', '.', '.','.', '.', '.' ,'.', '.', '.','.']
            , ['.', '.', '.','.', '.', '.', '.', '.', '.','.']
            , ['.', '.', '.','.', '.', '.', '.', '.', '.','.']
            , ['.', '.', '.','.', '.', '.', '.', '.', '.','.']
            , ['.', '.', '.','.', '.', '.', '.', '.', '.','.']
            , ['.', '.', '.','.', '.', '.', '.', '.', '.','.']
            , ['.', '.', '.','.', '.', '.', '.', '.', '.','.']
            , ['.', '.', '.','.', '.', '.', '.', '.', '.','.']
            , ['.', '.', '.','.', '.', '.', '.', '.', '.','.']
            , ['.', '.', '.','.', '.', '.', '.', '.', '.','.']]

sez_smeru = ['s', 'j', 'v', 'z']


def pohyb(souradnice):
    while True:
        smer='nesmysl'
        print()

        while smer not in sez_smeru:
            smer = input("Zadej stranu: ")

        prvni_pozice=souradnice[-1][0] #posledni pozice listu a jeji prvni cast
        druha_pozice=souradnice[-1][1]
        #print(souradnice)
        if smer=='v':
            zmena=prvni_pozice+1
            souradnice.append((zmena, druha_pozice))
            #print(souradnice)
            #return(souradnice)

        if smer=='z':
            zmena=prvni_pozice-1
            souradnice.append((zmena, druha_pozice))

        if smer=='s':
            zmena=druha_pozice-1
            souradnice.append((prvni_pozice, zmena))

        if smer=='j':
            zmena=druha_pozice+1
            souradnice.append((prvni_pozice, zmena))

        #print(souradnice)
        #navraci do tabulku . na mista odkud se hnul had
        nulta_pozice=souradnice[0][0]
        #print(nulta_pozice)
        nulta_pozice_b=souradnice[0][1]
        #print(nulta_pozice_b)
        tabulka[nulta_pozice_b][nulta_pozice ] = '.'
        #print(tabulka)
        print(souradnice)
        souradnice.pop(0)
        print(souradnice)
        print(souradnice[0])
        print(souradnice[2])
        #print(tabulka)
        #return(souradnice)
        #pohyb(souradnice)
        #def tabulka(souradnice):

        #had nesmi hrat na pole kde uz je
        if souradnice[2]!=souradnice[0]:
            pass
        else:
            raise RuntimeError("Chyba1")

        #had nesmi hrat nesmi vyjet z pole
        if (souradnice[-1][0] in [-1,10]) or (souradnice[-1][1] in [-1,10]):
            raise IndexError("Chyba2")

        for tup in souradnice:
            #print(tup)
            sloupec = (tup[0])
            radek = (tup[1])
            tabulka[radek][sloupec] = 'x'
            #print(tabulka)


        for radek in tabulka:
            print()
            for tecka in radek:
                print(tecka, end=' ')
        #print(tabulka_vzor)
        #print(tabulka)

#tabulka(souradnice)
try:
    pohyb(souradnice)
except RuntimeError:
    print("Na toto pole nejde hrat, had zde jiz je.")
except IndexError:
    print("Had narazil do zdi. Au!")
