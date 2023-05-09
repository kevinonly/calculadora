# Importação da biblioteca TKinter:
from tkinter import *


# Configuração da janela:
screen = Tk()
screen.title('Calculadora')
screen.geometry('316x420')
screen.configure(bg='#999')
# Criação de váriaveis:
inicial = StringVar()
inicial.set('Insira uma conta!')
var_text = StringVar()
conta = ''


# Criando as funções dos botões

# Função pra exibir números no display
def mudar(valor):
    global var_text
    global conta
    global inicial
    inicial.set('')
    conta += valor
    var_text.set(conta)


# Função pra resolver e exibir o resultado da conta
def calcular():
    global conta
    global inicial
    try:
        result = eval(entry.get())
        conta = ''
        inicial.set(f'{entry.get()} = {result}')
        var_text.set('')
    except SyntaxError:
        inicial.set('Conta inválida!')
        var_text.set('')
    except NameError:
        inicial.set('Conta inválida!')
        var_text.set('')


# Função pra limpar as váriaveis de conta e texto do display
def limpar():
    global conta
    conta = ''
    var_text.set(conta)


# Criação de uma classe pra gerenciamento dos botões:
class Teclas:
    # Métodos da classe
    def exibe(self, pai, texto, linha, coluna, value, bgd='#fff'):
        cria = Button(master=pai, text=texto, width=6, height=3, bd=4, bg=bgd,
                      font=('Arial', 12, 'bold'),  command=lambda: mudar(value))
        cria.grid(row=linha, column=coluna)
        return cria

    def faz_calculo(self, pai, texto, linha, coluna):
        r = Button(master=pai, text=texto, width=6, height=3, bd=4, bg='#d4cfcb',
                   font=('Arial', 12, 'bold'), command=lambda: calcular())
        r.grid(row=linha, column=coluna)
        return r

    def limpeza(self, pai, texto, linha, coluna):
        cria = Button(master=pai, text=texto, width=6, height=3, bd=4, bg='#d4cfcb',
                      font=('Arial', 12, 'bold'),  command=lambda: limpar())
        cria.grid(row=linha, column=coluna)
        return cria


# Divisão da janela em frames pra organizar:
frame_entry = Frame(screen, width=300, height=100, bg='#999')
frame_entry.pack()

frame_botoes = Frame(screen, width=300, height=300, bg='#222')
frame_botoes.place(x=10, y=104)

# Adicionando widgets de entrada e saida de informações:
label_resultados = Label(screen, textvariable=inicial, width=29, height=2,
                         bg='#999', font=('Arial', 13, 'italic bold'), relief=FLAT)
label_resultados.place(x=10, y=56)

entry = Entry(frame_entry, textvariable=var_text, font=('Arial', 14, 'bold'),
              bd=3,relief=SUNKEN, bg='#fff')
entry.place(x=12, y=10, height=40, width=274)

# Criando os botões com a função da classe Teclas:
btnClear = Teclas().limpeza(frame_botoes, 'C', 0, 0)
btnIgual = Teclas().faz_calculo(frame_botoes, '=', 0, 2)
btn0 = Teclas().exibe(frame_botoes, '0', 0, 1, '0')
btn1 = Teclas().exibe(frame_botoes, '1', 1, 0, '1')
btn2 = Teclas().exibe(frame_botoes, '2', 1, 1, '2')
btn3 = Teclas().exibe(frame_botoes, '3', 1, 2, '3')
btn4 = Teclas().exibe(frame_botoes, '4', 2, 0, '4')
btn5 = Teclas().exibe(frame_botoes, '5', 2, 1, '5')
btn6 = Teclas().exibe(frame_botoes, '6', 2, 2, '6')
btn7 = Teclas().exibe(frame_botoes, '7', 3, 0, '7')
btn8 = Teclas().exibe(frame_botoes, '8', 3, 1, '8')
btn9 = Teclas().exibe(frame_botoes, '9', 3, 2, '9')
btnX = Teclas().exibe(frame_botoes, 'x', 0, 3, '*', '#d97218')
btnDiv = Teclas().exibe(frame_botoes, '/', 1, 3, '/', '#d97218')
btnMais = Teclas().exibe(frame_botoes, '+', 2, 3, '+', '#d97218')
btnMenos = Teclas().exibe(frame_botoes, '_', 3, 3, '-', '#d97218')

# Setando foco pro campo de input com método .bind():
entry.focus_set()
# Definindo ação para pressionamento da tecla Enter:
entry.bind("<Return>", lambda e: calcular())

# Uso do .mainloop() pra manter interface ativa
screen.mainloop()