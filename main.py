url = 'bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar'

url = url.strip()

if url == '':
    raise ValueError('A URL está vazia')

print(url)

index_interrogacao = url.find('?')

url_base = url[:index_interrogacao]
print(url_base)

url_parametros = url[index_interrogacao+1:]
print(url_parametros)

parametro_busca = 'moedaOrigem'
index_parametro = url_parametros.find(parametro_busca)
index_valor = index_parametro + len(parametro_busca) + 1
index_e_comercial = url_parametros.find('&', index_valor)
if index_e_comercial == -1:
    valor = url_parametros[index_valor:]

else:
    valor = url_parametros[index_valor:index_e_comercial]

print(valor)