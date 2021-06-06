class Atributos:

    def listaTuplaFixa(self):
        tupla = ('Ninjutsu',
                 'Taijutsu',
                 'Genjutsu',     
                 'Inteligencia',
                 'Forca',
                 'Velocidade',
                 'Stamina',
                 'Hand Seals')
        return tupla

    def FindAtributos(self, filtro,lista_notas, tupla):
        indices = [i for i,x in enumerate(lista_notas) if x==filtro] 
        lista=[]

        for x in indices:
            lista.append(tupla[x])

        return lista

    def formatarHabilidades(self, lista_habilidades):
        resultado = ''
        lista_habilidades.sort()

        for x in lista_habilidades:
            resultado += (x + ' ')
        return resultado

    def MelhoresAtributos(self, lista_notas):

        tupla = self.listaTuplaFixa()
        filtro = max(lista_notas)
        resultadoAtributos = self.FindAtributos(filtro, lista_notas, tupla)
        resultado = self.formatarHabilidades(resultadoAtributos)

        return resultado

     
    def PioresAtributos(self, lista_notas):
        tupla = self.listaTuplaFixa()
        filtro = min(lista_notas)
        resultadoAtributos = self.FindAtributos(filtro, lista_notas, tupla)
        resultado = self.formatarHabilidades(resultadoAtributos)

        return resultado

if __name__ == '__main__':
    resultado = Atributos()  
    r = resultado.MelhoresAtributos([4,4.5,2,3,2.5,4.5,3.5,3])
    print(r)