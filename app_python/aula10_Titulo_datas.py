from datetime import datetime

class Titulo:
     
    def trabalhando_com_datetime(self):
        data_atual = datetime.now()

        tupla = ('Segunda-Feira',
                'Terça-Feira',
                'Quarta-Feira',
                'Quinta-Feira',
                'Sexta-Feira',
                'Sabado',
                'Domingo')
        diaSemana = (tupla[data_atual.weekday()])
        resultado = data_atual.strftime('%d/%m/%Y %H:%M:%S') + ' - {}'.format(diaSemana)
        return 'Relatorio Consolidado das equipes da Academia Konoha {}'.format(resultado)

if __name__ == '__main__':
    resultado = Titulo()  
    r = resultado.trabalhando_com_datetime()
    print(r)
