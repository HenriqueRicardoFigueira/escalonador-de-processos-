
#!/usr/bin/python
# -*- coding: utf-8 -*-

from processo import Processo

class Gerenciador:
    def __init__(self):
        listPro = []
        ref_arquivo = open("processo.txt", "r")
        for linhas in ref_arquivo:
            valores = linhas.split(" ")
            pro = Processo(valores[0],valores[1],valores[2],valores[3])
            listPro.append(pro)
        ref_arquivo.close()
        
        print(len(listPro))
        
Gerenciador().__init__()