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
window2 = Frame( root )
window2.pack( fill=X )
window3 = Frame( root )
window3.pack( fill=X )
window4 = Frame( root )
window4.pack( fill=X )

button = Button( window1, text ="1", font = 25, width =5, height = 2, command = lambda: display.set( display.get( ) + '1' ) ).pack(side=LEFT)
button = Button( window1, text ="2", font = 25, width =5, height = 2, command = lambda: display.set( display.get( ) + '2' ) ).pack(side=LEFT)
button = Button( window1, text ="3", font = 25, width =5, height = 2, command = lambda: display.set( display.get( ) + '3' ) ).pack(side=LEFT)
button = Button( window1, text ="CL", font = 25, width =5, height = 2, command = lambda: display.set( '' ) ).pack(side=LEFT)
button = Button( window1, text =".", font = 25, width =5, height = 2, command = lambda: display.set( display.get( ) + '.' ) ).pack(side=LEFT)
button = Button( window2, text ="4", font = 25, width =5, height = 2, command = lambda: display.set( display.get( ) + '4' ) ).pack( side=LEFT )
button = Button( window2, text ="5", font = 25, width =5, height = 2, command = lambda: display.set( display.get( ) + '5' ) ).pack( side=LEFT )
button = Button( window2, text ="6", font = 25, width =5, height = 2, command = lambda: display.set( display.get( ) + '6' ) ).pack( side=LEFT )
button = Button( window2, text ="*", font = 25, width =5, height = 2, command = lambda: display.set( display.get( ) + '*' ) ).pack( side=LEFT )
button = Button( window2, text ="+", font = 25, width =5, height = 2, command = lambda: display.set( display.get( ) + '+' ) ).pack( side=LEFT )
button = Button( window3, text ="7", font = 25, width =5, height = 2, command = lambda: display.set( display.get( ) + '7' ) ).pack( side=LEFT )
button = Button( window3, text ="8", font = 25, width =5, height = 2, command = lambda: display.set( display.get( ) + '8' ) ).pack( side=LEFT )
button = Button( window3, text ="9", font = 25, width =5, height = 2, command = lambda: display.set( display.get( ) + '9' ) ).pack( side=LEFT )
button = Button( window3, text ="/", font = 25, width =5, height = 2, command = lambda: display.set( display.get( ) + '/' ) ).pack( side=LEFT )
button = Button( window3, text ="-", font = 25, width =5, height = 2, command = lambda: display.set( display.get( ) + '-' ) ).pack( side=LEFT )
button = Button( window4, text ="0", font = 25, width =5, height = 2, command = lambda: display.set( display.get( ) + '0' ) ).pack( side=LEFT )
button = Button( window4, text ="(", font = 25, width =5, height = 2, command = lambda: display.set( display.get( ) + '(' ) ).pack( side=LEFT )
button = Button( window4, text =")", font = 25, width =5, height = 2, command = lambda: display.set( display.get( ) + ')' ) ).pack( side=LEFT )
button = Button( window4, text ="//", font = 25, width =5, height = 2, command = lambda: display.set( display.get( ) + "//" ) ).pack( side=LEFT )

button = Button( window4, text ="=", font = 25, width =5, height = 2, command = lambda: display.set( eval( display.get( ) ) ) )
button.pack(side = LEFT)

root.mainloop()











