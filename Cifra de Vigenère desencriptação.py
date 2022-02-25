#### DESENCRIPTAÇÃO
def desencriptacao_cifra_vegenere(mensagem_encriptada, chave):
    chave = chave*(len(mensagem_encriptada)//len(chave)) + chave[:(len(mensagem_encriptada)%len(chave))]
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    print(mensagem_encriptada,' --> Mensagem encriptada')
    print(chave, ' --> Chave')
    # ALGORITMO
    # (MENSAGEM ENCRIPTADA - CHAVE) % 26
    mensagem = ''
    for i in range(len(chave)):
        indice1 = alfabeto.index(mensagem_encriptada[i])
        indice2 = alfabeto.index(chave[i])
        mensagem += alfabeto[(indice1-indice2)%26]
    print(mensagem, ' --> Mensagem')
mensagem_encriptada = 'SUHPVSMNTEFWNNEEHRAEPXB'
chave = 'SENHA'
desencriptacao_cifra_vegenere(mensagem_encriptada, chave)
