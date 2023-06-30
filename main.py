import os
import shutil
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
import time

window = Tk()
window.geometry("290x470+650+150")
window.title("Directory File Mover")
window.resizable(False, False)

bg1='gainsboro' 
bg2='rosybrown'
bg3='darkgray' 

up_frame  =  Frame(window,  width=1880,  height=  400,  bg=bg1)
up_frame.grid(row=0,  column=0,  padx=5,  pady=5, sticky='w'+'e'+'n'+'s')

down_frame  =  Frame(window,  width=500,  height= 420,  bg=bg2)
down_frame.grid(row=1,  column=0,  padx=5,  pady=5, sticky='w'+'e'+'n'+'s')

directory = ""
source_directory = ""
destination_directory = ""
move_or_copy = IntVar(value=0)

def open_directory():
    global source_directory
    source_directory = fd.askdirectory()
    # report_list = os.listdir(source_directory)
    st.insert(END, "Source directory paths: " + source_directory + '\n')
    return source_directory

def dest_directory():
    global destination_directory
    destination_directory = fd.askdirectory()
    st.insert(END, "Destination directory paths: " + destination_directory + '\n')
    return destination_directory 

def copy_files():
    global source_directory
    global destination_directory
    global move_or_copy

    start_time = time.time()
    # Получаем список всех файлов в исходной директории и ее подпапках
    file_list = []
    for root, dirs, files in os.walk(source_directory):
        for file_name in files:
            # Полный путь к файлу в исходной директории
            source_file = os.path.join(root, file_name)
            file_list.append(source_file)

    # Копируем или перемещаем файлы в целевую директорию
    for source_file in file_list:
        destination_file = os.path.join(destination_directory, os.path.basename(source_file))
        
        if measurement_system.get() == 1:
            shutil.move(source_file, destination_file)
            st.insert(END, "File" + source_file + " moved successfully!" + '\n')
        else:    
            shutil.copy(source_file, destination_file)
            st.insert(END, "File" + source_file + " copied successfully!" + '\n') 
    end_time = time.time()
    execution_time = end_time - start_time
    st.insert(END, "Time: " + str(round(execution_time, 2)) + " sec " + '\n')
    st.see('end')  

Label(up_frame, text='Source directory paths', bg=bg1, width=25).grid(row=1, column=1, pady=0)
Label(up_frame, text='Destination directory paths', bg=bg1, width=25).grid(row=2, column=1, pady=0)

Button(up_frame, text="FROM", command=open_directory, width=10).grid(row=1, column=2, pady=5, padx=5)
Button(up_frame, text="TO", command=dest_directory, width=10).grid(row=2, column=2, pady=5, padx=5)
Button(up_frame, text="RUN", command=copy_files, width=10).grid(row=3, column=2, pady=5, padx=5)

Label(up_frame, text='MOVE', background=bg1, border=0, font='Arial 8 bold').grid(row=3, column=1, sticky='e', padx=0)
Label(up_frame, text='COPY', background=bg1, border=0, font='Arial 8 bold').grid(row=3, column=1, sticky='w', padx=0)
measurement_system = Scale(up_frame, orient=HORIZONTAL, from_= 0, to=1, length=50, showvalue=OFF, variable=move_or_copy, troughcolor=bg1, highlightbackground=bg1)
measurement_system.grid(row=3, column=1, padx=0,  pady=0)

st = ScrolledText(down_frame, width=35,  height=20, bd=1.5, font = 'Arial 10')
st.grid(row=1, padx=5, pady=5, sticky='w'+'e'+'n'+'s')

#------------------------------------------------------------------------------
def calculator():
    os.system("C:/WINDOWS/System32/calc.exe")
    return
def show_about():
    messagebox.showinfo(title="About", message="Version: 1.0\nAuthor: Stanislav Nikulin\nTelegram: @stan_nikulin\nDate: 2023\nLicense: MIT")
#меню
menu_bar = Menu(window)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Exit", command=window.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About...", command=show_about)
menu_bar.add_cascade(label="Help", menu=help_menu)

window.config(menu=menu_bar)

#------------------------------------------------------------------------------

window.mainloop()