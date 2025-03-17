import tkinter as tk

root = tk.Tk()


# this is my window script
root.title("joshuakingstech.com")
root.configure(background="blue")
root.minsize(2000, 2000)
root.maxsize(2000, 2000)

tk.Label(root, text="this is joshuas app!").pack()
tk.Label(root, text="and joshua is cool").pack()
tk.Label(root, text="and joshua coded this and tottally did not use tutorials").pack()
tk.Label(root, text="no but atually this took so long!").pack()
tk.Label(root, text="so i will update tomorrow :)").pack()
tk.Label(root, text="also visit joshuaking.icu and joshuakingstech.com bye!").pack()


root.mainloop()

print ("Opened Program!")