from tkinter import *
FONT = ("Arial", 14)
window = Tk()

window.title("Miles to Km Converter")
window.minsize(width=100, height=100)
window.config(padx=20, pady=20)

#Labels
equal_label = Label(text="is equal to", font=FONT)
equal_label.grid(column=0,row=1)
equal_label.config(padx=5, pady=5)
miles_label = Label(text="Miles", font=FONT)
miles_label.grid(column=2,row=0)
miles_label.config(padx=5, pady=5)
km_label = Label(text="Km", font=FONT)
km_label.grid(column=2, row=1)
km_label.config(padx=5, pady=5)
result_label = Label(text="0", font=FONT)
result_label.grid(column=1, row=1)
result_label.config(padx=5, pady=5)

#Buton
def button_press():
	miles = int(input.get())
	km = miles * 1.609344
	result_label.config(text=str(round(km)))
	
button = Button(text="Calculate",command=button_press)
button.grid(column=1, row=2)
button.config(padx=5, pady=5)


#Entry
input = Entry(width=10)
input.grid(column=1, row=0)


window.mainloop()