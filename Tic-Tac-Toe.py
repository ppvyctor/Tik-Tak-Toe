import random
import os
import copy
import fumo as f
sakuya = f.sakuya


def verificador_posicao_ocupada(matriz, posicao):
        for x in matriz:
                for i in x:
                        if(i == posicao):
                                return False
        return True

def Verificador_tabuleiro(matriz : list, tipo_retorno=0):
        if(matriz[0][0] == matriz[0][1] and matriz[0][1] == matriz[0][2]):
                if(tipo_retorno == 0):
                        return True
                else:
                        return matriz[0][0]
        if(matriz[1][0] == matriz[1][1] and matriz[1][1] == matriz[1][2]):
                if(tipo_retorno == 0):
                        return True
                else:
                        return matriz[1][0]
        if(matriz[2][0] == matriz[2][1] and matriz[2][1] == matriz[2][2]):
                if(tipo_retorno == 0):
                        return True
                else:
                        return matriz[2][0]
        if(matriz[0][0] == matriz[1][0] and matriz[1][0] == matriz[2][0]):
                if(tipo_retorno == 0):
                        return True
                else:
                        return matriz[2][0]
        if(matriz[0][1] == matriz[1][1] and matriz[1][1] == matriz[2][1]):
                if(tipo_retorno == 0):
                        return True
                else:
                        return matriz[0][1]
        if(matriz[0][2] == matriz[1][2] and matriz[1][2] == matriz[2][2]):
                if(tipo_retorno == 0):
                        return True
                else:
                        return matriz[0][2]
        if(matriz[0][0] == matriz[1][1] and matriz[1][1] == matriz[2][2]):
                if(tipo_retorno == 0):
                        return True
                else:
                        return matriz[0][0]
        if(matriz[0][2] == matriz[1][1] and matriz[1][1] == matriz[2][0]):
                if(tipo_retorno == 0):
                        return True
                else:
                        return matriz[0][2]
        if(tipo_retorno == 0):
                        return False
        else:
                return -1

def verificador_empate(matriz: list):
        identificador = 0
        for i in range(len(matriz)):
                for j in range(len(matriz[i])):
                        if(matriz[i][j] not in ["X", "O"]): identificador += 1
        if(identificador == 0): 
                return True
        else:
                return False

#caso não haja alteração, retornar a mesma matriz recebida como parâmetro
#e no if do proprograma colocar se a matriz alterada é igual a anterior
'''
def vitoria_Com_uma_jogada(matriz: list):
        matriz_aux = copy.deepcopy(matriz)
        lista_espaco_disponivel = []
        for y in matriz_aux:
                for i in y:
                        if(i != 'X' and i != 'O'): lista_espaco_disponivel.append(i)
        for y in lista_espaco_disponivel:
                for i in matriz_aux:
                        for z in range(3):
                                if(i[z] == y): i[z] = "O"
                if(Verificador_tabuleiro(matriz_aux)): return matriz_aux
                matriz_aux = copy.deepcopy(matriz)
        return matriz

def derrota_Com_uma_jogada(matriz: list):
        matriz_aux = copy.deepcopy(matriz)
        lista_espaco_disponivel = []
        for y in matriz_aux:
                for i in y:
                        if(i != 'X' and i != 'O'): lista_espaco_disponivel.append(i)
        for y in lista_espaco_disponivel:
                for i in matriz_aux:
                        for z in range(3):
                                if(i[z] == y): i[z] = "X"
                if(Verificador_tabuleiro(matriz_aux)): 
                        matriz_aux = copy.deepcopy(matriz)
                        for i in matriz_aux:
                                for z in range(3):
                                        if(i[z] == y): i[z] = "O"
                        return matriz_aux
                matriz_aux = copy.deepcopy(matriz)
        return matriz
'''

