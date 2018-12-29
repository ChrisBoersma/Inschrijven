from tkinter import *
import tkinter.simpledialog
import tkinter.messagebox

root = Tk()

root.title("Inschrijven practicum")

w = 800
h = 400
sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()

x = (sw/2) - (w/2)
y = (sh/2) - (h/2)

root.geometry("%dx%d+%d+%d" % (w, h, x, y))

w = Label(root, text="My Program")


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
	
	output = "Inschrijving:"
	output += "\n" + dag
	output += "\n" + datum
	output += "\n" + uur + " Uur"
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

	tkinter.messagebox.showinfo("Inschrijving", output)

button_1 = Button(root, text="Inschrijven")
button_1.bind("<Button-1>", getInfo)
button_1.pack(pady=h/3)
#quitButton = Button(root, text="Quit", command=root.quit)
#quitButton.pack(side=LEFT)


root.mainloop()
