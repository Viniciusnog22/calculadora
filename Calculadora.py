from tkinter import *
from tkinter import Tk, ttk

#cores
co0 = "#f0f3f5"  # preto / black
co1 = "#feffff"  # branco / white
co2 = "#3fb5a3"  # verde  / green
co3 = "#38576b"  # valor  / value
co4 = "#403d3d"  # letra  / latters

# criando janelas 
janela = Tk()
janela.title('')
janela.geometry('310x300')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

# dividindo a janela

Frame_cima = Frame(janela, width=310, height=50, bg=co1, relief='flat')
Frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

Frame_baixo = Frame(janela, width=310, height=250, bg=co2, relief='flat')
Frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)



# configurando frame de cima
l_nome = Label(Frame_cima, text='LOGIN', anchor=NE,font=('Ivy 25'), bg=co1, fg=co4)
l_nome.place(x=5, y=5)

l_nome = Label(Frame_cima, text='', width=235,  anchor=NW,font=('Ivy 1'), bg=co2, fg=co4)
l_nome.place(x=10, y=45)



# configurando o framde de baixo

l_nome = Label(Frame_baixo, text='Nome *', anchor=NW,font=('Ivy 10'), bg=co1, fg=co4)
l_nome.place(x=10, y=20)

e_nome = Entry(Frame_baixo, width=25, justify='left',font=("", 15), highlightthickness=1, relief='solid')
e_nome.place(x=14, y=50)