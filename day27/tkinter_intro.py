import tkinter

window = tkinter.Tk()

window.title("Hello World")
window.minsize(height= 300, width=500)

my_label = tkinter.Label(text="Welcome to tkinter" , font=('Arial' , 24 , 'italic'))
my_label.pack()

window.mainloop()