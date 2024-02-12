import sqlite3
from pybit.unified_trading import HTTP
import time
from decouple import config
conexion = sqlite3.connect("eth.db")
cursor = conexion.cursor()
try:
    cursor.execute("create table eth (id integer primary key autoincrement, valor real)")
   
except sqlite3.OperationalError:
    pass
cursor.close()
conexion.close()



# conexion = sqlite3.connect("btc.db")
# cursor = conexion.cursor()
# try:
#     cursor.execute("create table btc (id integer primary key autoincrement, valor real)")

# except sqlite3.OperationalError:
#     pass    
# cursor.close()
# conexion.close()




# conexion = sqlite3.connect("xrp.db")
# cursor = conexion.cursor()
# try:
#     cursor.execute("create table xrp (id integer primary key autoincrement, valor real)")
    
# except sqlite3.OperationalError:
#     pass 
# cursor.close()
# conexion.close()



def insert_eth(valor):
    conexion = sqlite3.connect("eth.db")
    cursor = conexion.cursor()
    cursor.execute("insert into eth (valor) values (?)", (valor,))
    conexion.commit()
    cursor.close()
    conexion.close()

def insert_btc(valor):
    conexion = sqlite3.connect("btc.db")
    cursor = conexion.cursor()
    cursor.execute("insert into btc (valor) values (?)", (valor,))
    conexion.commit()
    cursor.close()
    conexion.close()

def insert_xrp(valor):
    conexion = sqlite3.connect("xrp.db")
    cursor = conexion.cursor()
    cursor.execute("insert into xrp (valor) values (?)", (valor,))
    conexion.commit()
    cursor.close()
    conexion.close()

apiKey = config('BYBIT_API_KEY')
apisecret = config('BYBIT_API_PASS')
session = HTTP(
        testnet=False, 
        api_key=apiKey,
        api_secret=apisecret)
import inspect

methods = inspect.getmembers(session, predicate=inspect.ismethod)
print(methods)

while True:

    eth=session.last_traded_price(symbol="ETHUSDT")
    # btc=session.last_traded_price(symbol="BTCUSDT")
    # xrp=session.last_traded_price(symbol="XRPUSDT")
    eth=float(eth['result']['price'])
    # btc=float(btc['result']['price'])
    # xrp=float(xrp['result']['price'])
    insert_eth(eth)
    # insert_btc(btc)
    # insert_xrp(xrp)
    time.sleep(120)
    




