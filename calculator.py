import tkinter as tk

def click(event):
    current = entry.get()
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(current)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("400x500")

# Entry field for user input
entry = tk.Entry(root, font="Arial 20", borderwidth=5, relief=tk.RIDGE, justify=tk.RIGHT)
entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

# Frame to hold buttons
button_frame = tk.Frame(root)
button_frame.pack()

# Button layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
    ["C"]
]

for row in buttons:
    row_frame = tk.Frame(button_frame)
    row_frame.pack(expand=True, fill="both")
    for btn in row:
        button = tk.Button(row_frame, text=btn, font="Arial 18", relief=tk.GROOVE)
        button.pack(side="left", expand=True, fill="both", padx=2, pady=2)
        button.bind("<Button-1>", click)

# Run the application
root.mainloop()
