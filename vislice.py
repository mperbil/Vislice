import bottle
import model

vislice = model.Vislice()

@bottle.get('/')
def index():
    return bottle.template('indeks.tpl')

@bottle.post('/igra/')
def nova_igra():
    id = vislice.nova_igra()
    bottle.redirect('/igra/{}/'.format(id))

@bottle.get('/igra/<id_igre:int>/')
def pokazi_igro(id_igre):
    igra, stanje = vislice.igre[id_igre]
    return bottle.template('igra.tpl', igra=igra, stanje=stanje, id_igre=id_igre)




bottle.run(reloader=True, debug=True)