"""
módulo principal planilha em arquivo excel
autor:vania
versão:0.0.1
data:04/09/2022
"""

#importa pacotes próprios

import random

#importa  pacotes de terceitos

from openpyxl import workbook

#por fim, importe os pacotes que você desenvolveu
import manipula_xls


def main():
    lista_planilhas = ['receitas´,´despesas','resultado']
    pasta = manipula_xls.cria_xls()
    pasta.active
    for planilha in lista_planilhas:
        manipula_xls.cria_planilha(planilha, pasta)
    pasta.save("orcamento.xls")
    
if __name__=="__main__":
    main()