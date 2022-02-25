#### ENCRIPTAÇÃO

def limpa_texto(texto, alfabeto):
    texto_cifrado = ''
    for i in range(len(texto)):
        if texto[i] in alfabeto:
            texto_cifrado += texto[i]
    return texto_cifrado

#chave = 'SENHA'
#mensagem = 'Aqui vai a mensagem de texto'.upper()
def cifra_vigenere(mensagem, chave):
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    mensagem = limpa_texto(mensagem, alfabeto)
    chave = chave*(len(mensagem)//len(chave)) + chave[:(len(mensagem)%len(chave))]
    mensagem_cifrada = ''
    for i in range(len(mensagem)):
        indice1 = alfabeto.index(mensagem[i])
        indice2 = alfabeto.index(chave[i])
        mensagem_cifrada += alfabeto[(indice1+indice2)%26]
    #print(mensagem_cifrada)
    print('%s --> Mensagem\n%s --> Chave\n%s --> Mensagem encriptada'%(mensagem,chave,mensagem_cifrada))

# mensagem: AQUIVAIAMENSAGEMDETEXTO
# CHAVE:    SENHASENHASENHASENHASEN
# ALGORITMO DE VIGENÈRE
# 1- PASSAR PELA MENSAGEM, VENDO OS ÍNDICES
# 2- PASSAR PELA CHAVE, VENDO OS ÍNDICES
# 3- SOMAR OS ÍNDICES MÓDULO 26
chave = 'SENHA'
mensagem = 'Aqui vai a mensagem de texto'.upper()
cifra_vigenere(mensagem, chave)
