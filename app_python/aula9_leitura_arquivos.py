import shutil

class Leitura_Escrita_Arquivos:
    def __init__(self):
        self.arquivo = 'Notas/Notas_Academia_Konoha.txt'
        self.novoRelatorio = "Notas/Consolidado_Academia_Konoha.txt"

    def escrever_arquivo(self, texto):
        arquivo = open(self.novoRelatorio, 'w')
        arquivo.write(texto)
        arquivo.close()

    def atualizar_arquivo(self, texto):
        arquivo = open(self.novoRelatorio, 'a')
        arquivo.write(texto)
        arquivo.close()

    def ler_arquivo(self):
        arquivo = open(self.arquivo, 'r')
        return arquivo.read()

if __name__ == '__main__':
    arq = Leitura_Escrita_Arquivos()
    print(arq.ler_arquivo())