import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
import pgeocode
from tkinter import messagebox
import pandas as pd
import pgeocode_data


#root config
root = tk.Tk()
root.title('postc 1.0')
root.wm_iconbitmap('C:\\Users\\user\\Desktop\\PYTHON\\postc1.0\\postc1.0.ico')
root.minsize(1000,900)
HEIGHT = 900
WIDTH = 1000

root.withdraw()
root.update_idletasks()  

x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 5
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 35
root.geometry("+%d+%d" % (x, y))

root.deiconify()


#menubar config

def file_saveas():
    f = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Documents","*.txt")])
    fileobj = open(f, 'a')
    fileobj.writelines(str(kod()))
    fileobj.close()
    messagebox.showinfo('', 'File saved')

def file_saveas2():
    g = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Documents","*.txt")])
    fileobj2 = open(g, 'a')
    fileobj2.writelines(str(label8['text']))
    fileobj2.close()
    messagebox.showinfo('', 'File saved')

def Help():
    messagebox.showinfo('Help', '...in preparation...')


def About():
    messagebox.showinfo('About...', 'All rights reserved (2020). The following postc 1.0v1 software returns information \
about the area named by postal code/zip code in Poland. It is prepared by Maksymilian Twyrdy using Python 3.8.1 coding \
environment and free-to-use online packages. The program is dedicated to Windows systems (tested on WinXP to Win7 systems). \
The database used contains one zip file taken from the GeoNames.org database (freeware). \
If any problems/errors received, please contact maxt026@op.pl.') 


menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label='New', command=open('C:\\Users\\user\\Desktop\\PYTHON\\postc1.0\postc1.0.exe'))
filemenu.add_command(label='Save as (mode1)', command=file_saveas)
filemenu.add_command(label='Save as (mode2)', command=file_saveas2)

filemenu. add_separator()

filemenu.add_command(label='Exit', command=root.destroy)
menubar.add_cascade(label='File', menu=filemenu)
editmenu = Menu(menubar, tearoff=0)

editmenu.add_separator()

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label='Help', command=Help)
helpmenu.add_cascade(label='About...', command=About)
menubar.add_cascade(label='Help', menu=helpmenu)

root.config(menu=menubar)

#end of menu config

tabControl = ttk.Notebook()
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text = 'Mode 1')

tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text = 'Mode 2')

tabControl.pack(expan = 1, fill = 'both')



#  tab1 config  #

canvas = tk.Canvas(tab1, height=HEIGHT, width=WIDTH)
canvas.pack()

sec_frame = tk.Frame(tab1, bg='#80c1ff', bd=2)
sec_frame.place(relx=0.5, rely=0.25, relwidth=0.8, relheight=0.05, anchor='n')

lower_frame = tk.Frame(tab1, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.4, relwidth=0.8, relheight=0.55, anchor='n')

#end of frame building

#upmost frame config

label = tk.Label(tab1, text='In this mode the program shows \
information about the area named by postal code in Poland.', font = 20, wraplength=500)
label.place(relx=0.15, rely=0.1, relwidth=0.75, relheight=0.1)

entry = tk.Entry(sec_frame, bg='#64DF73', font=14, width='6')
entry.pack(side='right')

label3 = tk.Label(sec_frame, text='Enter postal code you want to search (use format XX-XXX):', font=14, bg='#80c1ff')
label3.pack(side='left')

label4 = tk.Label(lower_frame, text="", bg='#80c1ff', font=('Courier 14 bold'))
label4.pack(side='left')

###

    
def kod():
    nomi = pgeocode.Nominatim('PL')
    output = nomi.query_postal_code(entry.get())
    if (int(len(entry.get())!=6)):
        messagebox.showwarning('', 'Wrong input lenght, please correct it.')
    else:
        label4.config(text=output[:-1])
        return output[:-1]


button2 = tk.Button(tab1, text='GO!', command = kod)
button2.place(relx=0.43, rely=0.32, relwidth=0.2, relheight=0.05)

# end of tab1 #

#tab2 config#

canvas2 = tk.Canvas(tab2, height=HEIGHT, width=WIDTH)
canvas2.pack()

label5 = tk.Label(tab2, text='In this mode the program shows \
information about the distance between two areas selected by postal code in Poland.', font = 20, wraplength=500)
label5.place(relx=0.15, rely=0.01, relwidth=0.75, relheight=0.1)

upmost_frame2 = tk.Frame(tab2, bg='#A7FB98', bd=2)
upmost_frame2.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.05, anchor='n')

middle_frame2 = tk.Frame(tab2, bg='#A7FB98', bd=2)
middle_frame2.place(relx=0.5, rely=0.2, relwidth=0.75, relheight=0.05, anchor='n')
                   
lower_frame2 = tk.Frame(tab2, bg='#A7FB98', bd=2)
lower_frame2.place(relx=0.5, rely=0.32, relwidth=0.9, relheight=0.65, anchor='n')

label6 = tk.Label(upmost_frame2, text='Enter the first postal code (use XX-XXX format): ', font=20, bg = '#A7FB98')
label6.pack(side='left')

entry2 = tk.Entry(upmost_frame2, bg='#80c1ff', font=14, width='6')
entry2.pack(side='right')

label7 = tk.Label(middle_frame2, text='Enter the second postal code (use XX-XXX format): ', font=20, bg = '#A7FB98')
label7.pack(side='left')

entry3 = tk.Entry(middle_frame2, bg='#80c1ff', font=14, width='6')
entry3.pack(side='right')

label8 = tk.Label(lower_frame2, text="", bg='#A7FB98', font=('Courier', 9))
label8.place(relheight=1, relwidth=1)

pd.set_option('display.max_columns', 900)      #removes squeeze for columns
pd.set_option('display.max_rows', 700)

def dist():
    dist = pgeocode.GeoDistance('PL')
    nomi = pgeocode.Nominatim('PL')
    output3 = nomi.query_postal_code(entry2.get())
    output4 = nomi.query_postal_code(entry3.get())
    output2 = dist.query_postal_code(str(entry2.get()), str(entry3.get()))
    if ((int(len(entry2.get())!=6)) or (int(len(entry3.get())!=6))):
        messagebox.showwarning('', 'Wrong input lenght, please correct it.')
    else:
        label8.config(font=('Courier 13 bold'), text= str(output3[:-1]) + ('\n') + str(output4[:-1]) + ('\n') + ('\n') + 'The distance between these areas is ~' + str(round(output2, 2)) + ' km')
    return output2, output3[:-1], output4[:-1]
   
 
    
button3 = tk.Button(tab2, text='GO!', command = dist)
button3.place(relx=0.43, rely=0.26, relwidth=0.2, relheight=0.05)

root.mainloop()
