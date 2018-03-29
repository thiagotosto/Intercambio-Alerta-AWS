# -*- coding: utf-8 -*-

#recebe duas listas e retorna a diferença da primeira lista em relação a segunda
def diff(lista1, lista2):
    diferenca = []

    for lo in lista1:
        teste = False

        for li in lista2:
            if lo == li:
                teste = True
            #print "lo: ", lo,"li: ", li, 'teste: ',  teste

        #print 'teste: ',  teste, 'lo: ', lo

        if teste == False:
            diferenca.append(lo)

    return diferenca
