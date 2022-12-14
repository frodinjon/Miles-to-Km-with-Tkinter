from tkinter import *

window = Tk()

window.title("My First GUI Program")
window.minsize(width=500, height=500)

#Label
my_label = Label(text="Label test", font=("Arial", 24))
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="New Text 2")

def button_press():
	text = input.get()
	my_label.config(text=text)
	
#Buton
button = Button(text="Click Me",command=button_press)
button.pack()

#Entry
input = Entry(width=40)
input.pack()

#Text
text = Text(height=5, width=30)
text.focus()
text.insert(END, "Example of multi-line text entry.")
print(text.get("1.0", END))
text.pack()

#Spinbox
def spinbox_used():
	print(spinbox.get())

spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

def scale_used(value):
	print(value)


scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

#checkbox
def checkbox_used():
	print(checked_state.get())

checked_state = IntVar()
checkbox = Checkbutton(text="Is On?", variable=checked_state, command=checkbox_used)
checked_state.get()
checkbox.pack()

#Radiobutton
def radio_used():
	print(radio_state.get())

radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1",value=1,variable=radio_state,command=radio_used)
radiobutton2 = Radiobutton(text="Option2",value=2,variable=radio_state,command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


#Listbox
def listbox_used(event):
	print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
	listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used,)
listbox.pack()



window.mainloop()