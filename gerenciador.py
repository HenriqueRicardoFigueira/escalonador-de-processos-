
#!/usr/bin/python
# -*- coding: utf-8 -*-

from processo import Processo

class Gerenciador:
    def power(self):
        listPro = []
        
        i = 4
        ref_arquivo = open("processo.txt", "r")
        for linhas in ref_arquivo:
            eventos = []
            valores = linhas.split()
            id = valores[0]
            tamanho = valores[1]
            prioridade = valores[2]
            tchegada = valores[3]

            if(len(valores) > 4):
                while(i < len(valores)):
                    eventos.append(valores[i])
                    i = i+1
           
            pro = Processo(id,tamanho,prioridade,tchegada, eventos)
            listPro.append(pro)
           

           #del eventos[:]

        ref_arquivo.close()
        
        for pr in listPro:
            print(pr.id, pr.tamanho, pr.prioridade, pr.tempoChegada, pr.eventos, pr.tipoPros)
        

Gerenciador().power()