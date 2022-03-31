import requests


def draco():
    r = requests.post("https://api.mir4global.com/wallet/prices/draco/lastest")
    result = r.json()
    global realdraco
    prince=result.get('Data')
    realdraco=float(prince.get('USDDracoRate'))
    print('valor do draco: %.2f' %realdraco )

def wemix():
    r = requests.post("https://api.mir4global.com/wallet/prices/draco/lastest")
    result = r.json()
    global realwemix
    prince=result.get('Data')
    realwemix=float(prince.get('DracoPriceWemix'))
    print('valor do wemix %.2f' %realwemix)


def real():
    r= requests.get('https://economia.awesomeapi.com.br/last/USD-BRL')
    result = r.json()
    prince=result.get('USDBRL')
    global realdoleta
    realdoleta = float(prince.get('high'))
    print('valor do real %.2f' %realdoleta)
    

def binance():
    r = requests.get("https://api.binance.com/api/v3/ticker/price?",
                 params=dict(symbol="KLAYUSDT"))
    results = r.json()
    global realklay
    realklay=float(results.get('price'))
    print('valor da binance klay %.2f' %realklay)

draco()
wemix()
binance()
real()

  
dracos = float(input('Digite quantos dracos possui: '))

resultado = dracos * ( realdraco * realdoleta )
taxinha = resultado - realklay - realwemix
print('%.2f' %resultado)
print('taxa:%.2f' %taxinha )

input('pressione ENTER para sair..')