from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title("MBTA Route App")
root.geometry('400x300')

station_data = []
variable = StringVar()


# TODO: trying to get this to work for selecting
#  the stations but it's not necessary in the end
def save_data(data):
    global station_data
    station_data = data
    print(station_data)


def display_selected(choice):
    self = variable.get()
    print(choice)


# creating widget
dropdown = OptionMenu(
    root,
    variable,
    *station_data,
    command=display_selected
)

# positioning widget
dropdown.config(width=25)
dropdown.pack(expand=True)

# infinite loop
root.mainloop()
