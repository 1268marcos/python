# Autor : Marcos Santos
# print('olá mundo')
# pip install requests
# pip install babel
from tkinter import *
from tkinter import ttk
from urllib import response
from babel.numbers import format_currency
import requests
import json 
cor0 = "#ffffff" #branca
cor1 = "#fefefe" #branca areia
cor2 = "#a63c81" #roxo claro
cor_fundo = "#81bf24" #verde limao
janela = Tk()
janela.title('@marcosprofdigital')
janela.geometry('320x350')
janela.configure(bg=cor_fundo)
ttk.Separator(janela).grid(row=0, columnspan=1, ipadx=157)
frame_superior = Frame(janela, width=320, height=50, bg=cor0)
frame_superior.grid(row=1, column=0)
frame_inferior = Frame(janela, width=320, height=300, bg=cor_fundo)
frame_inferior.grid(row=2, column=0)
tempo = 0
def atualizar_info():
    global tempo
    api_link = 'https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,BRL,EUR,ARS'
    response = requests.get(api_link)
    dados = response.json()
    valor_real = float(dados['BRL'])
    valor_formatado_reais = format_currency(valor_real, 'BRL', locale='pt_BR')
    texto_preco_reais['text'] = valor_formatado_reais
    valor_dolar = float(dados['USD'])
    valor_formatado_dolares = "US$ {:,.3f}".format(valor_dolar)
    texto_preco_dolares['text'] = valor_formatado_dolares
    tempo +=1
    texto_tempo['text'] = "Tempo: " + str(tempo) + " segundo(s)"
    frame_inferior.after(1000, atualizar_info)
texto_aviso = Label(frame_superior, text='Cotação 1 BitCoin =', bg=cor1, fg=cor2, font=('Arial 20'))
texto_aviso.place(x=10, y=10)
texto_preco_reais = Label(frame_inferior, text='Reais', bg=cor_fundo, fg=cor1, font=('Arial 28'))
texto_preco_reais.place(x=10, y=50)
texto_preco_dolares = Label(frame_inferior, text='Dolares', bg=cor_fundo, fg=cor1, font=('Arial 14'))
texto_preco_dolares.place(x=10, y=100)
texto_tempo = Label(frame_inferior, text='Tempo', bg=cor_fundo, fg=cor2, font=('Arial 11'))
texto_tempo.place(x=10, y=150)

atualizar_info()

janela.mainloop()
