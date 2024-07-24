url = 'https://bytebank.com/cambio?moedaOrigem=real'
print(url)

index = url.find('?')

url_base = url[0:index]
print(url_base)

url_parametros = url[20:]
print(url_parametros)