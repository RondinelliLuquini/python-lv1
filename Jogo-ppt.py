import random

def jogo():
    voce = input ("Escolha uma item para jogar: \n 'pe' para pedra, 'pa' para papel, 'te' para tesoura \n")
    computador = random.choice(['pe','pa','te'])

    if voce == computador:
        return "Empate"
    
    if vencedor(voce, computador):
        return "Voce ganhou!"
    
    return "Voce perdeu!"

# abaixo, true caso o um dos jogadores ganhe a partida
# logica: pedra > papel, tesoura > papel, papel > tesoura
def vencedor(jogador, adversario):
    if  (jogador == 'pe' and adversario == 'pa' or jogador == 'te' and adversario == 'pa'or jogador == 'pa' and adversario == 'te' or jogador == 'pe' and adversario == 'te'):
        return True

print(jogo())