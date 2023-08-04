import random
import tkinter as tk
import messagebox
import sys
import os

import velha3
import velha2

velha3
velha2

#Tela
janela= tk.Tk()
janela.title('JOGO DA VELHA')
janela.attributes('-fullscreen', False)
altura= 400
largura= 400
tamanho= f'{altura}x{largura}'
janela.geometry(tamanho)
janela.maxsize(altura, largura)
janela.minsize(altura, largura)

#botão

botao_altura = altura//58
botao_largura = largura//29

linhas= 3
colunas= 3

matriz_botoes= []


jogador=''


#jogadas

tabuleiro = [['','',''],
             ['','',''],
             ['','','']
             ]

cont= velha2.contvelha2

#IA
computador = velha3.computador


robot= velha2.robot
human= velha2.human

cont_comp = 0

def IA():
    global cont_comp
    global linhas
    global colunas
    global human

    '''if cont_comp == 1:
        for linha in range(linhas):
            for coluna in range(colunas):
                if tabuleiro[linha][coluna] == '':
                    tabuleiro[linha][coluna] = robot
                    matriz_botoes[linha][coluna].config(text=robot, fg= velha2.cor_robot)
                    janela.update()
                    return'''

    # linha 1
    if tabuleiro[0][0] == tabuleiro[0][1] == human or tabuleiro[0][0] == tabuleiro[0][1] == robot and tabuleiro[0][
        2] == '':
        tabuleiro[0][2] = robot
        matriz_botoes[0][2].config(text=robot, fg=velha2.cor_robot)
        janela.update()
        pass

    elif tabuleiro[0][0] == tabuleiro[0][2] == human or tabuleiro[0][0] == tabuleiro[0][2] == robot and tabuleiro[0][
        1] == '':
        tabuleiro[0][1] = robot
        matriz_botoes[0][1].config(text=robot, fg=velha2.cor_robot)
        janela.update()
        pass

    elif tabuleiro[0][1] == tabuleiro[0][2] == human or tabuleiro[0][1] == tabuleiro[0][2] == robot and tabuleiro[0][
        0] == '':
        tabuleiro[0][0] = robot
        matriz_botoes[0][0].config(text=robot, fg=velha2.cor_robot)
        janela.update()
        pass

    # linha 2

    elif tabuleiro[1][0] == tabuleiro[1][1] == human or tabuleiro[1][0] == tabuleiro[1][1] == robot and tabuleiro[1][
        2] == '':
        tabuleiro[1][2] = robot
        matriz_botoes[1][2].config(text=robot, fg=velha2.cor_robot)
        janela.update()
        pass

    elif tabuleiro[1][0] == tabuleiro[1][2] == human or tabuleiro[1][0] == tabuleiro[1][2] == robot and tabuleiro[1][
        1] == '':
        tabuleiro[1][1] = robot
        matriz_botoes[1][1].config(text=robot, fg=velha2.cor_robot)
        janela.update()
        pass

    elif tabuleiro[1][1] == tabuleiro[1][2] == human or tabuleiro[1][1] == tabuleiro[1][2] == robot and tabuleiro[1][
        0] == '':
        tabuleiro[1][0] = robot
        matriz_botoes[1][0].config(text=robot, fg=velha2.cor_robot)
        janela.update()
        pass

    # linha 3

    elif tabuleiro[2][0] == tabuleiro[2][1] == human or tabuleiro[2][0] == tabuleiro[2][1] == robot and tabuleiro[2][
        2] == '':
        tabuleiro[2][2] = robot
        matriz_botoes[2][2].config(text=robot, fg=velha2.cor_robot)
        janela.update()
        pass

    elif tabuleiro[2][0] == tabuleiro[2][2] == human or tabuleiro[2][0] == tabuleiro[2][2] == robot and tabuleiro[2][
        1] == '':
        tabuleiro[2][1] = robot
        matriz_botoes[2][1].config(text=robot, fg=velha2.cor_robot)
        janela.update()
        pass

    elif tabuleiro[2][1] == tabuleiro[2][2] == human or tabuleiro[2][1] == tabuleiro[2][2] == robot and tabuleiro[2][
        0] == '':
        tabuleiro[2][0] = robot
        matriz_botoes[2][0].config(text=robot, fg=velha2.cor_robot)
        janela.update()
        pass

    # Coluna 1

    elif tabuleiro[0][0] == tabuleiro[1][0] == human or tabuleiro[0][0] == tabuleiro[1][0] == robot and tabuleiro[2][
        0] == '':
        tabuleiro[2][0] = robot
        matriz_botoes[2][0].config(text=robot, fg=velha2.cor_robot)
        janela.update()
        pass

    elif tabuleiro[0][0] == tabuleiro[2][0] == human or tabuleiro[0][0] == tabuleiro[2][0] == robot and tabuleiro[1][
        0] == '':
        tabuleiro[1][0] = robot
        matriz_botoes[1][0].config(text=robot, fg=velha2.cor_robot)
        janela.update()
        pass

    elif tabuleiro[1][0] == tabuleiro[2][0] == human or tabuleiro[1][0] == tabuleiro[2][0] == robot and tabuleiro[0][
        0] == '':
        tabuleiro[0][0] = robot
        matriz_botoes[0][0].config(text=robot, fg=velha2.cor_robot)

        pass


    # Coluna 2

    elif tabuleiro[0][1] == tabuleiro[1][1] == human or tabuleiro[0][1] == tabuleiro[1][1] == robot and tabuleiro[2][
        1] == '':
        tabuleiro[2][1] = robot
        matriz_botoes[2][1].config(text=robot, fg=velha2.cor_robot)
        janela.update()
        pass

    elif tabuleiro[0][1] == tabuleiro[2][1] == human or tabuleiro[0][1] == tabuleiro[2][1] == robot and tabuleiro[1][
        1] == '':
        tabuleiro[1][1] = robot
        matriz_botoes[1][1].config(text=robot, fg=velha2.cor_robot)
        janela.update()
        pass

    elif tabuleiro[1][1] == tabuleiro[2][1] == human or tabuleiro[1][1] == tabuleiro[2][1] == robot and tabuleiro[0][
        1] == '':
        tabuleiro[0][1] = robot
        matriz_botoes[0][1].config(text=robot, fg=velha2.cor_robot)
        janela.update()
        pass

    # Coluna 3

    elif tabuleiro[0][2] == tabuleiro[1][1] == human or tabuleiro[0][2] == tabuleiro[1][1] == robot and tabuleiro[2][
        2] == '':
        tabuleiro[2][2] = robot
        matriz_botoes[2][2].config(text=robot, fg=velha2.cor_robot)
        janela.update()
        pass

    elif tabuleiro[0][2] == tabuleiro[2][1] == human or tabuleiro[0][2] == tabuleiro[2][1] == robot and tabuleiro[1][
        2] == '':
        tabuleiro[1][2] = robot
        matriz_botoes[1][2].config(text=robot, fg=velha2.cor_robot)
        janela.update()
        pass

    elif tabuleiro[1][2] == tabuleiro[2][1] == human or tabuleiro[1][2] == tabuleiro[2][1] == robot and tabuleiro[0][
        2] == '':
        tabuleiro[0][2] = robot
        matriz_botoes[0][2].config(text=robot, fg=velha2.cor_robot)
        janela.update()
        pass

    # Diagonal 1

    elif tabuleiro[0][0] == tabuleiro[1][1] == human or tabuleiro[0][0] == tabuleiro[1][1] == robot and tabuleiro[2][
        2] == '':
        tabuleiro[2][2] = robot
        matriz_botoes[2][2].config(text=robot, fg=velha2.cor_robot)
        janela.update()
        pass

    elif tabuleiro[0][0] == tabuleiro[2][2] == human or tabuleiro[0][0] == tabuleiro[2][2] == robot and tabuleiro[1][
        1] == '':
        tabuleiro[1][1] = robot
        matriz_botoes[1][1].config(text=robot, fg=velha2.cor_robot)
        janela.update()
        pass

    elif tabuleiro[1][1] == tabuleiro[2][2] == human or tabuleiro[1][1] == tabuleiro[2][2] == robot and tabuleiro[0][
        0] == '':
        tabuleiro[0][0] = robot
        matriz_botoes[0][0].config(text=robot, fg=velha2.cor_robot)
        janela.update()
        pass
    # Diagonal 2

    elif tabuleiro[0][2] == tabuleiro[1][1] == human or tabuleiro[0][2] == tabuleiro[1][1] == robot and tabuleiro[2][
        0] == '':
        tabuleiro[2][0] = robot
        matriz_botoes[2][0].config(text=robot, fg=velha2.cor_robot)
        janela.update()
        pass


    elif tabuleiro[0][2] == tabuleiro[2][0] == human or tabuleiro[0][2] == tabuleiro[2][0] == robot and tabuleiro[1][
        1] == '':
        tabuleiro[1][1] = robot
        matriz_botoes[1][1].config(text=robot, fg=velha2.cor_robot)
        janela.update()
        pass

    elif tabuleiro[2][0] == tabuleiro[1][1] == human or tabuleiro[2][0] == tabuleiro[1][1] == robot and tabuleiro[0][
        2] == '':
        tabuleiro[0][2] = robot
        matriz_botoes[0][2].config(text=robot, fg=velha2.cor_robot)
        janela.update()
        pass

    else:
        print('deu certo')
        l = random.randint(0, 2)
        c = random.randint(0, 2)
        co= 0
        print(l, c)
        while co != 1:
            if tabuleiro[l][c] == '':
                tabuleiro[l][c] = robot
                matriz_botoes[l][c].config(text=robot, fg=velha2.cor_robot)
                janela.update()
                pass
                co = 1
            else:
                l = random.randint(1, 3)
                c = random.randint(1, 3)
    print(tabuleiro)



