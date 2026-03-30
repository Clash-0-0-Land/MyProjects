import tkinter as tk
from tkinter import messagebox



#Janela e texto

janela = tk.Tk()
janela.config(background='black')
janela.title('JOGO DA VELHA')
janela.maxsize(300, 300)
janela.minsize(300, 300)

texto = tk.Label(janela, text='\nESCOLHA UMA DAS OPÇÕES ABAIXO:', fg='white', bg='black')
texto.pack()



#Botões

contvelha2 = 0

robot=''
human = ''
cor_human = ''
cor_robot= ''

def opcao1():
    global human
    global janela
    global contvelha2
    global robot
    global cor_human
    global cor_robot

    contvelha2+=2
    janela.destroy()
    human= 'X'
    cor_human = 'blue'


    robot= 'O'
    cor_robot = 'red'

def opcao2():
    global human
    global janela
    global contvelha2
    global robot
    global cor_human
    global cor_robot

    contvelha2+=1
    janela.destroy()

    human = 'O'
    cor_human = 'red'


    robot= 'X'
    cor_robot = 'blue'

largura = 10
altura = 5

botao1 = tk.Button(janela, command=opcao1, text='X', fg='blue', width=largura, height=altura, bg='black')
botao1.pack(side=tk.LEFT)

botao2 = tk.Button(janela, command=opcao2, text='O', fg='red', width=largura, height=altura, bg='black')
botao2.pack(side=tk.LEFT)

janela.pack_propagate(0)
janela.update()
largura_janela = janela.winfo_width()

botao1.place(relx=0.3, rely=0.5, anchor=tk.CENTER)
botao2.place(relx=0.7, rely=0.5, anchor=tk.CENTER)

janela.mainloop()
