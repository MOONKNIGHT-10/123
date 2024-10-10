from tkinter import Tk, Entry, Button, StringVar

class Calculator:
    def __init__(self, master):
        master.title("Calculator")
        master.geometry('357x420+0+0')
        master.config(bg='gray')
        master.resizable(False, False)

        self.equation = StringVar()
        self.entry_value = ''

        Entry(master, width=17, bg='#fff', font=('Arial Bold', 28), textvariable=self.equation).place(x=0, y=0)

        # Define buttons and their positions
        buttons = [
            ('7', 0, 60), ('8', 60, 60), ('9', 120, 60), ('/', 180, 60),
            ('4', 0, 120), ('5', 60, 120), ('6', 120, 120), ('*', 180, 120),
            ('1', 0, 180), ('2', 60, 180), ('3', 120, 180), ('-', 180, 180),
            ('0', 0, 240), ('.', 60, 240), ('+', 120, 240), ('=', 180, 240),
            ('C', 0, 300)
        ]

        for (text, x, y) in buttons:
            if text == 'C':
                Button(master, text=text, width=6, height=2, command=self.clear).place(x=x, y=y)
            elif text == '=':
                Button(master, text=text, width=6, height=2, command=self.solve).place(x=x, y=y)
            else:
                Button(master, text=text, width=6, height=2, command=lambda t=text: self.show(t)).place(x=x, y=y)

    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)

    def solve(self):
        try:
            result = eval(self.entry_value)
            self.equation.set(result)
        except Exception as e:
            self.equation.set('Error')

if __name__ == '__main__':
    root = Tk()
    calculator = Calculator(root)
    root.mainloop()
