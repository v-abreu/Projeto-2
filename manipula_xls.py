"""
módulo criar planilha em arquivo excel
autor:vania
versão:0.0.1
data:04/09/2022
"""
#pedi para importar openpyxl
#importação de pacotes
import openpyxl

from openpyxl import workbook

def cria_xls() -> workbook:
    """ esta função cria uma pasta de trabalho
    MS-Excel."""
    pasta = workbook()
    return pasta

#retirei item "na linha 18 -> lista:"
def cria_planilha(nome_planilha:str, pasta:workbook):
    pasta.active
    pasta.create_sheet(nome_planilha)