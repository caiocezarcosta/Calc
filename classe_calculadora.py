import re
import tkinter as tk
from typing import List
import math 
class Calculator:
    '''teste'''
    def __init__(self ,
                 root: tk.Tk ,
                 label: tk.Label,
                 display: tk.Entry,
                 buttons: List[List[tk.Button]]
                 ):
        self.root = root
        self.label = label
        self.display = display
        self.buttons = buttons
        
    def start(self):
        self.config_buttons()
        self.config_display()
        self.root.mainloop()
        
        
    def config_buttons(self):
        button = self.buttons
        for row_values in button:
            for button in row_values:
                button_text = button['text']
                if button_text == 'C':
                    button.bind('<Button-1>', self.clear)
                if button_text in '0123456789/*-+.()':
                    button.bind('<Button-1>' , self.textToDisplay)
                if button_text == '=':
                    button.bind('<Button-1>',self.calculate)
    def config_display(self):
        fixed_text = self.fixText(self.display.get())
        self.display.bind('<Return>',self.calculate)
        
        
    def fixText(self, text):
        text = re.sub(r'[^\d\.\/\*\-\+\^\(\)e]', r'', text, 0)
        text = re.sub(r'([\.\+\/\-\*\^])\1+', r'\1', text, 0)
        text = re.sub(r'\*?\(z\)', '',text)

        return text
    def clear(self, event= None):
        self.display.delete(0,'end')
        
    def textToDisplay(self, event = None):
        self.display.insert('end', event.widget['text'])
        
    def calculate(self, event = None):
        fixed_text = self.fixText(self.display.get())
        equations = self._get_equations(fixed_text)
        
        try:
            if len(equations) == 1:
                result =eval(self.fixText(equations[0]))
            else:
                result = eval(self.fixText(equations[0]))
                for equation in equations[1:]:
                    result.math.pow(result,eval(self.fixText(equations)))
            self.display.delete(0,'end')
            self.display.insert('end',result)
            self.label.config(text=f'{fixed_text} = {result}')
        
        except Exception as e:
            print(e)
            self.label.config(text = 'Conta inválida')
       
    def _get_equations(self,text):
        return re.split(r'\^',text,0)