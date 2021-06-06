import requests

class Rodape:

    def retorna_rodape(self, cep):
        response = requests.get('https://viacep.com.br/ws/{}/json/' .format(cep))
        dados_cep = response.json()
        bairro = dados_cep['bairro']
        local = dados_cep['localidade']
        rodape = 'Done by Uzumaki Company in {} - {}'.format(bairro, local)
        return rodape

if __name__ == '__main__':
    rodape = Rodape()
    print(rodape.retorna_rodape('01513000'))
