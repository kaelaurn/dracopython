import requests





def draco():
    r = requests.post("https://api.mir4global.com/wallet/prices/draco/lastest").json()
    global realdraco
    prince=r.get('Data')
    realdraco=float(prince.get('USDDracoRate'))
    print('valor do draco: %.2f' %realdraco )

def wemix():
    r = requests.post("https://api.mir4global.com/wallet/prices/draco/lastest").json()
    global realwemix
    prince=r.get('Data')
    realwemix=float(prince.get('DracoPriceWemix'))
    print('valor do wemix %.2f' %realwemix)


def real():
    r= requests.get('https://economia.awesomeapi.com.br/last/USD-BRL').json()
    prince=r.get('USD')
    global realdoleta
    realdoleta=float(prince.get('high'))
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









  
dracos = float(input('Digite quantos dracos possui: '))

resultado = dracos * ( realdraco * realdoleta )
taxinha = resultado - realklay - realwemix
print('Sem taxa: %.2f' %resultado)
print('Taxa: %.2f' %taxinha )

input('pressione ENTER para sair..')


