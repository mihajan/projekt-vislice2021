import random

#NAJPREJ KONSTANTE
STEVILO_DOVOLJENIH_NAPAK = 9

PRAVILNA_CRKA = '+'
PONOVLJENA_CRKA = 'o'
NAPACNA_CRKA = '-'

ZACETEK = 'Z'
ZMAGA = 'W'
PORAZ = 'L'

DATTOEKA_ZA_SHRANJEVANJE = "podatki.json"

class Vislice:

    def __init__(self, zacetne_igre, zacetni_id=0):
        self.igre = zacetne_igre or {}
        self.max_id = zacetni_id

    def pretvori_v_json_slovar(self):
        slovar_ig = {}

        for id_igre, (igre,stanje)in self.igre.items():
            slovar_iger[id_igre]= (
                igra.pretvori_v_json_slovar(),
                stanje
            )
        return {
            "max_id": self.max_id,
            "igre": slovar_iger
        }


@classmethod
def dobi_iz_json_slovarja(cls, slovar):
    slovar_iger = {}
    for id_igre, (igra_slovar, stanje) in slovar["igre"].items():
        slovar_iger[int(id_igre)] = (
            Igra.dobi_iz_json_slovarja(igra_slovar), stanje
        )
    return Vislice(slovar_iger, slovar["max_id"])

@staticmethod
def preberi_iz_datoteke(datoteka):
    with open(datoteka, "r") as in_file:
        json_slovar = json.load(in_file)
    return Vislice.dobi_iz_json_slovarja(json_slovar)


    def zapisi_v_datoteko(self, datoteka):
        with open(datoteka, "w") as out_file:
            json_slovar = self.pretvori_v_json_slovar()
            json.dump(json_slovar, out_file)

    


    def prost_id_igre(self):
        if len(self.igre) == 0:
            return 0
        else:
            return max(self.igre.keys()) + 1

    def nova_igra(self):
        id_igre = self.prost_id_igre()
        igra = nova_igra()
        self.igre[id_igre] = (igra, ZACETEK)
        return id_igre

    def ugibaj(self, id_igre, crka):
        igra, _ = self.igre[id_igre]  # s _ poimenujemo spremenljivko ki jo ne bomo potrebovali
        stanje = igra.ugibaj(crka)
        self.igre[id_igre] = (igra, stanje)



class Igra:
    def __init__(self, geslo, crke):
        self.geslo = geslo.upper() #pravilno geslo
        self.crke = crke.upper() #do sedaj ugibane crke
        #vse stvari v igri so zgolj velike črke

    def napacne_crke(self):
        return [c for c in self.crke if c not in self.geslo]

    def pravilne_crke(self):
        return [c for c in self.crke if c in self.geslo]

    def stevilo_napak(self):
        return len(self.napacne_crke())

    def poraz(self):
        return self.stevilo_napak() > STEVILO_DOVOLJENIH_NAPAK

    def zmaga(self):
        vse_crke = True
        for crka in self.geslo:
            if crka in self.pravilne_crke():
                pass
            else:
                vse_crke = False
                break
        # vse_crke1 = all(crka in self.crke for crka in self.geslo)
        return vse_crke and STEVILO_DOVOLJENIH_NAPAK >= self.stevilo_napak()

    def pravilni_del_gesla(self):
        rezultat = ""
        for c in self.geslo:
            if c in self.crke:
                rezultat += c
            else:
                rezultat += "_ "
        return rezultat

    def nepravilni_ugibi(self):
        return " ".join(self.napacne_crke())

    def ugibaj(self, crka):
        crka = crka.upper()
        if self.poraz():
            return PORAZ
        
        if crka in self.crke:
            return PONOVLJENA_CRKA

        self.crke += crka

        if self.zmaga:
            return ZMAGA
        if crka in self.geslo:
            return PRAVILNA_CRKA
        if self.poraz():
            return PORAZ
        return NAPACNA_CRKA
    
    def pretvori_v_json_slovar(self):
        return {
            "geslo": self.geslo,
            "crke": self.crke,
        }

    @staticmethod
    def dobi_iz_slovarja(slovar):
        return Igra(slovar["geslo"], slovar["crke"])

bazen_besed = []
with open('besede.txt', encoding='utf-8') as input_file:
    bazen_besed = input_file.readlines()

def nova_igra():
    beseda = random.choice(bazen_besed).strip()
    return Igra(beseda, "")


#i = nova_igra(bazen_besed)
#print(i.geslo)