def jogada_maliciosa(matriz: list, identificador = 0):
        if(identificador == 0):
                if((matriz[0][0] == 'X' and matriz[1][1] == 'O') and matriz[2][2] == 'X'):
                        matriz_aux = copy.deepcopy(matriz)
                        matriz_aux[0][0] = -1
                        matriz_aux[1][1] = -1
                        matriz_aux[2][2] = -1
                        for x in range(3):
                                for y in range(3):
                                        if(matriz_aux[x][y] == 'X' or matriz_aux[x][y] == 'O'): return False
                        return True
                elif((matriz[0][2] == 'X' and matriz[1][1] == 'O') and matriz[2][0] == 'X'):
                        matriz_aux = copy.deepcopy(matriz)
                        matriz_aux[0][2] = -1
                        matriz_aux[1][1] = -1
                        matriz_aux[2][0] = -1
                        for x in range(3):
                                for y in range(3):
                                        if(matriz_aux[x][y] == 'X' or matriz_aux[x][y] == 'O'): return False
                        return True
        else:
                if(matriz[1][1] == 'X'):
                        if(matriz[0][0] == 'X' and matriz[2][2] == 'O'):
                                matriz_aux = copy.deepcopy(matriz)
                                matriz_aux[0][0] = -1
                                matriz_aux[1][1] = -1
                                matriz_aux[2][2] = -1
                                for x in range(3):
                                        for i in range(3):
                                                if(matriz_aux[x][i] == 'X' or matriz_aux[x][i] == 'O'): return matriz
                                y = random.choice([9, 1])
                                matriz_aux = copy.deepcopy(matriz)
                                for x in range(3):
                                        for i in range(3):
                                                if(matriz_aux[x][i] == y):
                                                        matriz_aux[x][i] = 'O'
                                                        return matriz_aux
                        elif(matriz[0][2] == 'X' and matriz[2][0] == 'O'):
                                matriz_aux = copy.deepcopy(matriz)
                                matriz_aux[0][2] = -1
                                matriz_aux[1][1] = -1
                                matriz_aux[2][0] = -1
                                for x in range(3):
                                        for i in range(3):
                                                if(matriz_aux[x][i] == 'X' or matriz_aux[x][i] == 'O'): return matriz
                                y = random.choice([7, 3])
                                matriz_aux = copy.deepcopy(matriz)
                                for x in range(3):
                                        for i in range(3):
                                                if(matriz_aux[x][i] == y):
                                                        matriz_aux[x][i] = 'O'
                                                        return matriz_aux
                        elif(matriz[2][0] == 'X' and matriz[0][2] == 'O'):
                                matriz_aux = copy.deepcopy(matriz)
                                matriz_aux[2][0] = -1
                                matriz_aux[1][1] = -1
                                matriz_aux[0][2] = -1
                                for x in range(3):
                                        for i in range(3):
                                                if(matriz_aux[x][i] == 'X' or matriz_aux[x][i] == 'O'): return matriz
                                y = random.choice([7, 3])
                                matriz_aux = copy.deepcopy(matriz)
                                for x in range(3):
                                        for i in range(3):
                                                if(matriz_aux[x][i] == y):
                                                        matriz_aux[x][i] = 'O'
                                                        return matriz_aux
                        elif(matriz[2][2] == 'X' and matriz[0][0] == 'O'):
                                matriz_aux = copy.deepcopy(matriz)
                                matriz_aux[0][0] = -1
                                matriz_aux[1][1] = -1
                                matriz_aux[2][2] = -1
                                for x in range(3):
                                        for i in range(3):
                                                if(matriz_aux[x][i] == 'X' or matriz_aux[x][i] == 'O'): return matriz
                                matriz_aux = copy.deepcopy(matriz)
                                y = random.choice([9, 1])
                                for x in range(3):
                                        for i in range(3):
                                                if(matriz_aux[x][i] == y):
                                                        matriz_aux[x][i] = 'O'
                                                        return matriz_aux
                return matriz
                                
        return False

