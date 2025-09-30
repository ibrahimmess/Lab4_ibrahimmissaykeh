import tkinter as tk

def say_hello():
    label.config(text="Hello from Tkinter — Ibrahim Missaykeh")

root = tk.Tk()
root.title("Tkinter Demo — Ibrahim Missaykeh")
root.geometry("320x160")

label = tk.Label(root, text="Click the button (Tkinter)")
label.pack(pady=10)

btn = tk.Button(root, text="Say Hello", command=say_hello)
btn.pack(pady=10)

root.mainloop()
