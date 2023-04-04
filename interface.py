from tkinter import *

from tkinter import filedialog

def browseFiles():
	filename = filedialog.askopenfilename(initialdir = "/",title = "Select a File", filetypes = (("Arquivos PDF","*.pdf*"),	("Todos os Arquivos","*.*")))
	
	label_file_explorer.configure(text="Arquivo aberto: "+filename)
	
window = Tk()

w = 800 # width for the Tk root
h = 500 # height for the Tk root

# get screen width and height
ws = window.winfo_screenwidth() # width of the screen
hs = window.winfo_screenheight() # height of the screen

x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

window.geometry('%dx%d+%d+%d' % (w, h, x, y))

window.title('Sistema de leitura de cartões ponto')

window.config(background = "white", width=800)

frame = Frame(window)
frame.place(relx=0.5, rely=0.5, anchor='center')
	
label_file_explorer = Label(frame,	text = "Arquivo à selecionar", height = 4,fg = "blue")
button_explore = Button(frame, text = "Procurar arquivo", command = browseFiles)

checkbox_cp_01 = Checkbutton(frame, offvalue="older", text='Modelo Antigo')
checkbox_cp_02 = Checkbutton(frame, offvalue="newest", text='Modelo Atual')

label_model_ask = Label(frame, text="Selecione o modelo do cartão ponto")
label_cp_01 = Label(frame, text="Modelo antigo")
label_cp_02 = Label(frame, text="Modelo atual")


label_file_explorer.grid(column = 1, row = 1)

button_explore.grid(column = 1, row = 2)

label_model_ask.grid(column=1, row=3)

checkbox_cp_01.grid(column = 0, row = 4)
checkbox_cp_02.grid(column = 1, row = 4)
window.mainloop()
