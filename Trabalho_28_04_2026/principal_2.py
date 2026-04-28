import tkinter

raiz = tkinter.Tk()
raiz.title("Calculadora")

texto = tkinter.Entry() #criar o campo de texto
texto.pack()

def ligar_lampada_1():
    print("Lampada 1 ligada")

def ligar_lampada_2():
    print("Lampada 2 ligada")

#criar o botao
botao1 = tkinter.Button(text="1", command=ligar_lampada_1)
botao1.pack(side=tkinter.LEFT, padx=5)
botao2 = tkinter.Button(text="2", command=ligar_lampada_2)
botao2.pack(side=tkinter.LEFT, padx=5)       
botao3 = tkinter.Button(text="3")
botao3.pack(side=tkinter.LEFT, padx=5)
botao4 = tkinter.Button(text="4")
botao4.pack(side=tkinter.LEFT, padx=5)
botao5 = tkinter.Button(text="5")
botao5.pack(side=tkinter.LEFT, padx=5)
botao6 = tkinter.Button(text="6")
botao6.pack(side=tkinter.LEFT, padx=5)
botao7 = tkinter.Button(text="7")
botao7.pack(side=tkinter.LEFT, padx=5)
botao8 = tkinter.Button(text="8")
botao8.pack(side=tkinter.LEFT, padx=5)
botao9 = tkinter.Button(text="9")
botao9.pack(side=tkinter.LEFT, padx=5)
botao0 = tkinter.Button(text="0")
botao0.pack(side=tkinter.LEFT, padx=5)
#envialo para o interface

botao1.pack()
botao2.pack()
botao3.pack()
botao4.pack()
botao5.pack()
botao6.pack()
botao7.pack()
botao8.pack()
botao9.pack()
botao0.pack()


#arrancar com o interface
raiz.mainloop() 
