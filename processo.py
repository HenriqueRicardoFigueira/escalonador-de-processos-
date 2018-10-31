
#!/usr/bin/python
# -*- coding: utf-8 -*-

class Processo:
    def __init__(self, id, tamanho, prioridade, tempoChegada):
        self.id = id
        self.tamanho = tamanho
        self.prioridade = prioridade
        self.tempoChegada = tempoChegada
        #self.eventos = eventos
        self.blqueado = False
        self.tempoInicio = 0
        self.estadoPros = "pronto"
        #if (len(eventos) > 0):
         #   self.tipoPros = "IObound"
       # else:
           # self.tipoPros = "CPUbound"
    
    def retornaPrioridade(self):
       return self.prioridade
    
    def retornaTempoChegada(self):
        return self.tempoChegada
    
    def retornaTempoInicio(self):
        return self.tempoInicio

    def retornaEstado(self):
        return str(self.estadoPros)

    def tobloqueado(self):
        return self.blqueado
    
    #def retornaTipo(self):
       # return self.tipoPros
