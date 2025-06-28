import tkinter as tk

def on_click(char):
    current = entry.get()
    if char == 'C':
        entry.delete(0, tk.END)
    elif char == '=':
        try:
            expression = current.replace('×', '*').replace('÷', '/')
            result = eval(expression)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    else:
        entry.insert(tk.END, char)

root = tk.Tk()
root.title("Simple Calculator")

entry = tk.Entry(root, width=20, font=('Arial', 18), borderwidth=2, relief='ridge', justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('÷', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('×', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
    ('=', 5, 0, 4)
]

for (text, row, col, *span) in buttons:
    colspan = span[0] if span else 1
    tk.Button(root, text=text, width=5, height=2, font=('Arial', 16),
              command=lambda char=text: on_click(char)).grid(row=row, column=col, columnspan=colspan, sticky='nsew', padx=2, pady=2)

root.mainloop()