from tkinter import *
from tkinter import colorchooser, filedialog, font
from tkinter.messagebox import *
from tkinter.filedialog import *
import os.path


def color_chooser():
    color = colorchooser.askcolor()
    text_area.config(fg=color[1])


def change_font(*args):
    text_area.config(font=(font_name.get(), font_size.get()))


def new_file():
    window.title("untitled")
    text_area.delete(1.0, END)


def open_file():
    file = askopenfilename(defaultextension='.txt',
                           file=[("All files", "*.*"),
                                 ("Text Documents", "*.txt")])

    try:
        window.title(os.path.basename(file))
        text_area.delete(1.0, END)

        file = open(file, 'r')

        text_area.insert(1.0, file.read())

    except Exception:
        print("Can't open the file , Please try again .. ! ")

    finally:
        file.close()


def save_file():
    file = filedialog.asksaveasfilename(initialfile='untitled.txt',
                                        defaultextension='.txt',
                                        filetypes=[("All Files", "*.*"),
                                                   ("Text Documents", "*.txt")])
    if file is None:
        return

    else:
        try:
            window.title(os.path.basename(file))
            file = open(file, 'w')

            file.write(text_area.get(1.0, END))

        except Exception:
            print("couldn't read file")


def quite():
    window.destroy()


def copy():
    text_area.event_generate("<<Copy>>")


def paste():
    text_area.event_generate("<<Paste>>")


def cut():
    text_area.event_generate("<<Cut>>")


def about():
    showinfo('About this program', 'This is a program written by Ali Abu Usba')


window = Tk()

file = None

window.title("Text editor program")
window_height = 500
window_width = 500
screen_height = window.winfo_screenheight()
screen_width = window.winfo_screenwidth()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))

font_name = StringVar(window)
font_name.set("Arial")

font_size = StringVar(window)
font_size.set("20")

text_area = Text(window, bg="light yellow", font=(font_name.get(), font_size.get()))
text_area.grid(sticky=N + W + E + S)

scroll_bar = Scrollbar(text_area)
scroll_bar.pack(side=RIGHT, fill=Y)
scroll_bar.config(command=text_area.yview)
text_area.config(yscrollcommand=scroll_bar.set)

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

frame = Frame(window)
frame.grid()

button_color = Button(frame, text="Choose your color", command=color_chooser)
button_color.grid(row=0, column=0)

option_font = OptionMenu(frame, font_name, *font.families(), command=change_font)
option_font.grid(row=0, column=1)

size_font = Spinbox(frame, from_=1, to=100, textvariable=font_size, command=change_font)
size_font.grid(row=0, column=2)

menubar = Menu(window)
window.config(menu=menubar)

file_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label='New', command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Quite", command=quite)

edit_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)
edit_menu.add_command(label="Cut", command=cut)

help_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about)

window.mainloop()
