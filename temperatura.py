from tkinter import *
from tkinter import ttk
from urllib import response
from babel.numbers import format_currency
import requests
import json 
janela = Tk()
janela.geometry('500x500')
ttk.Separator(janela).grid(row=0, columnspan=1, ipadx=350)
api_link = 'https://weather.contrateumdev.com.br/api/weather/city/?city=Barueri'
response = requests.get(api_link)
dados = response.json()
janela.title('Transformação Digital a temperatura é ' + str(dados['main']['feels_like']))
janela.mainloop()
