from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt
Df=pd.DataFrame()
window = Tk()
chosenKpi= StringVar()
chosenCell=StringVar()
Sitechosen=StringVar()
CellState=[]
ListOfCells=[]
def browseFiles():
	filename = filedialog.askopenfilename(initialdir = "/home/kartik/Downloads",title = "Select a File",filetypes = (("CSV Files","*.csv*"),("Excel Files","*.xls*")))
	global Df
	global CellState
	for i in range(50):
		x=IntVar(0)
		CellState.append(x)
	Df=pd.read_csv(filename)
	button_plot.grid(column=1,row=9)
	fileState= Label(window,text="CSV Uploaded").grid(column=1,row=3)
	KPIHeaders=[]  
	NonKPIHeaders=[] 
	for column in Df:
		flagCheckNumber=True
		ListToStoreValues=[]
		for row in Df[column].tolist():
			if(type(row)!=type("")):
				ListToStoreValues.append(row)
			else:
				value=''.join(row.split(","))
				if(value[0]=='-'):
					value=value[1:]
					if('.' in value):
						temp=''.join(value.split("."))
						if(temp.isnumeric()==False):
							flagCheckNumber=False
							break
						else:
							push=float(value)
							ListToStoreValues.append(-push)
					else:
						if(value.isnumeric()==False):
							flagCheckNumber=False
							break
						else:
							push=int(value)
							ListToStoreValues.append(-push)
				else:
					if('.' in value):
						temp=''.join(value.split("."))
						if(temp.isnumeric()==False):
							flagCheckNumber=False
							break
						else:
							push=float(value)
							ListToStoreValues.append(push)
					else:
						if(value.isnumeric()==False):
							flagCheckNumber=False
							break
						else:
							push=int(value)
							ListToStoreValues.append(push)

		if flagCheckNumber:
			KPIHeaders.append(column)
			Df[column]=ListToStoreValues
		else: 
			NonKPIHeaders.append(column)
	selectedKPI['values']= KPIHeaders
	for i in range(len(NonKPIHeaders)):
		original_name=NonKPIHeaders[i]
		modified = '_'.join(NonKPIHeaders[i].split(" "))
		NonKPIHeaders[i]= modified.upper()
		Df.rename(columns = {original_name:NonKPIHeaders[i]}, inplace = True)
	if "CELL" not in NonKPIHeaders:
		selectedCell['values']= ["CELL is Not Present in CSV"]
	else:
		global ListOfCells
		ListOfCells=list(set(Df['CELL'].tolist()))
		cnt=0
		for i in ListOfCells:
			x=CellState[cnt]
			selectedCell2.menu.add_checkbutton(label=i,variable = x)
			cnt+=1
		selectedCell['values']=ListOfCells
	selectedSite['values']= list(set(Df['SITE'].tolist()))
def plot():
	KPI=chosenKpi.get()
	GRAPH=Graphchosen.get()
	for i in range(len(ListOfCells)):
		if( CellState[i].get()==1):
			CELL= ListOfCells[i]
			DF=Df.loc[(Df["CELL"]==CELL)]
			DF.plot(kind=GRAPH,x="PERIOD_START_TIME",y=KPI) 
			plt.legend([CELL,KPI],loc='upper left')
			plt.ylabel(KPI)
	plt.show()
	# Site=Sitechosen.get()
	# if(Site!=""):
	# 	DF=Df.loc[(Df["SITE"]==Site)]
	# 	DF.plot(kind=GRAPH,x="PERIOD_START_TIME",y=KPI)
	# 	plt.show()
	# else:
	# 	DF=Df.loc[(Df["CELL"]==CELL)]
	# 	DF.plot(kind=GRAPH,x="PERIOD_START_TIME",y=KPI) 
	# 	plt.legend([CELL,KPI],loc='upper left')
	# 	plt.ylabel(KPI)
	# 	plt.show()
	chosenKpi.set("")
	chosenCell.set("")
	Graphchosen.set("")
	Sitechosen.set("")

window.title('File Explorer')
window.geometry("500x500")
window.config(background = "white")
label_file_explorer = Label(window,text = "Upload your CSV ",width = 100, height = 4,fg = "blue")	
button_explore = Button(window,text = "Browse Files",command = browseFiles)
button_plot=Button(window,text="plot",command=plot)
label_file_explorer.grid(column = 1, row = 1)
button_explore.grid(column = 1, row =2)
ttk.Label(window, text = "KPI PERFORMANCE MONITORING TOOL",
		background = 'green', foreground ="white",
		font = ("Times New Roman", 15)).grid(row = 0, column = 1)
ttk.Label(window, text = "Select The KPI for which you want to plot:",
		font = ("Times New Roman", 10)).grid(column = 0,
		row = 7, padx = 10, pady = 25)
ttk.Label(window, text = "Select The CELL for which you want to plot:",
		font = ("Times New Roman", 10)).grid(column = 0,
		row = 6, padx = 10, pady = 25)
selectedCell = ttk.Combobox(window, width = 27, textvariable = chosenCell)
selectedCell2 = Menubutton (window,text="CheckComboBox", relief=RAISED,direction=RIGHT)
selectedCell2.menu= Menu(selectedCell2,tearoff=0)
selectedCell2["menu"]= selectedCell2.menu
selectedCell['values'] = ['Upload Your CSV First']
selectedCell.grid(column = 1, row = 6)
ttk.Label(window, text = "Select The Site for which you want to plot:",
		font = ("Times New Roman", 10)).grid(column = 0,
		row = 5, padx = 10, pady = 25)
selectedSite = ttk.Combobox(window, width = 27, textvariable = Sitechosen)
selectedSite['values'] = ['Upload Your CSV First']
selectedSite.grid(column = 1, row = 5)

ttk.Label(window, text = "Select The Graph for which you want to plot:",
		font = ("Times New Roman", 10)).grid(column = 0,
		row = 8, padx = 10, pady = 25)


Graphchosen=StringVar()
selectedGraph = ttk.Combobox(window, width = 27, textvariable = Graphchosen)
selectedGraph['values'] = ('bar','line','scatter')
selectedKPI = ttk.Combobox(window, width = 27, textvariable = chosenKpi)
selectedKPI['values'] = ['Upload Your CSV First']
selectedSite.grid(column   = 1, row = 5)
selectedCell.grid(column  = 1, row=6)
selectedCell2.grid(column =1,row =  10)
selectedKPI.grid(column = 1, row=7)
selectedGraph.grid(column  = 1, row=8)

window.mainloop()




