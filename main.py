from calculadora import make_root, make_label, make_display, make_botoes
from calculadora_classe import Calculadora

def main():
    root = make_root()
    label = make_label(root)
    display = make_display(root)
    botoes = make_botoes(root)
    calculator = Calculadora(root, label, display, botoes)
    calculator.inicio()


if __name__ == '__main__':
    main()
