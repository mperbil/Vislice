import bottle
import model
SKRIVNOST = 'moja_skrivnost'
vislice = model.Vislice()

@bottle.get('/')
def index():
    return bottle.template('index.tpl')

@bottle.post('/nova_igra/')
def nova_igra():
    id = vislice.nova_igra()
    bottle.response.set_cookie("idigre", "idigre{0}".format(id), secret=SKRIVNOST, path='/')
    bottle.redirect('/igra/')

@bottle.get('/igra/')
def pokazi_igro():
    id_igre = int(bottle.request.get_cookie("idigre", secret=SKRIVNOST).split('e')[1])
    igra, stanje = vislice.igre[id_igre]
    return bottle.template('igra.tpl', igra=igra, stanje=stanje)

@bottle.post('/igra/')
def ugibaj():
    id_igre= int(bottle.request.get_cookie("idigre", secret=SKRIVNOST).split('e')[1])
    crka = bottle.request.forms.getunicode('crka')
    vislice.ugibaj(id_igre, crka)
    bottle.redirect('/igra/')

@bottle.get('/img/<picture>')
def serve_pictures(picture):
    return bottle.static_file(picture, root="img")




bottle.run(reloader=True, debug=True)