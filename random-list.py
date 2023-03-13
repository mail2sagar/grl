from tkinter import *
import random

window = Tk()

window.title("Generate Random List")
window.geometry("500x500")

def random_li():
    r1 = random.randint(0,25)
    r2 = random.randint(0,25)
    r3 = random.randint(0,25)
    r4 = random.randint(0,25)
    r5 = random.randint(0,25)
    r6 = random.randint(0,25)
    r7 = random.randint(0,25)
    r8 = random.randint(0,25)
    r9 = random.randint(0,25)
    r10 = random.randint(0,25)
    r11 = random.randint(0,25)
    r12 = random.randint(0,25)
    r13 = random.randint(0,25)
    r14 = random.randint(0,25)
    r15 = random.randint(0,25)
    r16 = random.randint(0,25)
    r17 = random.randint(0,25)
    r18 = random.randint(0,25)
    r19 = random.randint(0,25)
    r20 = random.randint(0,25)
    r21 = random.randint(0,25)
    r22 = random.randint(0,25)
    r23 = random.randint(0,25)
    r24 = random.randint(0,25)
    r25 = random.randint(0,25)
    r26 = random.randint(0,25)
    print(list[r1],[r2],[r3],[r4],[r5],[r6],[r7][r8],[r9],[r10],[r11],[r12],[r13],[r14],[r15],[r16],[r17],[r18],[r19],[r20],[r21],[r22],[r23],[r24],[r25],[r26])

button = Button(window,text="Generate Random List")
label = Label(window)
button.place(relx=0.5,rely=0.4,anchor=CENTER)
label.place(relx=0.5,rely=0.3,anchor=CENTER)


window.mainloop()