import tkinter as tk
import tkinter.font as tkfont

janela = tk.Tk()
janela.title('Calculadora')

print('\033[34mHistórico:')

largura= 300
altura= 420

janela.maxsize(largura, altura)
janela.minsize(largura, altura)

#caixa de texto
cor_num= 'black'

# -- Fonte

fonte= tkfont.Font(size=32)

# -- frame pack

frame_pack = tk.Frame(janela)
frame_pack.pack()

# -- maximo de caracteres

caracteres_validar = ['7', '8', '9', '4', '5', '6', ':','3', '2', '1', 'x', '0', '+', '-']

cont_validar= 0


def validar_text(texto):

    while True:
        if len(texto) <= 30:
            return True

        else:
            return False



validacao = frame_pack.register(validar_text)



caixa = tk.Entry(frame_pack, width=largura, validate='key', validatecommand=(validacao, '%P'), font=fonte, state='readonly', fg=cor_num)
caixa.pack()


#botões

caracteres = ['C', '+', '-', 'Delete','7', '8', '9', '()', '4', '5', '6', ':','3', '2', '1', 'x', '%', '0', ',', '=']



largura_b= 6
altura_b= 3

butao= []

colunas= 4
linhas=5
cont= 0

c_caixa= [['C', '+', '-', 'Delete'],['7', '8', '9', '()'], ['4', '5', '6', ':'],['3', '2', '1', 'x'], ['%', '0', ',', '=']]



frame_grid = tk.Frame(janela)
frame_grid.pack()



#defs



def caractere(textinho):
    global cor_num
    caixa.config(state='normal')
    if cor_num != 'black':
        delete_all(textinho)
        cor_num= 'black'
        caixa.config(fg=cor_num)
    else:
        caixa.insert(tk.END, textinho)
    caixa.config(state='readonly')

def milhar(str):
    p=''
    cont_loop = 0
    s = str[::-1]

    if ',' in s:
        parte_virg= s.split(',')[1]
        print(parte_virg)

        for q in range(0, len(parte_virg)):
            if cont_loop != 0:
                if q % 3 == 0:
                    p+='.'
            p+=parte_virg[q]

            cont_loop+=1

        new_p= p[::-1]

        new_p+= ','+str.split(',')[1]

        print(new_p)

        return new_p


    else:

        for q in range(0, len(s)):
            if cont_loop != 0:
                if q % 3 == 0:
                    p+='.'
            p+=s[q]

            cont_loop+=1

        new_p= p[::-1]

        print(new_p)
        return new_p


def deletar():
    global cor_num

    caixa.config(state='normal')
    texto= caixa.get()
    new_text = texto[:-1]
    if cor_num != 'black':
        delete_all('')
        cor_num = 'black'
        caixa.config(fg=cor_num)
    else:
        caixa.delete(0, tk.END)
        caixa.insert(0, new_text)
    caixa.config(state='readonly')


def delete_all(n):
    caixa.config(state='normal')
    caixa.delete(0, tk.END)
    caixa.insert(tk.END, n)
    caixa.config(state='readonly')

def delete_all2():
    caixa.config(state='normal')
    caixa.delete(0, tk.END)
    caixa.insert(tk.END, '')
    caixa.config(state='readonly')


def paranteses():
    global cor_num
    caixa.config(state='normal')
    t= caixa.get()
    cont = 0
    for q in t:
        if q == '(':
            cont += 1
        elif q == ')':
            cont += 1

    if cont % 2 == 0:
        if cor_num != 'black':
            delete_all('(')
            cor_num = 'black'
            caixa.config(fg=cor_num)
        else:
            caixa.insert(tk.END, '(')

    else:
        if cor_num != 'black':
            delete_all('(')
            cor_num = 'black'
            caixa.config(fg=cor_num)
        else:
            caixa.insert(tk.END, ')')

    caixa.config(state='readonly')

def igual():
    global cor_num
    equac=''
    num = caixa.get()

    if num == "":
        final_num = ''
        inicio_num = ''

    else:
        final_num = num[-1]
        inicio_num = num[0]

    try:

        if final_num == inicio_num == num == "":
            return

        elif final_num == ':' or final_num == '+' or final_num == '-' or final_num == 'x' or inicio_num == ':' or inicio_num == '+' or inicio_num == '-' or inicio_num == 'x':
            cor_num = 'red'
            delete_all('Erro')
            caixa.config(fg=cor_num)

        else:
            equac= num
            for q in num:
                if q == ':':
                    num = num.replace(':', '/')
                if q == 'x':
                    num = num.replace('x', '*')
                if q == ',':
                    num= num.replace(',', '.')

            resultado = eval(num)

            if resultado % 1 == 0:
                resultado = int(resultado)



            res= str(resultado)
            res= res.replace('.', ',')

            if len(res) > 3:
                print('Hm')
                res = milhar(res)

            cor_num= 'green'
            caixa.config(fg=cor_num)
            delete_all(res)
            print(f'\033[32m\n{equac} = {res}')
    except:
        delete_all('Erro')
        cor_num= 'red'
        caixa.config(fg=cor_num)


for linha in range(linhas):
    reta= []
    for coluna in range(colunas):

        b = tk.Button(master = frame_grid, width= largura_b, height=altura_b, text=caracteres[cont], command=lambda l = linha, c= coluna: caractere(c_caixa[l][c]))

        if caracteres[cont] == 'Delete':
            b.config(bg= 'red', command=deletar)
        if caracteres[cont] == '=':
            b.config(bg= 'green', fg= 'white', command=igual)
        if caracteres[cont] == 'x':
            b.config(bg= 'blue', fg= 'white')
        if caracteres[cont] == ':':
            b.config(bg= 'blue', fg= 'white')
        if caracteres[cont] == '+':
            b.config(bg= 'blue', fg= 'white')
        if caracteres[cont] == '-':
            b.config(bg= 'blue', fg= 'white')

        if caracteres[cont] == '%':
            b.config(bg= 'blue', fg= 'white')
        if caracteres[cont] == '()':
            b.config(bg= 'blue', fg= 'white', command=paranteses)
        if caracteres[cont] == ',':
            b.config(bg= 'blue', fg= 'white')
        if caracteres[cont] == 'C':
            b.config(bg= 'red', fg= 'black', command=delete_all2)

        reta.append(b)
        b.grid(row=linha, column=coluna)
        cont+=1

    butao.append(reta)

janela.mainloop()