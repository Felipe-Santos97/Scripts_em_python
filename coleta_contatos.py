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


telefones = []
for i in regex_numero_brasil.findall(texto_copiado):
  phone = '-'.join([i[0]])
  telefones.append(phone)


# Pega os emails e adiciona numa lista
emails = []
for indice in email_regex.findall(texto_copiado):
  emails.append(indice[0])

# Remove duplicadas
emails_uniq = list(set(emails))
telefones_uniq = list(set(telefones))

# Exibe os dados 
if len(emails_uniq) == 0 and len(telefones_uniq) == 0:
  print('\nNão achado nenhum contado...\n')
  quit()

if len(emails_uniq) > 0:
  print('\n========== E-MAILS ==========\n') 
  print('\n'.join(emails_uniq))

if len(telefones_uniq) > 0:
  print('\n========== TELEFONES ==========\n')
  print('\n'.join(telefones_uniq))
 
print('\n')