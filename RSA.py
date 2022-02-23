import random

def primos(k):
  lista = []
  penerar = [1]*(100000+1)
  for i in range(2, 100000+1):
    if penerar[i]:
      lista.append(i)
    for j in range(i, 100000+1, i):
      penerar[j] = 0
  #print(lista)
  primos = algarismos(k, lista)
  primo_escolhido1, primo_escolhido2 = 0, 0
  while primo_escolhido1 == primo_escolhido2:
    primo_escolhido1, primo_escolhido2 = primos[random.randint(0, len(primos)-1)], primos[random.randint(0, len(primos)-1)]
  #print(primo_escolhido1, primo_escolhido2)
  return primo_escolhido1, primo_escolhido2


def algarismos(k, lista):
  return [i for i in lista if len(str(i))== k] 



# Chaves públicas: (𝑛;𝑒)
# Chaves privadas: (𝑝;𝑞;𝑑)
# 𝐶 = Bloco de mensagem codificada
# 𝐶= 𝑀𝑒 mod (𝑛)
def rsa(mensagem, p, q):
  primos(k)
  asc = []
  for i in mensagem:
    asc.append(ord(i))
  print('Mensagem em ASCII --> ',asc)
  n = p*q
  print('p = %d   q = %d   n = %d'%(p,q,n))
  totiente = (p-1)*(q-1)
  for i in range(2,totiente):
    if totiente % i != 0:
      e = i
      break
  print('e = %d'%e)
  inverso_multiplicativo_modular = False
  for d in range(0, totiente):
    if (e*d)%totiente == 1:
      inverso_multiplicativo_modular = d
      break
  if inverso_multiplicativo_modular:
    print('d = %d'%d)
    blocos_codificados = []
    for bloco in asc:
      m = (int(bloco)**e)%n
      blocos_codificados.append(m)
    print('Mensagem encriptada --> ',blocos_codificados)
    decifrando = []
    
    for bloco in blocos_codificados:
      m = (int(bloco)**d)%n
      decifrando.append(m)
    string = ''
    for i in decifrando:
      string += str(chr(i)) +' '

    print('Mensagem "recuperada" em  ASCII --> ',decifrando)
    print('Mensagem = ',string)

  
  else:
    print('Não tem inverso multiplicativo modular\nRode novamente o algoritmo.')


k = 3
p,q = primos(k)
rsa('Ataque ao anoitecer', p, q) 
