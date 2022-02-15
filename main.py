from tkinter import *


def miles_to_km():
    miles = float(input.get())
    km = miles*1.609
    result.config(text=f"{km}")


window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=50, pady=50)

miles_label = Label(text="Miles", font=("Ariel", 10))
miles_label.grid(row=0, column=2)

equal_to = Label(text="is equal to", font=("Ariel", 10))
equal_to.grid(row=1, column=0)

km_label = Label(text="Km", font=("Ariel", 10))
km_label.grid(row=1, column=2)

result = Label(text="0", font=("Ariel", 10))
result.grid(row=1, column=1)

button = Button(text="Calculate", command=miles_to_km)
button.grid(row=2, column=1)

input = Entry(width=10)
input.grid(row=0, column=1)


window.mainloop()
