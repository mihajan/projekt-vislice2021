import model

def izpis_igre(igra):
    return (
        f"Igraš igro vislic:\n" +
        f"Narobe ugibane črke so: {igra.nepravilni_ugibi()}\n" +
        f"Trenutno stanje besed:{igra.pravilni_del_gesla()}\n"
    )

def izpis_poraza(igra):
    return (
        f"\nIzgubil si, več sreče prihodnjič.\n" +
        f"Tvoji napačni ugibi so bili: {igra.nepravilni_ugibi()}\n" +
        f"Pravilno si uganil: {igra.pravilni_del_gesla()}\n" +
        f"Pravilno geslo je bilo: {igra.geslo}"
    )

def izpis_zmage(igra):
    return (
        f"Zmagal si, bravo.\n" +
        f"Narobe si uganil {igra.nepravilni_ugibi()}\n" +
        f"Pravilno geslo je bilo: {igra.geslo}" +
        f"Potreboval si {len(igra.crka)}"
    )

def pozeni_vmesnik():
    igra = model.nova_igra()
    while True:
        if igra.zmaga():
            print(izpis_zmage(igra))
            break
        elif igra.poraz():
            print(izpis_poraza(igra))
            break
        else:
            print(izpis_igre(igra))
            vnos = input("Vnesi novo crko:")
            igra.ugibaj(vnos)

pozeni_vmesnik()








#igra = model.Igra('banana', "")
#print(izpis_igre(igra))
#igra.ugibaj('b')
#print(izpis_igre(igra))
#igra.ugibaj('c')
#igra.ugibaj('n')
#igra.ugibaj('a')
#print(izpis_igre(igra))
#print(izpis_poraza(igra))