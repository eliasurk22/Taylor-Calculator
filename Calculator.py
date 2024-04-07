import tkinter as tk
import math

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        # Create Entry widget to display result
        self.result = tk.Entry(master, width=16, font=('Arial', 16))
        self.result.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        # Create buttons for digits and operations
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'sin', 'cos', 'tan'
        ]
        row = 1
        col = 0
        for button in buttons:
            if col == 4:
                col = 0
                row += 1
            tk.Button(master, text=button, width=4, height=2, command=lambda x=button: self.click(x)).grid(row=row, column=col)
            col += 1

        # Create clear button
        tk.Button(master, text='C', width=4, height=2, command=lambda: self.clear()).grid(row=6, column=0)

    # Function to handle button clicks
    def click(self, key):
        if key == '=':
            try:
                result = eval(self.result.get())
                self.clear()
                self.result.insert(0, str(result))
            except:
                self.clear()
                self.result.insert(0, "Error")
        elif key == 'C':
            self.clear()
        elif key in ['sin', 'cos', 'tan']:
            try:
                if key == 'sin':
                    result = self.sin_taylor(float(self.result.get()))
                elif key == 'cos':
                    result = self.cos_taylor(float(self.result.get()))
                elif key == 'tan':
                    result = self.tan_taylor(float(self.result.get()))
                else:
                    result = eval('math.' + key + '(' + self.result.get() + ')')
                self.clear()
                self.result.insert(0, str(result))
            except:
                self.clear()
                self.result.insert(0, "Error")
        else:
            self.result.insert(tk.END, key)

    # Function to clear the result
    def clear(self):
        self.result.delete(0, tk.END)

    # Function to calculate sin using Taylor series expansion
    def sin_taylor(self, x):
        # Convert x to radians
        x = math.radians(x)

        # Initialize the sum and term
        sum = term = x

        # Iterate until the term becomes smaller than epsilon
        i = 1
        epsilon = 1e-10
        while abs(term) > epsilon:
            term *= -1 * x**2 / ((2*i) * (2*i+1))
            sum += term
            i += 1

        return sum
    def cos_taylor(x):
        # Convert x to radians
        x = math.radians(x)

        # Initialize the sum and term
        sum = term = 1

        # Iterate until the term becomes smaller than epsilon
        i = 1
        epsilon = 1e-10
        while abs(term) > epsilon:
            term *= -1 * x**2 / ((2*i) * (2*i-1))
            sum += term
            i += 1

        return sum

    def tan_taylor(x):
        # Convert x to radians
        x = math.radians(x)

        # Initialize the sum and term
        sum = term = x

        # Iterate until the term becomes smaller than epsilon
        i = 1
        epsilon = 1e-10
        while abs(term) > epsilon:
            term = 2 * math.pow(-1, i+1) * math.pow(x, 2*i - 1) / (2*i - 1)
            sum += term
            i += 1

        return sum

root = tk.Tk()
app = Calculator(root)
root.mainloop()
