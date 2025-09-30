import tkinter as tk

def say_hello():
    label.config(text="Hello from Tkinter!")

root = tk.Tk()
root.title("Tkinter Demo")
root.geometry("320x160")

label = tk.Label(root, text="Click the button")
label.pack(pady=10)

btn = tk.Button(root, text="Say Hello", command=say_hello)
btn.pack(pady=10)

root.mainloop()
