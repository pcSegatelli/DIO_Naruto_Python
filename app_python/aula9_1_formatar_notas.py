from aula9_leitura_arquivos import Leitura_Escrita_Arquivos
from aula_2_Atributos import Atributos

class FormatarNotas:
    def obter_dados_ninjas(self):
        arquivo = Leitura_Escrita_Arquivos()

        aluno_nota = arquivo.ler_arquivo()
        aluno_nota = aluno_nota.split('\n')
        resultado = Atributos()
        i=0

        for x in aluno_nota:
            lista_dados = x.split(',')
            nome_ninja = lista_dados[0]
            nr_equipe = lista_dados[1]
            resp_equipe = lista_dados[2]
            lista_dados.pop(0)
            lista_dados.pop(0)
            lista_dados.pop(0)
            media_aluno = lambda notas, total: sum([float(i) for i in notas])/total
            qtTotalElementos = float(len(lista_dados))
            if i == 0 or i % 3 == 0:
                arquivo.atualizar_arquivo("\nEquipe: {} - {} \n".format(nr_equipe, resp_equipe))
                arquivo.atualizar_arquivo("--------------------------------\n")

            arquivo.atualizar_arquivo(nome_ninja + " media: {:.2f} \n".format(media_aluno(map(float, lista_dados),qtTotalElementos)))
            arquivo.atualizar_arquivo("Maiores notas: {}- Piores notas: {} \n".format(resultado.MelhoresAtributos(lista_dados), resultado.PioresAtributos(lista_dados)))
            arquivo.atualizar_arquivo('\n')
            i=i+1

if __name__ == '__main__':
    arq = FormatarNotas()
    lista_media = arq.obter_dados_ninjas()
    print(lista_media)