import re

class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            raise ValueError('A URL está vazia')
    
    def valida_url(self):
        if not self.url:
            raise ValueError('A URL está vazia')
        
        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(self.url)
        if not match:
            raise ValueError("A URL não é válida.")
    
    def get_url_base(self):
        index_interrogacao = self.url.find('?')
        url_base = self.url[:index_interrogacao]
        return url_base

    def get_url_parametros(self):
        index_interrogacao = self.url.find('?')
        url_parametros = self.url[index_interrogacao + 1 :]
        return url_parametros
    
    def get_valor_parametro(self, parametro_busca):
        index_parametro = self.get_url_parametros().find(parametro_busca)
        index_valor = index_parametro + len(parametro_busca) + 1
        index_e_comercial = self.get_url_parametros().find('&', index_valor)
        if index_e_comercial == -1:
            valor = self.get_url_parametros()[index_valor:]
        else:
            valor = self.get_url_parametros()[index_valor:index_e_comercial]

        return valor
    
    def __len__(self):
        return len(self.url)

    def __str__(self):
        return self.url
    def __eq__(self, other):
        return self.url == other.url



url = 'bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar'
extrator_url = ExtratorURL('bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar')
print('O tamanho da URL: ', len(extrator_url))
print(extrator_url)

extrator_url = ExtratorURL(url)
extrator_url_2 = ExtratorURL(url)
print(id(extrator_url))
print(id(extrator_url_2))

print(extrator_url == extrator_url_2)

#extrator_url = ExtratorURL('bytebank.com/ca?quantidade=100&moedaOrigem=real&moedaDestino=dolar') #return url nao é valida
#extrator_url = ExtratorURL(None) #return url vazia
valor_quantidade = extrator_url.get_valor_parametro('quantidade')
print(valor_quantidade)