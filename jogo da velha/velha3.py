import tkinter as tk


#Janela
janela = tk.Tk()
largura= 300

janela.title('JOGO DA VELHA')
janela.config(background='black')
janela.maxsize(300, 300)
janela.minsize(300, 300)

texto = tk.Label(janela, text='\nQUE MODO DESEJA JOGAR?', fg='white', bg= 'black')
texto.pack()

#Botôes


def opcao1():
    global janela
    global contvelha3
    contvelha2= 0
    contvelha2+=1

    if contvelha2 == 1:
        janela.destroy()




computador= 0
def opcao2():
    global computador
    computador = 1
    janela.destroy()





largura_botao= 10
altura_botao= 2

janela.update()


botao1= tk.Button(janela, command=opcao1, width=largura_botao, height=altura_botao, text='2 JOGADORES', fg='white', bg= 'black')
botao1.pack()


botao2= tk.Button(janela, command=opcao2, width=largura_botao, height=altura_botao, text='COMPUTADOR', fg='white', bg='black')
botao2.pack()

janela.update()

botao1.place(relx=0.5, rely= 0.4, anchor=tk.CENTER)
botao2.place(relx=0.5 , rely= 0.6, anchor=tk.CENTER)

janela.mainloop()