from tkinter import *
import yfinance as yf
import pandas as pd
import pandas_datareader as data
yf.pdr_override()

#Função para ler o ticker
tickers = []
#def ler_ticker():
    #tickers.append(entry.get())
    #print(tickers)
    #return tickers
#Função para procurar ticker
def procura_ticker():
    acao = entry.get()
    acao = data.get_data_yahoo(acao)
    print(acao)

#Tela do app
tela1 = Tk()
#Caixa de entrada
entry = Entry(tela1)
entry.pack()
#Botão para pegar o ticker
#botao_ticker = Button(tela1,text = "Clique para entrar o ticker", command = ler_ticker)
#botao_ticker.pack()
#Botão para imprim
botao_proc = Button(tela1,text = "Procure ticker", command = procura_ticker)
botao_proc.pack()
#Botão para sair do app
botao_saida = Button(tela1,text = "Clique para sair", command = tela1.quit)
botao_saida.pack()



tela1.mainloop()

