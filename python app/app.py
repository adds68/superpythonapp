from tkinter import *
from tkinter import messagebox
root = Tk()


# this is my window script
root.title("joshuakingstech.com")
root.configure(background="red")
root.minsize(2000, 2000)
root.maxsize(2000, 2000)

Label(root, text="this is joshuas app!").pack()
Label(root, text="and joshua is cool").pack()
Label(root, text="and joshua coded this and tottally did not use tutorials").pack()
Label(root, text="no but atually this took so long!").pack()
Label(root, text="so i will update tomorrow :)").pack()
Label(root, text="also visit joshuaking.icu and joshuakingstech.com bye!").pack()

def helloCallBack():
   msg=messagebox.showinfo( "Hello Python", "Josh smells like a big fat fart head")

B = Button(root, text ="Hello Button Josh", command = helloCallBack)
B.place(x=50,y=50)


root.mainloop()

print ("Opened Program!")