def jogada_IA(matriz: list):
        lista_melhor_pos = []
        eventos = 5000 
        best_chance_victory = 0
        if(jogada_maliciosa(matriz)):
                y = random.choice([2, 4, 6, 8])
                matriz_aux = copy.deepcopy(matriz) 
                for x in range(3):
                        for i in range(3):
                                if(matriz_aux[x][i]== y): matriz_aux[x][i] = 'O'
                return matriz_aux
        else:
                matriz_aux = jogada_maliciosa(matriz, 1)
                for x in range(3):
                        for i in range(3):
                                if(matriz_aux[x][i] != matriz[x][i]): return matriz_aux
        #probabilidade_derrota_aux = 0
        for linha in range(3):
                for coluna in range(3):
                        if(matriz[linha][coluna] != 'X' and matriz[linha][coluna] != 'O'):
                                qtd_vitorias = []
                                qtd_empates = []
                                #qtd_derrota = []
                                matriz_aux = copy.deepcopy(matriz) 
                                matriz_aux[linha][coluna] = 'O'
                                if(Verificador_tabuleiro(matriz_aux)): return matriz_aux
                                for i in range(eventos):
                                        matriz_aux = copy.deepcopy(matriz)
                                        matriz_aux[linha][coluna] = 'X'
                                        lista_espaco_disponivel = []
                                        for y in matriz_aux:
                                                for i in y:
                                                        if(i != 'X' and i != 'O'): lista_espaco_disponivel.append(i)
                                        primeira_pos = copy.deepcopy(matriz_aux)
                                        vez = 1
                                        identificador = 0
                                        while(len(lista_espaco_disponivel) != 0 or identificador == 0):
                                                if(len(lista_espaco_disponivel) != 0):
                                                        y = random.choice(lista_espaco_disponivel)
                                                        for i in matriz_aux:
                                                                for z in range(3):
                                                                        if(i[z] == y):
                                                                                if(vez == 0):
                                                                                        i[z] = "X"
                                                                                        vez += 1
                                                                                else:
                                                                                        i[z] = "O"
                                                                                        vez -= 1
                                                        lista_espaco_disponivel.remove(y)
                                                if(Verificador_tabuleiro(matriz_aux, 1) == 'O'):
                                                        #qtd_derrota.append(primeira_pos)
                                                        break
                                                elif(Verificador_tabuleiro(matriz_aux, 1) == 'X'):
                                                        qtd_vitorias.append(primeira_pos)
                                                        break
                                                elif(verificador_empate(matriz_aux)):
                                                        qtd_empates.append(primeira_pos)
                                                
                                                identificador += 1
                                probabilidade_vitoria = len(qtd_vitorias)/eventos
                                probabilidade_empates = len(qtd_empates)/eventos
                                '''print(f"Vitória {linha}, {coluna}: {probabilidade_vitoria}")
                                print(f"Empate {linha}, {coluna}: {probabilidade_empates}")
                                os.system("pause")'''
                                if(probabilidade_vitoria == 1):
                                        if(Verificador_tabuleiro(primeira_pos)):
                                                best_chance_victory = probabilidade_vitoria
                                                lista_melhor_pos = copy.deepcopy(primeira_pos)
                                if(probabilidade_vitoria == best_chance_victory):
                                        if(Verificador_tabuleiro(primeira_pos)):
                                                best_chance_victory = probabilidade_vitoria
                                                lista_melhor_pos = copy.deepcopy(primeira_pos)
                                if(probabilidade_vitoria > best_chance_victory):
                                        best_chance_victory = probabilidade_vitoria
                                        lista_melhor_pos = copy.deepcopy(primeira_pos)
                                if(probabilidade_empates > best_chance_victory):
                                        best_chance_victory = probabilidade_empates
                                        lista_melhor_pos = copy.deepcopy(primeira_pos)
                                
        for x in range(3):
                for y in range(3):
                        if(lista_melhor_pos[x][y] != matriz[x][y]):
                                lista_melhor_pos[x][y] = 'O'
        return lista_melhor_pos
                                
