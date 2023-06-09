# Ketvirta užduotis - Tkinter
#
# Sukurti programą su TKinter. Programa turi turėti:
# Laukelį, į kurį įvedama temperatūrą
# Mygtuką, kurį paspaudus į laukelį įrašyta temperatūrą būtų konvertuojama iš farenheito į celsijų.
# Konvertuota temperatūra turi būti atvaizduota programoje kaip tekstas.
# Mygtuką, kurį paspaudus į laukelį įrašyta temperatūrą būtų konvertuojama iš celsijaus į farenhaitą.
# Konvertuota temperatūra turi būti atvaizduota programoje kaip tekstas.
# Tekstą, kuris atvaizduos temperatūros konvertavimo rezultatą

from tkinter import *


def farenheit_celsius():
    farenheit = float(e.get())
    celsius = (farenheit - 32) * 5 / 9
    result_label.config(text="{:.1f}".format(celsius))     #grazina rezultata kad parodytu pagrindineme lange, ir palieka 1 skaiciu po kablelio

def celsius_farenheit():
    celsius = float(e.get())
    farenheit = celsius * 9 / 5 + 32
    result_label.config(text="{:.1f}".format(farenheit))      #grazina rezultata kad parodytu pagrindineme lange ir palieka viena skaiciu po kablelio

root = Tk()
root.title("Temperaturos Konvertuotojas")
e = Entry(root,width=40,borderwidth=20)
e.grid(row=0, column=0, padx=0,pady=5)


button_1 = Button(root, text="Paversti Farenheit i Celsius",command=farenheit_celsius )
button_2 = Button(root, text="Paversti Celsius i Farenheit",command=celsius_farenheit )
button_3 = Button(root, text="Exit", command=root.destroy)



button_1.grid(row=2, column=0)
button_2.grid(row=3, column=0)
button_3.grid(row=3, column=1)

result_label = Label(root, text="")
result_label.grid(row=4, column=0, pady=10)





root.mainloop()