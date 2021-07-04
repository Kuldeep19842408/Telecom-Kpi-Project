from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt
Df=pd.DataFrame()
window = Tk()
chosenKpi= StringVar()
chosenCell=StringVar()
def browseFiles():
	filename = filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("CSV Files","*.csv*"),("Excel Files","*.xls*")))
	global Df
	Df=pd.read_csv(filename)
	button_plot.grid(column=1,row=8)
	fileState= Label(window,text="CSV Uploaded").grid(column=1,row=3)
	selectedCell['values']= list(set(Df['CELL'].tolist()))
	headers=list(Df.columns.values)
	headers.remove("CELL")
	headers.remove("PERIOD_START_TIME")
	selectedKPI['values']=headers
def plot():
	KPI=chosenKpi.get()
	CELL=chosenCell.get()
	GRAPH=Graphchosen.get()
	DF=Df.loc[(Df["CELL"]==CELL)]
	DF.plot(kind=GRAPH,x="PERIOD_START_TIME",y=KPI)
	plt.show()
	chosenKpi.set("")
	chosenCell.set("")
	Graphchosen.set("")
window.title('File Explorer')
window.geometry("500x500")
window.config(background = "white")

label_file_explorer = Label(window,text = "Upload your CSV ",width = 100, height = 4,fg = "blue")	
button_explore = Button(window,text = "Browse Files",command = browseFiles)
button_plot=Button(window,text="plot",command=plot)
label_file_explorer.grid(column = 1, row = 1)
button_explore.grid(column = 1, row = 2)
ttk.Label(window, text = "CELL v/s KPI",
		background = 'green', foreground ="white",
		font = ("Times New Roman", 15)).grid(row = 0, column = 1)
ttk.Label(window, text = "Select The KPI for which you want to plot:",
		font = ("Times New Roman", 10)).grid(column = 0,
		row = 5, padx = 10, pady = 25)
ttk.Label(window, text = "Select The CELL for which you want to plot:",
		font = ("Times New Roman", 10)).grid(column = 0,
		row = 6, padx = 10, pady = 25)
selectedCell = ttk.Combobox(window, width = 27, textvariable = chosenCell)
selectedCell['values'] = ['Upload Your CSV First']
selectedCell.grid(column = 1, row = 5)
ttk.Label(window, text = "Select The Graph for which you want to plot:",
		font = ("Times New Roman", 10)).grid(column = 0,
		row = 7, padx = 10, pady = 25)
Graphchosen=StringVar()
selectedGraph = ttk.Combobox(window, width = 27, textvariable = Graphchosen)
selectedGraph['values'] = ('bar','line','scatter')
selectedGraph.grid(column = 1, row = 5)
selectedKPI = ttk.Combobox(window, width = 27, textvariable = chosenKpi)
selectedKPI['values'] = ['Upload Your CSV First']
selectedKPI.grid(column = 1, row = 5)
selectedCell.grid(column=1,row=6)
selectedGraph.grid(column=1,row=7)
window.mainloop()






# Site=selectedSite.get()
# Sitechosen.set("")
# ttk.Label(window, text = "Select The Site for which you want to plot:",
# 		font = ("Times New Roman", 10)).grid(column = 0,
# 		row = 8, padx = 10, pady = 25)
# selectedSite=StringVar()
# selectedSite = ttk.Combobox(window, width = 27, textvariable = Sitechosen)
# selectedSite['values'] = ('BA3A0138B11','LA3A0138B31','EA3A0138B31','DA3A0138B31')
# selectedSite.grid(column = 1, row = 8)