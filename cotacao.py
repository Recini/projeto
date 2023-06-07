import requests 

acesso = requests.get("http://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL")

acesso_a = acesso.json()
cotacao_dolar = acesso_a['USDBRL']['bid']
print(cotacao_dolar)
cotacao_euro = acesso_a['EURBRL']['bid']
print(cotacao_euro)
cotacao_bit = acesso_a['BTCBRL']['bid']
print(cotacao_bit)