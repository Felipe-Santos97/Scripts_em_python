from zipfile import ZipFile
from time import sleep
from os import path

input_file_zip = input('Digite o nome do arquivo ou caminho completo: ') 


if not path.exists(input_file_zip):
  print('ERRO... Digite um arquivo .ZIP')
  quit()

for i in range (0,5):
  print('Extraindo Conteudo, aguarde', '..' * i)
  sleep(0.60)

try:
  file_zip = ZipFile(input_file_zip)
  file_zip.extractall()
  print('\n\033[36mCONTEUDO EXTRAIDO, VERIFIQUE A PASTA ATUAL\033[m\n')
except: 
  print('Um Erro ocorreu na execução...')

