from aula9_leitura_arquivos import Leitura_Escrita_Arquivos
from aula9_1_formatar_notas import FormatarNotas
from aula10_Titulo_datas import Titulo
from aula12_capturarFrase import Rodape
from python_SCRAPING.main import CapturarNindo

if __name__ == '__main__':
    leitura = Leitura_Escrita_Arquivos()

    resultado = Titulo()
    d = resultado.trabalhando_com_datetime()

    #gravar titulo no novo arquivo
    leitura.escrever_arquivo(d)
    leitura.atualizar_arquivo('\n------------------------------------------------------------------------------------\n')

    #obter informações para gravar dados
    notas = FormatarNotas()
    lista = notas.obter_dados_ninjas()

    rodape = Rodape()
    leitura.atualizar_arquivo('\n')
    leitura.atualizar_arquivo(rodape.retorna_rodape('01513000'))

    nindo = CapturarNindo()
    leitura.atualizar_arquivo('\n')
    leitura.atualizar_arquivo(nindo.capturandoNindo())