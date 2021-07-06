

from tkinter import *
L=["hello","bye","dfhdf","ldfflk","lsfhk","fflkfdh"]
top = Tk()

mb=  Menubutton ( top, text="CheckComboBox", relief=RAISED )
mb.grid()
mb.menu  =  Menu ( mb, tearoff = 0 )
mb["menu"]  =  mb.menu

Item0 = IntVar()
Item1 = IntVar()
Item2 = IntVar()
def f():
	x=Item0.get()
	y=Item1.get()
	z=Item2.get()
	print(x,y,z)
mb.menu.add_checkbutton( label="Item0", variable=Item0)
mb.menu.add_checkbutton( label="Item1", variable=Item1)
mb.menu.add_checkbutton( label="Item2", variable=Item2)

mb.pack()
top.mainloop()








# window = tk.Tk()
# window.title('BAR SELECT DROPDOWN')
# window.geometry('500x250')
# ttk.Label(window, text = "Btao Bhai Konsa Plot Karna Hai",
# 		background = 'green', foreground ="white",
# 		font = ("Times New Roman", 15)).grid(row = 0, column = 1)
# ttk.Label(window, text = "Select The Site for which you want to plot:",
# 		font = ("Times New Roman", 10)).grid(column = 0,
# 		row = 5, padx = 10, pady = 25)
# selectedSite=StringVar()
# selectedSite = ttk.Combobox(window, width = 27, textvariable = Chosengraph)
# selectedSite['values'] = ('BA3A0138B11','LA3A0138B31','EA3A0138B31','DA3A0138B31')
# selectedSite.grid(column = 1, row = 5)
# selectedGraph.current()
# window.mainloop()