matriz = [[7, 8, 9],
        [4, 5, 6],
        [1, 2, 3]]

print("\t +--------------------------------+")
print("\t |   BEM VINDO AO JOGO DA VELHA   |")
print("\t +--------------------------------+\n")
#print("\t\t\t  ᗜˬᗜ Bom Jogo ᗜˬᗜ")


for x in matriz:
        print("\t\t    ", end = "")
        for i in range(3):
                print(x[i],  "", end = '')
                if(i != 2):
                        print("| ", end='')
        print("")
        if(x[0] != 1):
                print("\t\t", end="")
                for i in range(17):
                        if(i == 6 or i == 10):
                                print("+", end="")
                        else:
                                print("-", end="")
                print("")

print("\nUtilize seu teclado numerico para indicar a posicao onde deseja realizar a jogada\n")
os.system("pause")
os.system("cls")

username = ''
player_1 = ''
player_2 = ''
while(True):
        opcao = -1
        pontuacao_usuario_1 = 0
        pontuacao_IA = 0
        pontuacao_usuario_2 = 0
        while(opcao <= 0 or opcao > 3):
                os.system("cls")
                print("Escolha o modo de jogo.")
                print("\t1) Singleplayer.")
                print("\t2) Multiplayer.")
                print("\t3) Sair do jogo.\n")
                try:
                        opcao = int(input("\nDigite o numero da opção desejada: "))
                        if(opcao <= 0 or opcao > 3):
                                print("\n\nOOOPS!!! Digite um número entre 1 e 3")
                                os.system("pause")
                        elif(opcao == 1):
                                os.system("cls")
                                if(username == ''):
                                        username = input("Digite um username: ")
                                        if((username == '' or username == ' ') or username == '  '): username = "Player"
                                else:
                                        opcao_nome = input('Digite qualquer coisa diferente de "s ou S" para digitar um outro nome: ').upper()
                                        if(opcao != 'S'):
                                                username = input("\n\nDigite um username: ")
                                                if((username == '' or username == ' ') or username == '  '): username = "Player 1"
                                break
                        elif(opcao == 2):
                                os.system("cls")
                                if(player_1 == ''):
                                        player_1 = input("Digite um username para o player 1: ")
                                        if((player_1 == '' or player_1 == ' ') or player_1 == '  '): player_1 = "Player 1"
                                else:
                                        opcao_nome = input('Digite qualquer coisa diferente de "s ou S" para digitar um outro nome: ').upper()
                                        if(opcao_nome != 'S'):
                                                player_1 = input("\n\nDigite um username para o player 1: ")
                                                if((username == '' or player_1 == ' ') or player_1 == '  '): player_1 = "Player 1"
                                os.system("cls")
                                if(player_2 == ''):
                                        player_2 = input("Digite um username para o player 2: ")
                                        if((player_2 == '' or player_2 == ' ') or player_2 == '  '): player_2 = "Player 2"
                                else:
                                        opcao_nome = input('Digite qualquer coisa diferente de "s ou S" para digitar um outro nome: ').upper()
                                        if(opcao_nome != 'S'):
                                                player_2 = input("\n\nDigite um username para o player 2: ")
                                                if((player_2 == '' or player_2 == ' ') or player_2 == '  '): player_2 = "Player 2"
                        else:
                                os.system("cls")
                                print("OBRIGADO POR JOGAR O TIC TAC TOE!!!!\n")
                                print(sakuya)
                                os.system("pause")
                                exit()
                except ValueError:
                        print("\n\nOOOOPS!!! Digitação errada, por favor digite um número inteira.")
                        os.system("pause")
        if(opcao == 1):
                while(True):
                        matriz = [[7, 8, 9],
                        [4, 5, 6],
                        [1, 2, 3]]
                        identificador_comeca = random.randint(0,1)
                        while (True):
                                os.system("cls")
                                if(Verificador_tabuleiro(matriz)): break
                                if(verificador_empate(matriz)): break
                                print(f"\t       {username}: {pontuacao_usuario_1}  VS  Bot: {pontuacao_IA}\n")
                                for x in range(len(matriz)):
                                        print("\t\t    ", end="")
                                        for i in range(len(matriz)):
                                                if(matriz[x][i] == "X" or matriz[x][i] == "O"):
                                                        print(matriz[x][i], "", end='')
                                                else:
                                                        print("  ", end='')
                                                if (i != 2):
                                                        print("| ", end='')
                                        if(x != 2):
                                                print("")
                                                if (matriz[x][0] != 1):
                                                        print("\t\t", end="")
                                                        for i in range(17):
                                                                if (i == 6 or i == 10):
                                                                        print("+", end="")
                                                                else:
                                                                        print("-", end="")
                                                        print("")
                                print("")

                                if(identificador_comeca == 0):
                                        try:
                                                jogada = int(input("Digite o número da posicao que deseja realiar a jogada: "))
                                                if(0 <= jogada >9):
                                                        print("\n\nOOOPS!!! Digite um número de 1 a 9 para realiar a jogada")
                                                        os.system("pause")
                                                        continue

                                                elif(verificador_posicao_ocupada(matriz, jogada)):
                                                        print("\n\nOOOPS!!! lugar já ocupado, por favor escolha outro lugar")
                                                        os.system("pause")
                                                        continue
                                                for x in matriz:
                                                        for i in range(3):
                                                                if(x[i] == jogada):
                                                                        x[i] = "X"
                                                                        identificador_comeca += 1
                                        except :
                                                print("\n\nOOOPS!! Digite apenas números inteiros")
                                                os.system("pause")
                                                continue
                                else:
                                        matriz = jogada_IA(matriz)
                                        identificador_comeca -= 1
                                                
                        os.system("cls")
                        print(f"\t       {username}: {pontuacao_usuario_1}  VS  Bot: {pontuacao_IA}\n")
                        for x in range(len(matriz)):
                                print("\t\t    ", end="")
                                for i in range(len(matriz)):
                                        if(matriz[x][i] == "X" or matriz[x][i] == "O"):
                                                print(matriz[x][i], "", end='')
                                        else:
                                                print("  ", end='')
                                        if (i != 2):
                                                print("| ", end='')
                                if(x != 2):
                                        print("")
                                        if (matriz[x][0] != 1):
                                                print("\t\t", end="")
                                                for i in range(17):
                                                        if (i == 6 or i == 10):
                                                                print("+", end="")
                                                        else:
                                                                print("-", end="")
                                                print("")
                        print("")
                        
                        if(Verificador_tabuleiro(matriz, 1) == "X"):
                                print(f"\nPARABÉNS VOCÊ VENCEU!!!")
                                pontuacao_usuario_1 += 1
                                os.system("pause")
                                os.system("cls")
                        elif(Verificador_tabuleiro(matriz, 1) == "O"):
                                print(f"\nVOCÊ PERDEU!!!")
                                pontuacao_IA += 1
                                os.system("pause")
                                os.system("cls")
                        else:
                                print("EMPATE!!!")
                                os.system("pause")
                                os.system("cls")
                        opcao = input('Digite qualquer coisa diferente de "n ou N" para continuar jogando, caso contrário voltará ao menu inicial: ').upper()
                        if(opcao == 'N'):
                                break
        elif(opcao == 2):
                while(True):
                        matriz = [[7, 8, 9],
                        [4, 5, 6],
                        [1, 2, 3]]
                        identificador_comeca = random.randint(0,1)
                        while (True):
                                os.system("cls")
                                if(Verificador_tabuleiro(matriz)): break
                                if(verificador_empate(matriz)): break
                                print(f"\t       {player_1}: {pontuacao_usuario_1}  VS  {player_2}: {pontuacao_usuario_2}\n")
                                for x in range(len(matriz)):
                                        print("\t\t    ", end="")
                                        for i in range(len(matriz)):
                                                if(matriz[x][i] == "X" or matriz[x][i] == "O"):
                                                        print(matriz[x][i], "", end='')
                                                else:
                                                        print("  ", end='')
                                                if (i != 2):
                                                        print("| ", end='')
                                        if(x != 2):
                                                print("")
                                                if (matriz[x][0] != 1):
                                                        print("\t\t", end="")
                                                        for i in range(17):
                                                                if (i == 6 or i == 10):
                                                                        print("+", end="")
                                                                else:
                                                                        print("-", end="")
                                                        print("")
                                print("")

                                if(identificador_comeca == 0):
                                        try:
                                                print(f"Vez do(a): {player_1}")
                                                jogada = int(input("Digite o número da posicao que deseja realiar a jogada: "))
                                                if(0 <= jogada >9):
                                                        print("\n\nOOOPS!!! Digite um número de 1 a 9 para realiar a jogada")
                                                        os.system("pause")
                                                        continue

                                                elif(verificador_posicao_ocupada(matriz, jogada)):
                                                        print("\n\nOOOPS!!! lugar já ocupado, por favor escolha outro lugar")
                                                        os.system("pause")
                                                        continue
                                                for x in matriz:
                                                        for i in range(3):
                                                                if(x[i] == jogada):
                                                                        x[i] = "X"
                                                                        identificador_comeca += 1
                                        except :
                                                print("\n\nOOOPS!! Digite apenas números inteiros")
                                                os.system("pause")
                                                continue             
                                else:
                                        try:
                                                print(f"Vez do(a): {player_2}")
                                                jogada = int(input("Digite o número da posicao que deseja realiar a jogada: "))
                                                if(0 <= jogada >9):
                                                        print("\n\nOOOPS!!! Digite um número de 1 a 9 para realiar a jogada")
                                                        os.system("pause")
                                                        continue

                                                elif(verificador_posicao_ocupada(matriz, jogada)):
                                                        print("\n\nOOOPS!!! lugar já ocupado, por favor escolha outro lugar")
                                                        os.system("pause")
                                                        continue
                                                for x in matriz:
                                                        for i in range(3):
                                                                if(x[i] == jogada):
                                                                        x[i] = "O"
                                                                        identificador_comeca -= 1
                                        except :
                                                print("\n\nOOOPS!! Digite apenas números inteiros")
                                                os.system("pause")
                                                continue 
                                                
                        os.system("cls")
                        print(f"\t       {player_1}: {pontuacao_usuario_1}  VS  {player_2}: {pontuacao_usuario_2}\n")
                        for x in range(len(matriz)):
                                print("\t\t    ", end="")
                                for i in range(len(matriz)):
                                        if(matriz[x][i] == "X" or matriz[x][i] == "O"):
                                                print(matriz[x][i], "", end='')
                                        else:
                                                print("  ", end='')
                                        if (i != 2):
                                                print("| ", end='')
                                if(x != 2):
                                        print("")
                                        if (matriz[x][0] != 1):
                                                print("\t\t", end="")
                                                for i in range(17):
                                                        if (i == 6 or i == 10):
                                                                print("+", end="")
                                                        else:
                                                                print("-", end="")
                                                print("")
                        print("")
                        
                        if(Verificador_tabuleiro(matriz, 1) == "X"):
                                print(f"\n{player_1} VENCEU!!!")
                                pontuacao_usuario_1 += 1
                                os.system("pause")
                                os.system("cls")
                        elif(Verificador_tabuleiro(matriz, 1) == "O"):
                                print(f"\n{player_2} VENCEU!!!")
                                pontuacao_usuario_2 += 1
                                os.system("pause")
                                os.system("cls")
                        else:
                                print("EMPATE!!!")
                                os.system("pause")
                                os.system("cls")
                        opcao = input('Digite qualquer coisa diferente de "n ou N" para continuar jogando, caso contrário voltará ao menu inicial: ').upper()
                        if(opcao == 'N'):
                                break