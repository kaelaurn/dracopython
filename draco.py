import requests


def draco():
    r = requests.post("https://api.mir4global.com/wallet/prices/draco/lastest").json()
    global realdraco
    price=r.get('Data')
    realdraco=float(price.get('USDDracoRate'))
    print('valor do draco: %.2f' %realdraco )

def wemix():
    r = requests.post("https://api.mir4global.com/wallet/prices/draco/lastest").json()
    global realwemix
    price=r.get('Data')
    realwemix=float(price.get('DracoPriceWemix'))
    print('valor do wemix %.2f' %realwemix)


def real():
    r= requests.get('https://economia.awesomeapi.com.br/last/USD-BRL').json()
    #get the first value of a tuple
    naoadiantamudar= list(r)[0]
    price=r.get(naoadiantamudar)
    global realdoleta
    realdoleta=float(price.get('high'))
    print('valor do real %.2f' %realdoleta)

   

def binance():
    r = requests.get("https://api.binance.com/api/v3/ticker/price?",
                        params=dict(symbol="KLAYUSDT")).json()
    global realklay
    realklay=float(r.get('price'))
    print('valor da binance klay %.2f' %realklay)

draco()
wemix()
real()
binance()









def resultados():
    dracos = float(input('Digite quantos dracos possui: '))

    resultado = dracos * ( realdraco * realdoleta )
    taxinha = resultado - realklay - realwemix
    return ('Sem taxa: %.2f' %resultado) + ('\nCom taxa: %.2f' %taxinha)

print(resultados())


input('pressione ENTER para sair..')


