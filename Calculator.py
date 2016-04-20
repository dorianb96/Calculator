from tkinter import *
# root = TK() inicijalizira novi prozor
# root je  glavni prozor za sve tkinter widgete
root = Tk()
# ovo postavalja prozor za +300 i +150 piksela
root.geometry("+300+150")

#title od prozora moramo postaviti kao kalkulator
root.wm_title("Kalkulator")
# ovo kaze da se nemoze micati vecina kalkulatora
root.resizable(width=FALSE, height=FALSE)


# display je objekt StringVar() klase
# koristi se za Entry klasu koja moze primati StringVar() i prikazivati ga
# moze pretvoriti matematicke izraze koji su dodani kao string u stvaran racun
# naprimjer "4 * 8" ce pretvoriti u pravi matematicki izraz
# to pretvara pomocu naredbe evaluate()
display = StringVar()


# rezultati je Entry widget koji prikazuje rezultat
# text mora biti StringVar() pa zato i koristimo varijablu display
#font moramo postaviti da se bolje vidi
rezultati = Entry(root,font = "Helvetica 15 bold", text=display)
#ipday ce produziti entry widget na 10 redova
rezultati.pack(fill = X, ipady = 10)


# fill = x znaci da ce prozor ispunit cijelu x os u tom redu
# kada konstruiramo prozor1 on je widget tipa Frame
# pri inicijaliziranju mu treba poslati koji okvir mu je  "vlasnik"
prozor1 = Frame(root)
# pack layout manager dodaje u novi red
prozor1.pack(fill=X)

#moramo dodati svih 4 prozora
prozor2 = Frame(root)
prozor2.pack(fill=X)

prozor3 = Frame(root)
prozor3.pack(fill=X)

prozor4 = Frame(root)
prozor4.pack(fill=X)



# prvo prozor jedan treba napuniti a to je prvi red
# lambda je kratkorocna funkcija koja ce obaviti tocno tu radnju kada netko stisne gumb
button = Button(prozor1, text = "1", font = 25, width =5, height = 2, command = lambda: display.set(display.get() + '1'))
# button.pack dodaje button u prozor1 ali skroz lijevo jer pazimo da ne prijede u drugi red
# zato dajemo kljucni argument side=LEFT
button.pack(side=LEFT)

#postavili smo i visinu i sirinu programa
#width znaci koji broj redaka je jedna tipka
button = Button(prozor1, text = "2", font = 25, width =5, height = 2, command = lambda: display.set(display.get() + '2'))
button.pack(side=LEFT)

# command = lambda: display.set(display.get() + '3'))
# taj command je ono sto se dogodi nakon sto stisnemo gumb
# onda program uzima string iz StringVar() display i postavlja novu vrijednost sa display.get()
button = Button(prozor1, text = "3", font = 25, width =5, height = 2, command = lambda: display.set(display.get() + '3'))
button.pack(side=LEFT)

button = Button(prozor1, text = "CL", font = 25, width =5, height = 2, command = lambda: display.set(''))
button.pack(side=LEFT)

button = Button(prozor1, text = ".", font = 25, width =5, height = 2, command = lambda: display.set(display.get() + '.'))
button.pack(side=LEFT)




# drugi prozor je drugi red kalkulatora
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

# trcci prozor je treci red kalkulatora
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

# cetvrti prozor je cetvrti red kalkulatora
button = Button(prozor4, text = "0", font = 25, width =5, height = 2, command = lambda: display.set(display.get() + '0'))
button.pack(side = LEFT)

button = Button(prozor4, text = "(", font = 25, width =5, height = 2, command = lambda: display.set(display.get() + '('))
button.pack(side = LEFT)

button = Button(prozor4, text = ")", font = 25, width =5, height = 2, command = lambda: display.set(display.get() + ')'))
button.pack(side = LEFT)

button = Button(prozor4, text = "//", font = 25, width =5, height = 2, command = lambda: display.set(display.get() + "//"))
button.pack(side = LEFT)

# ovo je kljucna funkcija eval
# ona pretvara ekspresiju StringVar() u matematicki format i rjesava ju
# jako vazna za kalkuliranje jer Entry widget drzi informacije racuna koje smo proveli
button = Button(prozor4, text = "=", font = 25, width =5, height = 2, command = lambda: display.set(eval(display.get())))
button.pack(side = LEFT)


# root.mainloop koristimo kako se program nebi ugasio odma nakon pokretanja
# pokrece program
root.mainloop()











