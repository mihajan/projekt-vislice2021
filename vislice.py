import bottle
import model

vislice = model.Vislice()

@bottle.get('/')
def index():
    return bottle.template('index.tpl')

@bottle.post('/igra/')
def nova_igra():
    vislice = model.Vislice.preberi_iz_datoteke(model.DATTOEKA_ZA_SHRANJEVANJE)

    id_igre = vislice.nova_igra()

    vislice.zapisi_v_datoteko(model.DATTOEKA_ZA_SHRANJEVANJE)

    bottle.redirect('/igra/{}/'.format(id_igre)) #preusmeri na drug naslov da ne kompiramo kode

@bottle.get('/igra/<id_igre:int>/')
def pokazi_igro(id_igre):
    igra, stanje = vislice.igre[id_igre]
    return bottle.template('igra.tpl', igra=igra, id_igre=id_igre, stanje=stanje)

@bottle.post('/igra/<id_igre:int>/')
def ugibaj(id_igre):
    crka = bottle.request.forms.getunicode('crka')
    vislice.ugibaj(id_igre, crka)
    bottle.redirect('/igra/{}/'.format(id_igre))

@bottle.get('/img/<picture>') #v špičastih oklepajih je parameter
def serve_picture(picture):
    return bottle.static_file(picture, root='img') #pod root je ime podmape kjer se nahaja

bottle.run(reloader=True, debug=True)