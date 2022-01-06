from tkinter import*
klik=0 #прога считает клики и должна увеличивать число нажатий от нажатий
def klikker(event):
    global klik
    klik+=1
    lbl.configure(text=klik)
    #aken.winfo_width()+10 #увеличить ширину
    #aken.winfo_height()+10 #увеличить высоту
    #aken.winfo_width()-10 #уменьшить ширину
    #aken.winfo_height()-10 #уменьшить высоту
    aken.geometry(str(aken.winfo_width()+10)+"x"+str(aken.winfo_height()+10))
def klikker_minus(event):
    global klik
    if klik==-10:
        klik=0
    klik-=1
    lbl.configure(text=klik)
def txt_to_lbl(event):
    #pass 
    text_to_lbl=txt.get() #взяли из текста from Entry and paste из 24 строчки
    lbl.configure(text=text_to_lbl)
    txt.delete(0,END) #координаты
def valik():
    valik_=var.get() #считываем инф
    lbl.configure(txt=valik_)
    txt.insert(0,valik_) #на какой позиции стоит
def vqhod(event):
    aken.destroy()

aken=Tk() #создаем окно
aken.title("Akna nimetus") #метод заголовок, обязательно в скобках св-ва, если постянно неизменный текст - "", если переменная - просто без ковычек
aken.geometry("400x300") #размер окна
nupp=Button(aken,text="Mina olen nupp\nVajuta mind!",font="Arial 20",fg="red",bg="Lightblue", height=4,width=20,relief=GROOVE) #сначала - где хотим видеть кнопку, потом текст, щрифт и его размер, fg - цвет, bg - форма, высота, ширина, рельеф: RAISED, SUNKEN
nupp.bind("<Button-1>",klikker) #запуск функции (какое/ие событие/я, кго название(функция))
nupp.bind("<Button-3>",klikker_minus)
lbl=Label(aken,text="...",height=4,width=20,font="Arial 20",fg="green",bg="Lightblue")
txt=Entry(aken,width=20,font="Arial 20",fg="pink",bg="Lightblue",justify=CENTER) #выравнивание текста по центру (автом. он по левому краю)
txt.bind("<Return>",txt_to_lbl) #Enter
i1=PhotoImage(file="1.png")
i2=PhotoImage(file="2.png")
i3=PhotoImage(file="3.png")
varStringVar()
var.set("Üks")
r1=Radiobutton(aken,image=i1,variable=var,value="Üks",command=valik)
r2=Radiobutton(aken,image=i2,variable=var,value="Kaks",command=valik)
r3=Radiobutton(aken,image=i3,variable=var,value="Kolm",command=valik)

lbl.pack()
nupp.pack() #...(side=LEFT/TOP/RIGHT) 
txt.pack()
r1.pack()
r2.pack()
r3.pack()
aken.mainloop() #запуск окна

#problema s kartinkami

