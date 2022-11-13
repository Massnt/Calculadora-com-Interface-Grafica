import tkinter as tk
from typing import List

def make_root() -> tk.Tk:
    root = tk.Tk()
    root.title('Calculadora 2000')
    root.config(padx=10, pady=10, background='#DCDCDC')
    root.resizable(False, False)
    return root


def make_label(root) -> tk.Label:
    label = tk.Label(
        root, text='Sem Operação',
        anchor='e', justify='left', background='#DCDCDC'
    )
    label.grid(row=0, column=0, columnspan=5, sticky='news')
    return label


def make_display(root) -> tk.Entry:
    display = tk.Entry(root)
    display.grid(row=1, column=0, columnspan=5, pady=(0, 10))
    display.config(
        font=('Verdana', 40, 'normal'),
        justify='left', bd=1, relief='flat',
        highlightthickness=1, highlightcolor='#ccc'
    )
    display.bind('<Control-a>', _display_control_a)
    return display


def _display_control_a(event):
    event.widget.select_range(0, 'end')
    event.widget.icursor('end')
    return 'break'


def make_botoes(root) -> List[List[tk.Button]]:
    botoes_texto : List[List[str]] = [
        ['7', '8', '9', '/', '√', 'L'],
        ['4', '5', '6', '+', '-'],
        ['1', '2', '3', '*', '^'],
        ['0', '.', '(', ')', '='],
    ]

    botoes : List[List[tk.Button]] = []

    for row, row_value in enumerate(botoes_texto, start=2):
        botoes_row = []
        for col_index, col_value in enumerate(row_value):
            btn = tk.Button(root, text=col_value)
            btn.grid(row=row, column= col_index, sticky='news',padx=5, pady=5)
            btn.config(
                font=('Verdana', 15, 'normal'),
                pady=40, width=1, background='#f1f2f3', bd=0,
                cursor='hand2', highlightthickness=0,
                highlightcolor='#ccc', highlightbackground='#ccc',
                activebackground='#ccc'
            )
            botoes_row.append(btn)
        botoes.append(botoes_row)
    return botoes

