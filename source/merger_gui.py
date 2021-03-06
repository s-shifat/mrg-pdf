from tkinter import *
from tkinter.filedialog import askopenfilename
from PyPDF2 import PdfFileMerger
import os


# Tkinter mini cheatsheet
# widgets............
# Labels -- used to display text and images, display purpose only
#        -- can't be edited, kinda like print function
# Buttons
# Entry
# Text
# Frame
# ...................
# widget common parameters
# background, bd, bg, borderwidth, class,
#         colormap, container, cursor, height, highlightbackground,
#         highlightcolor, highlightthickness, menu, relief, screen, takefocus,
#         use, visual, width

def i_Merge(pdfs):
    print(pdfs)
    merger = PdfFileMerger(False)

    for pdf in pdfs:
        merger.append(pdf)

    merger.write("result.pdf")
    merger.close()


root = Tk()
root.title("Do Merge")

label = Label(root, text="Selected Files")
label.grid(row=1, column=0)

ent1 = Text(root, font=40)
ent1.grid(row=2, column=2)
files = list()


def browsefunc():
    filename = askopenfilename(filetypes=(("pdf file", "*.pdf"), ("All files", " *.* ")))
    files.append(filename)
    ent1.insert(END, filename + "\n")


def merge():
    i_Merge(files)
    root.destroy()


def op():
    os.system('explorer .')
    root.destroy()


b1 = Button(root, text="Load", font=40, command=browsefunc)
b1.grid(row=2, column=4)

merger_button = Button(root, text="Merge", font=40, command=merge)
merger_button.grid(row=2, column=5)
root.mainloop()

# Exit Screen
root = Tk()
root.geometry('250x150+15+15')
Label(root, text="Done!").pack(padx=15, pady=20)
openExport = Button(root, text="Open Folder", command=op)
openExport.pack(padx=10, pady=30)
root.mainloop()

