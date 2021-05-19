# Author : Manibarathi
# Github : https://github.com/mani-barathi

import tkinter,os
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import datetime
from tkinter.font import Font

class notepad:
    def __init__(self):
        # initialize
        self.file = None
        self.window = tkinter.Tk(className="Untitled - Notepad")
        self.window.geometry('700x500')
        self.menubar = Menu(self.window)
        self.filemenu = Menu(self.menubar,tearoff=0)
        self.editmenu = Menu(self.menubar,tearoff=0)
        self.helpmenu = Menu(self.menubar,tearoff=0)
        self.var = StringVar()
        self.textarea = Text(self.window,font="Calibri 12")
        self.scrollbar = Scrollbar(self.textarea)
        self.fontsize = 13
        self.bold = 0
        self.italic = 0
        
        # file menu
        self.filemenu.add_command(label="New ",command=self.newfile,accelerator="Ctrl+N")
        self.filemenu.add_command(label="Open ",command=self.openfile,accelerator="Ctrl+O")
        self.filemenu.add_command(label="Save",command=self.save,accelerator="Ctrl+S")
        self.filemenu.add_command(label="Save as",command=self.saveas)
        self.filemenu.add_separator()                               # displays a line inbetween
        self.filemenu.add_command(label="Exit",command=self.exitfile,accelerator="Ctrl+Q")
        self.menubar.add_cascade(label="File",menu=self.filemenu)   # adding the filemenu to menubar

        # edit menu
        self.editmenu.add_command(label="Increase font size",command=self.incresefont,accelerator="Ctrl+Up")
        self.editmenu.add_command(label="Decrease font size",command=self.decresefont,accelerator="Ctrl+Down")        
        self.editmenu.add_command(label="Bold/normal",command=self.boldfont,accelerator="Ctrl+b")
        self.editmenu.add_command(label="italic/normal",command=self.italicfont,accelerator="Ctrl+i")
        self.editmenu.add_command(label="Date/time",command=self.date_time,accelerator="F5")
        self.menubar.add_cascade(label="Edit",menu=self.editmenu)
        # help menu
        self.helpmenu.add_command(label="About",command=self.about)
        self.menubar.add_cascade(label="help",menu=self.helpmenu)   # adding the helpmenu to menubar
        # add menubar to window
        self.window.config(menu=self.menubar)
        # textarea
        self.textarea.pack(expand=1,fill='both')
        #scrollbar
        self.scrollbar.pack(side=RIGHT,fill=Y)
        # setting the scrollbar to textarea
        self.scrollbar.config(command=self.textarea.yview)
        self.textarea.config(yscrollcommand=self.scrollbar.set)

        #  key binding for shortcuts
        self.window.bind("<Control-q>",self.exitfile)
        self.window.bind("<Control-s>",self.save)
        self.window.bind("<Control-o>",self.openfile)
        self.window.bind("<Control-n>",self.newfile)
        self.window.bind("<Control-Up>",self.incresefont)
        self.window.bind("<Control-Down>",self.decresefont)
        self.window.bind("<F5>",self.date_time)
        self.window.bind("<Control-b>",self.boldfont)
        self.window.bind("<Control-i>",self.italicfont)
        #self.window.bind("<Control><Shit><s>",self.saveas)

    def newfile(self,event=None):
        confirm = tkinter.messagebox.askyesnocancel(
            message="Do you want to save the current file?",
            title="Save on close" 
        )
        if confirm:
            self.save()
            self.reset()
        elif confirm is None:
            pass
        else :
            self.reset()


    def reset(self):
        self.textarea.delete(1.0,END)
        self.file = None
        self.filename = None
        self.window.title("Untitled - Notepad") 
        self.flag = 0

    def openfile(self,event=None):
        self.file = filedialog.askopenfilename(initialdir="/",title="select file",filetypes=(("Text Files",".txt"),("All Files","*.*")))
        if(self.file == None or self.file ==""):
            pass
        else :
            file = open(self.file,'r')
            self.textarea.insert(1.0,file.read())
            self.filename = os.path.basename(self.file).split(".")
            self.window.title(self.filename[0]+ " - Notepad")
            file.close()

    def save(self,event=None):
        if self.file == None :
            self.file = filedialog.asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",filetypes=[("Text Documents","*.txt"),("All Files","*.*")])
            if self.file == "":      # supppose if user starts to save but then cancels without saving it
                self.file = None     # setting the empty self.file= None
            else:
                file = open(self.file,'w')
                file.write(self.textarea.get(1.0,END))
                file.close
                self.filename=os.path.basename(self.file).split(".")
                self.window.title(self.filename[0]+ " - Notepad")
                tkinter.messagebox.showinfo("Info ","File saved")
        else:
            file = open(self.file,'w')
            file.write(self.textarea.get(1.0,END))
            file.close()
            tkinter.messagebox.showinfo("Info ","File saved")


    def saveas(self,event=None):
        file=filedialog.asksaveasfile(mode='w+',defaultextension=".txt",filetypes=[("Text Documents","*.txt"),("All Files","*.*")])
        file.write(self.textarea.get(1.0,END))
        filename=os.path.basename(file.name).split(".")
        self.window.title(filename[0]+" - Notepad")
        self.file=file.name
        file.close()
        
    def incresefont(self,event=None):
        self.fontsize=self.fontsize + 1
        f="Calibri "+str(self.fontsize)
        self.textarea.configure(font=f)

    def decresefont(self,event=None):
        self.fontsize=self.fontsize - 1
        f="Calibri "+str(self.fontsize)
        self.textarea.configure(font=f)
    
    def boldfont(self,event=None):
        if(self.bold == 0):
            myFont = Font(family="Times New Roman", size=self.fontsize,weight="bold")
            self.textarea.configure(font=myFont)
            self.bold=1
        elif(self.bold==1):
            myFont = Font(family="Times New Roman", size=self.fontsize,weight="normal")
            self.textarea.configure(font=myFont)
            self.bold=0
    
    def italicfont(self,event=None):
        if(self.italic == 0):
            myFont = Font(family="Times New Roman", size=self.fontsize,slant="italic")
            self.textarea.configure(font=myFont)
            self.italic = 1
        elif(self.italic == 1):
            myFont = Font(family="Times New Roman", size=self.fontsize,slant="roman")
            self.textarea.configure(font=myFont)
            self.italic = 0

    def date_time(self,event=None):
        dt = datetime.datetime.now().strftime("%H:%M %x")
        self.textarea.insert(INSERT,dt)

    def exitfile(self,event=None):
        self.window.quit()
    
    def about(self):
        tkinter.messagebox.showinfo("Notepad","This notepad is created by Manibarathi using python") 

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    pad = notepad()
    pad.run()
