from tkinter import *

window = Tk()

p = Label(bg="pink", width=40, height=5)
p.grid(row=0, column=0)

b = Label(bg="blue", width=40, height=5)
b.grid(row=1, column=0)

y = Label(bg="yellow", width=40, height=5)
y.grid(row=2, column=0)

g = Label(bg="green", width=40, height=5)
g.grid(row=3, column=0)

r = Label(bg="red", width=40, height=5)
r.grid(row=4, column=0)

m = Label(bg="maroon", width=40, height=5)
m.grid(row=5, column=0)

be = Label(bg="beige", width=40, height=5)
be.grid(row=6, column=0)

p = Label(bg="pink", width=40, height=5)
p.grid(row=6, column=1)

b = Label(bg="blue", width=40, height=5)
b.grid(row=5, column=1)

y = Label(bg="yellow", width=40, height=5)
y.grid(row=4, column=1)

w = Label(bg="white", width=40, height=5)
w.grid(row=3, column=1)

r = Label(bg="red", width=40, height=5)
r.grid(row=2, column=1)

m = Label(bg="maroon", width=40, height=5)
m.grid(row=1, column=1)

be = Label(bg="beige", width=40, height=5)
be.grid(row=0, column=1)

window.mainloop()
