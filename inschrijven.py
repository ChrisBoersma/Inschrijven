from tkinter import *
from openpyxl import *
import tkinter.simpledialog
import tkinter.messagebox

#loads the excel sheet
wb2 = load_workbook('test.xlsx')
#print (wb2.sheetnames)
ws = wb2.active

#loads the page
root = Tk()
root.title("Inschrijven practicum")

#initializes page height and width
w = 800
h = 400
sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()
x = (sw/2) - (w/2)
y = (sh/2) - (h/2)
root.geometry("%dx%d+%d+%d" % (w, h, x, y))


#function when clikcing the button
def getInfo(event):
	tNaam2 = ""
	aNaam2 = ""
	klas2 = ""
	dag = tkinter.simpledialog.askstring("dag", "Welke dag?")
	datum = tkinter.simpledialog.askstring("datum", "Welke datum?")
	uur = tkinter.simpledialog.askstring("uur", "Welk uur?")
	vNaam1 = tkinter.simpledialog.askstring("voornaam1", "Voornaam van leerling 1?")
	tNaam1 = tkinter.simpledialog.askstring("tussenvoegsel1", "Tussenvoegsel van leerling1?")
	aNaam1 = tkinter.simpledialog.askstring("achternaam1", "Achternaam van leerling 1?")
	klas1 = tkinter.simpledialog.askstring("klas1", "Klas van leerling1?")
	vNaam2 = tkinter.simpledialog.askstring("voornaam2", "Voornaam van leerling 2?")
	if(vNaam2):
		tNaam2 = tkinter.simpledialog.askstring("tussenvoegsel2", "Tussenvoegsel van leerling2?")
		aNaam2 = tkinter.simpledialog.askstring("achternaam2", "Achternaam van leerling2")
		klas2 = tkinter.simpledialog.askstring("klas2", "Klas van leerling2?")
	proefnr = tkinter.simpledialog.askstring("proefnummer", "Proefnummer?")
	titel = tkinter.simpledialog.askstring("titel", "Titel van de proef?")
	vak = tkinter.simpledialog.askstring("vak", "Voor welk vak?")
	
	#creates output
	output = "Inschrijving:"
	output += "\n" + dag
	output += "\n" + datum
	output += "\n" + uur + " uur"
	output += "\n" + vNaam1
	if(tNaam1):
		output += " " + tNaam1
	output += " " + aNaam1
	output += "\n" + klas1
	if(vNaam2):
		output += "\n" + vNaam2
	if(tNaam2):
		output += " " + tNaam2
	if(aNaam2):
		output += " " + aNaam2
	if(klas2):
		output += "\n" + klas2
	output += "\nProef:"
	output += "\n" + proefnr
	output += "\n" + titel
	output += "\n" + vak
	
	#puts output in excel
	ws.append([dag, datum, uur, vNaam1, tNaam1, aNaam1, klas1, proefnr, titel, vak])
	ws.append([dag, datum, uur, vNaam2, tNaam2, aNaam2, klas2, proefnr, titel, vak])
	wb2.save("test.xlsx")
	
	
	#shows output message on screen
	tkinter.messagebox.showinfo("Inschrijving", output)


#creates button
button_1 = Button(root, text="Inschrijven")
button_1.bind("<Button-1>", getInfo)
button_1.pack(pady=h/3)
#quitButton = Button(root, text="Quit", command=root.quit)
#quitButton.pack(side=LEFT)


root.mainloop()

