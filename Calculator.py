from tkinter import *
root = Tk()
root.geometry("+300+150")

root.wm_title("Calculator")
root.resizable(width=FALSE, height=FALSE)

display = StringVar()

result = Entry(root, font="Helvetica 15 bold", text=display)
result.pack(fill=X, ipady=10)

window1 = Frame( root )
window1.pack(fill=X)
prozor2 = Frame(root)
prozor2.pack(fill=X)
prozor3 = Frame(root)
prozor3.pack(fill=X)
prozor4 = Frame(root)
prozor4.pack(fill=X)

button = Button( window1, text ="1", font = 25, width =5, height = 2, command = lambda: display.set( display.get( ) + '1' ) )
button.pack(side=LEFT)
button = Button( window1, text ="2", font = 25, width =5, height = 2, command = lambda: display.set( display.get( ) + '2' ) )
button.pack(side=LEFT)
button = Button( window1, text ="3", font = 25, width =5, height = 2, command = lambda: display.set( display.get( ) + '3' ) )
button.pack(side=LEFT)
button = Button( window1, text ="CL", font = 25, width =5, height = 2, command = lambda: display.set( '' ) )
button.pack(side=LEFT)
button = Button( window1, text =".", font = 25, width =5, height = 2, command = lambda: display.set( display.get( ) + '.' ) )
button.pack(side=LEFT)
button = Button(prozor2, text = "4", font = 25, width =5, height = 2, command = lambda: display.set(display.get() + '4'))
button.pack(side=LEFT)
button = Button(prozor2, text = "5", font = 25, width =5, height = 2, command = lambda: display.set(display.get() + '5'))
button.pack(side=LEFT)
button = Button(prozor2, text = "6", font = 25, width =5, height = 2, command = lambda: display.set(display.get() + '6'))
button.pack(side=LEFT)
button = Button(prozor2, text = "*", font = 25, width =5, height = 2, command = lambda: display.set(display.get() + '*'))
button.pack(side=LEFT)
button = Button(prozor2, text = "+", font = 25, width =5, height = 2, command = lambda: display.set(display.get() + '+'))
button.pack(side=LEFT)
button = Button(prozor3, text = "7", font = 25, width =5, height = 2, command = lambda: display.set(display.get() + '7'))
button.pack(side=LEFT)
button = Button(prozor3, text = "8", font = 25, width =5, height = 2, command = lambda: display.set(display.get() + '8'))
button.pack(side = LEFT)
button = Button(prozor3, text = "9", font = 25, width =5, height = 2, command = lambda: display.set(display.get() + '9'))
button.pack(side = LEFT)
button = Button(prozor3, text = "/", font = 25, width =5, height = 2, command = lambda: display.set(display.get() + '/'))
button.pack(side = LEFT)
button = Button(prozor3, text = "-", font = 25, width =5, height = 2, command = lambda: display.set(display.get() + '-'))
button.pack(side = LEFT)
button = Button(prozor4, text = "0", font = 25, width =5, height = 2, command = lambda: display.set(display.get() + '0'))
button.pack(side = LEFT)
button = Button(prozor4, text = "(", font = 25, width =5, height = 2, command = lambda: display.set(display.get() + '('))
button.pack(side = LEFT)
button = Button(prozor4, text = ")", font = 25, width =5, height = 2, command = lambda: display.set(display.get() + ')'))
button.pack(side = LEFT)
button = Button(prozor4, text = "//", font = 25, width =5, height = 2, command = lambda: display.set(display.get() + "//"))
button.pack(side = LEFT)

button = Button(prozor4, text = "=", font = 25, width =5, height = 2, command = lambda: display.set(eval(display.get())))
button.pack(side = LEFT)

root.mainloop()











