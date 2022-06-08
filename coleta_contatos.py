from pyperclip import paste 
import re

# Pega o texto que foi copiado para o clipboard
texto_copiado = str(paste())


email_regex = re.compile(r'''(
  [a-zA-Z0-9._%+-]+               # primeira parte do e-mail   
  @                               # arroba @ 
  [a-zA-Z0-9.-_]+                 # segunda parte  
  (\.[a-zA-Z]{2,4})               # final (.com.br)
)''', re.VERBOSE)


regex_numero_brasil = re.compile(r'''(
 ((\(\d+\)|\d+))?            # tem dd ? (12)
  (\s|.|-)?                   # separador apos o dd ?
  (\d{4,})                      # primeira parte do numero  (3892)
  (-|\s|.)?                   # separador?
  (\d{4,}) 
)''', re.VERBOSE)

regex_numero_0800 = re.compile(r'''(
  (\d{4})
  (\s|.|-)?
  (\d{3,})
  (\s|-|.)?
  (\d{3,})
)''' , re.VERBOSE)


# Pega os emails e adiciona numa lista
emails = []
for indice in email_regex.findall(texto_copiado):
  emails.append(indice[0])

# Pega os telefones e adiciona numa lista
telefones = []
for indice in regex_numero_brasil.findall(texto_copiado):
  telefones.append(indice[0])

tel_0800 = []
for indice in regex_numero_0800.findall(texto_copiado):
  tel_0800.append(indice[0])

# Remove duplicadas
emails_uniq = list(set(emails))
telefones_uniq = list(set(telefones))

# Exibe os dados 
if len(emails_uniq) == 0 and len(telefones_uniq) == 0 and len(tel_0800) == 0:
  print('\nNão achado nenhum contado...\n')
  quit()

if len(emails_uniq) > 0:
  print('\n========== E-MAILS ==========\n') 
  print('\n'.join(emails_uniq))

if len(telefones_uniq) > 0:
  print('\n========== TELEFONES ==========\n')
  print('\n'.join(telefones_uniq))
 
if len(tel_0800) > 0:
  print('\n'.join(tel_0800))

print('\n')