def repetir():
    arquivo= sys.executable
    os.execl(arquivo, arquivo, *sys.argv)

def empate():
    cont_empate = 0
    global janela
    for l in range(linhas):
        for c in range(colunas):
            if tabuleiro[l][c] != '':
                cont_empate+=1
    if cont_empate == 9:
        janela.destroy()
        info = messagebox.showinfo(title='JOGO DA VELHA', message='EMPATE')
        repetir()
        info.protocol('WM_DELETE_WINDOW', exit)




#Vencedor
def vencedor():
    janela.update()
    if tabuleiro[0][0] == tabuleiro[0][1] == tabuleiro[0][2]:
        if tabuleiro[0][0] == 'X':
            messagebox.showinfo(title='JOGO DA VELHA', message='X VENCEU')
            repetir()
        elif tabuleiro[0][0] == 'O':
            messagebox.showinfo(title='JOGO DA VELHA', message='O VENCEU')
            repetir()


    elif tabuleiro[1][0] == tabuleiro[1][1] == tabuleiro[1][2]:
        if tabuleiro[1][0] == 'X':
            messagebox.showinfo(title='JOGO DA VELHA', message='X VENCEU')
            repetir()
        elif tabuleiro[1][0] == 'O':
            messagebox.showinfo(title='JOGO DA VELHA', message='O VENCEU')
            repetir()


    elif tabuleiro[2][0] == tabuleiro[2][1] == tabuleiro[2][2]:
        if tabuleiro[2][0] == 'X':
            messagebox.showinfo(title='JOGO DA VELHA', message='X VENCEU')
            repetir()
        elif tabuleiro[2][0] == 'O':
            messagebox.showinfo(title='JOGO DA VELHA', message='O VENCEU')
            repetir()

    elif tabuleiro[0][0] == tabuleiro[1][0] == tabuleiro[2][0]:
        if tabuleiro[0][0] == 'X':
            messagebox.showinfo(title='JOGO DA VELHA', message='X VENCEU')
            repetir()
        elif tabuleiro[0][0] == 'O':
            messagebox.showinfo(title='JOGO DA VELHA', message='O VENCEU')
            repetir()

    elif tabuleiro[0][1] == tabuleiro[1][1] == tabuleiro[2][1]:
        if tabuleiro[0][1] == 'X':
            messagebox.showinfo(title='JOGO DA VELHA', message='X VENCEU')
            repetir()
        elif tabuleiro[0][1] == 'O':
            messagebox.showinfo(title='JOGO DA VELHA', message='O VENCEU')
            repetir()

    elif tabuleiro[0][2] == tabuleiro[1][2] == tabuleiro[2][2]:
        if tabuleiro[0][2] == 'X':
            messagebox.showinfo(title='JOGO DA VELHA', message='X VENCEU')
            repetir()
        elif tabuleiro[0][2] == 'O':
            messagebox.showinfo(title='JOGO DA VELHA', message='O VENCEU')
            repetir()

    elif tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2]:
        if tabuleiro[0][0] == 'X':
            messagebox.showinfo(title='JOGO DA VELHA', message='X VENCEU')
            repetir()
        elif tabuleiro[0][0] == 'O':
            messagebox.showinfo(title='JOGO DA VELHA', message='O VENCEU')
            repetir()

    elif tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0]:
        if tabuleiro[0][2] == 'X':
            messagebox.showinfo(title='JOGO DA VELHA', message='X VENCEU')
            repetir()
        elif tabuleiro[0][2] == 'O':
            messagebox.showinfo(title='JOGO DA VELHA', message='O VENCEU')
            repetir()
    else:
        empate()

