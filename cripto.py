print('========== CRIPTOGRAFIA ========== \n', '')
# importação do alfabeto que vai ser usado
from string import ascii_lowercase
import unidecode

alfabeto = list(ascii_lowercase)

def codifica(mensagem, chave):
  newMsg = unidecode.unidecode(mensagem)
  cifra = ""
  for letra in newMsg:
    indice = ord(letra)-97
    cifra += alfabeto[(indice + chave)%len(alfabeto)] if letra in alfabeto else letra
  return print('A sua mensagem (des)criptografada é: \n -->', cifra)

def descodifica(mensagem, chave): 
  return codifica(mensagem, len(alfabeto) - chave)

desloc = int(input('Digite a chave da sua criptografia: '))
print('')
modo = input('O que você quer fazer? \n 1- Criptografar \n 2- Decifrar \n')
print('')

if(modo == '1'):
  print('----- Encriptar -----')
  msg = input('Texto para encriptar: \n').lower()
  codifica('{}'.format(msg), desloc)

elif(modo =='2'):
  print('----- Decifrador -----')
  msg = input('Texto para Decifrar: \n').lower()
  descodifica('{}' .format(msg), desloc)
  msg = ''