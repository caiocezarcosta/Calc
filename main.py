from calculadora_gui import make_buttons,make_display,make_label,make_root
from classe_calculadora import Calculator
def main():
    root = make_root()
    display = make_display(root)
    buttons = make_buttons(root)
    label   = make_label(root)
    calculador = Calculator(root,label,display,buttons)
    calculador.start()
if __name__ == '__main__':
    main()