def x_o(pos):
    global linhas
    global colunas
    global cont
    global botao
    global tabuleiro
    global matriz_botoes
    global computador
    global human
    global cont_comp

    if tabuleiro[pos[0]][pos[1]] == 'X' or tabuleiro[pos[0]][pos[1]] == 'O':
        pass


    else:
        if computador != 1:
            if cont % 2 == 0:
                tabuleiro[pos[0]][pos[1]] = 'X'
                matriz_botoes[pos[0]][pos[1]].config(text='X', fg= 'blue')

            else:
                tabuleiro[pos[0]][pos[1]] = 'O'
                matriz_botoes[pos[0]][pos[1]].config(text='O', fg='red')

        else:
            cont_comp += 1
            tabuleiro[pos[0]][pos[1]] = human
            matriz_botoes[pos[0]][pos[1]].config(text=human, fg= velha2.cor_human)
            IA()
            janela.update()
    cont += 1
    #vencedor
    vencedor()

for linha in range(linhas):
    reta= []
    for coluna in range(colunas):
        botao = tk.Button(janela, text='', command=lambda l = linha, c= coluna: x_o((l , c)), height=botao_altura, width=botao_largura, bg='black',
                          fg = 'red')
        reta.append(botao)
        botao.grid(row=linha, column=coluna)
    matriz_botoes.append(reta)

#loop
janela.mainloop()

