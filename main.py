import MySQLdb
from tkinter import*
#куку
conn = MySQLdb.connect('141.8.193.236', 'f0549337_123', '9514753', 'f0549337_123')
cursor = conn.cursor()
# cursor.execute("SELECT * FROM Trata")
# row = cursor.fetchone()
# print(row)
# rows = cursor.fetchall()
# for row in rows:
#     print(row)

def Quit(EV):
    #conn.close()
    global root
    root.destroy()


def produkt(ev):
    textbox.delete('1.0', 'end')
    sql = "SELECT name, price FROM Trata WHERE date >= ? and date <= ?"
    cursor.execute(sql, [(datas_entry.get()), (datapo_entry.get())])
    results = cursor.fetchall()
    textbox.insert(1.0, results)
    textbox.insert(2.0, 'Расходы составили: ')
    sql = "SELECT SUM(price) FROM Trata WHERE date >= ? and date <= ?"
    cursor.execute(sql, [(datas_entry.get()), (datapo_entry.get())])
    results = cursor.fetchall()
    textbox.insert(3.0, results)
    textbox.insert(4.0, ' рублей.')


def Clearee(ev):
    textbox.delete('1.0', 'end')


def Dobavsql(ev):
    sql = '''INSERT INTO Trata(name, date, tipe, price) VALUES (?, ?, ?, ?)'''
    cursor.execute(sql, (name_entry.get(), datte_entry.get(), tippe_entry.get(), tratta_entry.get()))
    conn.commit()


def zapoln(ev):
    textbox.delete('1.0', 'end')
    # cursor.execute("SELECT * FROM Trata")
    # results = cursor.fetchall()
    # textbox.insert(1.0, results)
    cursorObj = conn.cursor()
    cursorObj.execute('SELECT * FROM Trata')
    rows = cursorObj.fetchall()
    for row in rows:
        textbox.insert(1.0, row)
        textbox.insert(1.0, '\n')


# def LoadFile(ev):
#     fn = tkFileDialog.Open(root, filetypes=[('*.txt files', '.txt')]).show()
#     if fn == '':
#         return
#     textbox.delete('1.0', 'end')
#     textbox.insert('1.0', open(fn, 'rt').read())
#
#
# def SaveFile(ev):
#     fn = tkFileDialog.SaveAs(root, filetypes=[('*.txt files', '.txt')]).show()
#     if fn == '':
#         return
#     if not fn.endswith(".txt"):
#         fn += ".txt"
#     open(fn, 'wt').write(textbox.get('1.0', 'end'))


root = Tk()

panelFrame = Frame(root, height=170, bg='GREY')
textFrame = Frame(root, height=340, width=600)

panelFrame.pack(side='top', fill='x')
textFrame.pack(side='bottom', fill='both', expand=1)

textbox = Text(textFrame, font='Arial 14', wrap='word')
scrollbar = Scrollbar(textFrame)

scrollbar['command'] = textbox.yview
textbox['yscrollcommand'] = scrollbar.set

textbox.pack(side='left', fill='both', expand=1)
scrollbar.pack(side='right', fill='y')

zapolnBtn = Button(panelFrame, text='Показать всё')
clearbtn = Button(panelFrame, text='Очистить')
quitBtn = Button(panelFrame, text='Выход')
dobavbtn = Button(panelFrame, text='Добавить')
produktbtn = Button(panelFrame, text='Расоды C - ПО')

zapolnBtn.bind("<Button-1>", zapoln)
clearbtn.bind("<Button-1>", Clearee)
quitBtn.bind("<Button-1>", Quit)
dobavbtn.bind("<Button-1>", Dobavsql)
produktbtn.bind("<Button-1>", produkt)

zapolnBtn.place(x=10, y=10, width=140, height=40)
clearbtn.place(x=160, y=10, width=140, height=40)
produktbtn.place(x=310, y=10, width=140, height=40)
quitBtn.place(x=760, y=10, width=140, height=40)
dobavbtn.place(x=610, y=110, width=140, height=40)

name = StringVar()
datte = StringVar()
tippe = StringVar()
tratta = StringVar()
datas = StringVar()
datapo = StringVar()

name_label = Label(text="Название:")
datte_label = Label(text="Дата:")
tippe_label = Label(text="Тип:")
tratta_label = Label(text="Затраты:")

name_label.place(x=10, y=60, width=140, height=40)
datte_label.place(x=160, y=60, width=140, height=40)
tippe_label.place(x=310, y=60, width=140, height=40)
tratta_label.place(x=460, y=60, width=140, height=40)

name_entry = Entry(textvariable=name)
datte_entry = Entry(textvariable=datte)
tippe_entry = Entry(textvariable=tippe)
tratta_entry = Entry(textvariable=tratta)
datas_entry = Entry(textvariable=datas)
datapo_entry = Entry(textvariable=datapo)

name_entry.place(x=10, y=110, width=140, height=40)
datte_entry.place(x=160, y=110, width=140, height=40)
tippe_entry.place(x=310, y=110, width=140, height=40)
tratta_entry.place(x=460, y=110, width=140, height=40)
datas_entry.place(x=460, y=10, width=140, height=40)
datapo_entry.place(x=610, y=10, width=140, height=40)

root.mainloop()

conn.close()