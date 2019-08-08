from nltk.corpus import wordnet
from tkinter import Tk,Label,Entry,Text,END,Button

root=Tk()
root.title("Dictionary") 
root.geometry('1000x800')
root.configure(bg="orange")
label1 = Label(root, text="Search",font="Helvetica 20 bold",bg="orange")
E1 = Entry(root, bd =5,font="gotham",bg="white")

def code():
    word=E1.get()
    syn = wordnet.synsets(word)
    T = Text(root,height=9, width=500,bd=5,font="gotham",bg="white")
    T.pack(side="bottom",expand=True)
    try:
        for i in range(1,101):
            T.insert(END,str(i)+")"+str(syn[i].definition()).capitalize()+"\n")
            
    except IndexError:
        T.insert(END,"Sorry!!! No more meanings available")
submit = Button(root, text ="Submit", command = code,font="gotham",bg="orange",bd=5,relief="raised")
label1.pack()
E1.pack()

submit.pack()
root.mainloop()