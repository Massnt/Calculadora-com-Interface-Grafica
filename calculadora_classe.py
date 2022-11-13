import re
import math
import tkinter as tk
from typing import List


class Calculadora:
    def __init__(self, root: tk.Tk, label: tk.Label, display: tk.Entry, botoes: List[List[tk.Button]]):
        self.root = root
        self.label = label
        self.display = display
        self.botoes = botoes


    def inicio(self):
        self._config_botoes()
        self._config_display()
        self.root.mainloop()


    def _config_botoes(self):
        botoes = self.botoes

        for row_values in botoes:
            for botao in row_values:
                botao_texto = botao['text']

                if botao_texto == 'L':
                    botao.bind('<Button-1>', self.limpa)
                    botao.config(bg='#0000CD', fg='#fff')
                if botao_texto in '0123456789.+-/*()√^':
                    botao.bind('<Button-1>', self.adiciona_display)
                if botao_texto == '=':
                    botao.bind('<Button-1>', self.calcular)
                '''if botao_texto == '√':
                    self.root.bind('<Button-1>', self.raiz)'''



    def _config_display(self):
        self.display.bind('<Return>', self.calcular)
        self.display.bind('<Delete>', self.limpa)



    def _fixa_texto(self, text):
        text = re.sub(r'[^\d\.\/\*\-\+\^\√\(\)e]', r'', text, 0)
        text = re.sub(r'([\.\/\*\-\+\^\√])\1+', r'\1', text, 0)
        text = re.sub(r'\*?\(\)', '', text)

        return text


    def limpa(self, event=None):
        self.display.delete(0, 'end')


    def adiciona_display(self, event=None):
        self.display.insert('end', event.widget['text'])


    def calcular(self, event=None):
        fixa_texto = self._fixa_texto(self.display.get())
        equacoes = self.pega_equacoes(fixa_texto)

        try:
            if len(equacoes) == 1:
                resultado = eval(self._fixa_texto(equacoes[0]))
            else:
                resultado= eval(self._fixa_texto(equacoes[0]))
                for equacoes in equacoes[1:]:
                    resultado = math.pow(resultado, eval(self._fixa_texto(equacoes)))

            self.display.delete(0,'end')
            self.display.insert('end', resultado)
            self.label.config(text=f'{fixa_texto} = {resultado}')



        except OverflowError:
            self.label.config(text='Excedido o número do calculo')
        except Exception:
            self.label.config(text='Operação Invalida')



    def pega_equacoes(self, text):
        return re.split(r'\^', text, 0)
