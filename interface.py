import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd

root = tk.Tk()
text = tk.Text(root, height=12)
root.geometry('300x110')
root.title('Automatizador de Digitação')
ttk.Label(root, text='Classic Label', foreground="#0066ff", font=('Silkscreen',12)).pack()
def callback():
	f = fd.askopenfile()    
	text.insert('1.0', f.readlines())
ttk.Button(
   root, 
   text="Demo Button", 
   command=callback
).pack()

root.mainloop()
