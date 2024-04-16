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
janela.geometry("235x318") # Definindo as dimensões da janela
janela.config(bg=preto) # Definindo a cor da janela

# Criando um frame para a tela da calculadora
frame_tela = Frame(janela, width=235, height=50) # Criando um Frame
frame_tela.grid(row=0, column=0) # Posicionando o frame na primeira linha (row=0), primeira coluna (column=0) da janela

frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)

# Iniciando o loop principal da interface gráfica (GUI)
janela.mainloop()
