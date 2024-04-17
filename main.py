# Importando o tkinter
from tkinter import *
from tkinter import ttk

# Cores

preto = "#3b3b3b"
branco = "#feffff"
azul = "#38576b"
cinza = "#ECEFF1"
laranja = "#FFAB40"

# Criando a janela principal
janela = Tk()
janela.title("Calculadora") # Definindo o título da janela
janela.geometry("236x310") # Definindo as dimensões da janela
janela.config(bg=preto) # Definindo a cor da janela

# Criando um frame para a tela da calculadora
frame_tela = Frame(janela, width=236, height=50, bg=azul) # Criando um Frame
frame_tela.grid(row=0, column=0) # Posicionando o frame na primeira linha (row=0), primeira coluna (column=0) da janela

frame_corpo = Frame(janela, width=236, height=268)
frame_corpo.grid(row=1, column=0)

# Criando os botoes

# Botao de apagar
b_1 = Button(frame_corpo, text="C", width=11, height=2, bg=cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) 
b_1.place(x=0, y=0)

# Botao do resto de divisao
b_2 = Button(frame_corpo, text="%", width=5, height=2, bg=cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) 
b_2.place(x=118, y=0)

# Botao da divisao
b_3 = Button(frame_corpo, text="/", width=5, height=2, bg=laranja, fg=branco, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) 
b_3.place(x=177, y=0)

# Botoes de numeros do 7 ao 9
b_4 = Button(frame_corpo, text="7", width=5, height=2, bg=cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) 
b_4.place(x=0, y=52)

b_5 = Button(frame_corpo, text="8", width=5, height=2, bg=cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) 
b_5.place(x=59, y=52)

b_6 = Button(frame_corpo, text="9", width=5, height=2, bg=cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) 
b_6.place(x=118, y=52)

b_7 = Button(frame_corpo, text="*", width=5, height=2, bg=laranja, fg=branco, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) 
b_7.place(x=177, y=52)

# Botoes de numeros do 4 ao 6

b_8 = Button(frame_corpo, text="4", width=5, height=2, bg=cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) 
b_8.place(x=0, y=104)

b_9 = Button(frame_corpo, text="5", width=5, height=2, bg=cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) 
b_9.place(x=59, y=104)

b_10 = Button(frame_corpo, text="6", width=5, height=2, bg=cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) 
b_10.place(x=118, y=104)

b_11 = Button(frame_corpo, text="-", width=5, height=2, bg=laranja, fg=branco, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) 
b_11.place(x=177, y=104)

# Botoes de numeros do 1 ao 3

b_12 = Button(frame_corpo, text="1", width=5, height=2, bg=cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) 
b_12.place(x=0, y=156)

b_13 = Button(frame_corpo, text="2", width=5, height=2, bg=cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) 
b_13.place(x=59, y=156)

b_14 = Button(frame_corpo, text="3", width=5, height=2, bg=cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) 
b_14.place(x=118, y=156)

b_15 = Button(frame_corpo, text="+", width=5, height=2, bg=laranja, fg=branco, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) 
b_15.place(x=177, y=156)

# Botao doo 0
b_16 = Button(frame_corpo, text="0", width=11, height=2, bg=cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) 
b_16.place(x=0, y=208)

# Botao do .
b_17 = Button(frame_corpo, text=".", width=5, height=2, bg=cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) 
b_17.place(x=118, y=208)

# Botao de =
b_18 = Button(frame_corpo, text="=", width=5, height=2, bg=laranja, fg=branco, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) 
b_18.place(x=177, y=208)

# Iniciando o loop principal da interface gráfica (GUI)
janela.mainloop()
