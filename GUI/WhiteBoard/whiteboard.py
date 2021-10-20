import os
from tkinter import *
from tkinter import messagebox, colorchooser
from tkinter.filedialog import asksaveasfilename,askopenfilename
import pyscreenshot as ImageGrab
from PIL import ImageTk,Image


class Color_Button(Button):#Inherited custom made color button , with default command to change colour of pen
    def __init__(self,color):
        self.color=color
        super().__init__(bg=color,relief=RIDGE,width=2,height=1,bd=2,command=self.on_click)
    def on_click(self):
        program.color_fg=self.color

class main:
    def __init__(self, master):
        self.root = master
        self.root.title("WhiteBoard")
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        self.root.geometry(f"{screen_width-int(screen_width*0.3)}x{screen_height-int(screen_height*0.3)}")
        self.color_fg = 'black'  # Colour of pen
        self.color_bg = 'white'  # Background colour
        self.root.configure(background='white')

        self.undo = open('undo.rec', 'w')


        # making colour buttons
        colors = ['#F8F8FF', '#cc1701','#0bd3d3','#a845b5', '#f1c232' , '#FF00FF']
        i=5;j=5#For Location
        for color in colors:
            Color_Button(color).place(x=i,y=j)#Refer class Color_Button
            j+=30
        colors = [ 'black', '#ffa500','red' ,'#009888', 'blue','#2bdf94']
        i=35;j=5
        for color in colors:
            Color_Button(color).place(x=i,y=j)
            j+=30

        # making other buttons and placing them in appropriate place
        self.Pallet_For_Foreground = Button(self.root, text='PALLET', font=('calibri', 10), bd=3, bg='white', command=self.choose_color,width=8, relief=RIDGE)
        self.Pallet_For_Foreground.place(x=0,y=185)


        self.erazer_button = Button(self.root, text='ERAZE', font=('calibri', 10), bd=3, bg='white', command=self.eraze,width=8, relief=RIDGE)
        self.erazer_button.place(x=0, y=215)

        self.clear_button = Button(self.root, text='CLEAR', bd=3, bg='white', command=self.clear, width=8, relief=RIDGE)
        self.clear_button.place(x=0, y=245)

        self.save_button = Button(self.root, text='SAVE', bd=3, bg='white', command=self.save, width=8, relief=RIDGE)
        self.save_button.place(x=0, y=275)

        self.Brush_Text = Label(self.root, text='BRUSH', bd=0, bg='white', font=('calibri', 11))
        self.Brush_Text.place(x=1, y=310)



        self.options = StringVar(self.root)
        self.options.set('3')#Default option
        self.size_chooser = OptionMenu(self.root, self.options, *( str(x) for x in range(10)))
        self.size_chooser.place(x=0, y=330)


        self.change_canvas_button=Button(self.root,text='CANVAS',font=('calibri', 10), bd=3,width=8, bg='white',command=self.change_canvas, relief=RIDGE)
        self.change_canvas_button.place(x=0, y=370)

        self.graph_button =Button(self.root,text='GRAPH',font=('calibri', 10), bd=3,width=8, bg='white',command=self.graph, relief=RIDGE)
        self.graph_button.place(x=0, y=400)

        self.undo_button = Button(self.root, text='UNDO', font=('calibri', 10), bd=3,width=8, bg='white',command=self.undo_exec, relief=RIDGE)
        self.undo_button.place(x=0, y=430)

        self.open_button=Button(self.root,text="OPEN" ,font=('calibri', 10), bd=3,width=8, bg='white',command=self.open, relief=RIDGE)
        self.open_button.place(x=0, y=460)


        self.Background_Button = Button(self.root, text='BG COLOR', font=('calibri', 10),bd=3, bg='white', command=self.change_bg, width=8, relief=RIDGE)
        self.Background_Button.place(x=0, y=490)

        # making the canvas and making it recognise movements of the mouse

        self.canvas = Canvas(self.root, bg='white', bd=3, relief=GROOVE, height=(screen_height-int(screen_height*0.33)), width=(screen_width-int(screen_width*0.37)))
        self.canvas.place(x=75, y=3)

        self.old_x = None
        self.old_y = None
        self.penwidth = 3
        self.tag = 0
        self.canvas.bind('<B1-Motion>', self.paint)  # drawing  line
        self.canvas.bind('<ButtonRelease-1>', self.reset)


    # All functions are defined below
    def paint(self, e):
        '''creates a canvas where you can paint'''

        if self.old_x and self.old_y:

            self.canvas.create_line(self.old_x, self.old_y, e.x, e.y,
                                    width=self.options.get(),
                                    fill=self.color_fg,
                                    capstyle=ROUND,
                                    smooth=True,
                                    tag='my_tag' + str(self.tag))
        self.old_x = e.x
        self.old_y = e.y

    def reset(self, e):
        '''reseting or cleaning the canvas'''
        self.old_x = None
        self.old_y = None

        self.canvas.create_oval(e.x, e.y, e.x, e.y,
                                width=self.options.get(),
                                outline=self.color_fg,
                                fill=self.color_fg,
                                tag='my_tag' + str(self.tag))
        self.undo.write(f"self.canvas.delete('{'my_tag' + str(self.tag)}')\n")
        self.tag += 1

    def clear(self):
        '''clears the canvas'''
        self.canvas.delete(ALL)

    def eraze(self):
        '''erazing stuff simply by changing colour of the brush to white'''
        self.undo.write(f"self.color_fg='{self.color_fg}'\n")
        self.undo.write(f"self.options.set({self.options.get()})\n")
        self.color_fg = 'white'
        self.options.set('20')

    def undo_exec(self):
        self.undo.close()
        # Find last line and execute it
        file = open("copy.txt", 'w')
        with open("undo.rec", 'r') as undo:
            length = sum(1 for x in undo)
        with open("undo.rec", 'r') as undo:
            count = 0
            for line in undo:
                count += 1
                if count != length:
                    file.write(line)
                pass
        file.close()
        os.replace(r'copy.txt', r'undo.rec')
        try:
            command = line
            exec(command)

        except UnboundLocalError:
            pass
        self.undo = open("undo.rec", 'a')

    def save(self):
        # Asking format
        filename: str = asksaveasfilename(initialdir="/Desktop", title="Select file", filetypes=(
            ('JPEG', '*.jpg'), ('PNG', '*.png'), ('PS', '*.ps'),
            ('BMP', '*.bmp'),
            ('GIF', '*.gif')),defaultextension=".jpg")
        print(filename)
        if filename.endswith('.ps'):
            # Saving a postscript file
            try:
                self.canvas.postscript(file=filename, colormode='color')
                messagebox.showinfo('File saved : ', str(filename))
            except:
                print('No file saved')

        else:
            try:
                # Making values for a screenshort
                x = self.root.winfo_rootx() + self.canvas.winfo_x()
                y = self.root.winfo_rooty() + self.canvas.winfo_y()
                x1 = x + self.canvas.winfo_width()
                y1 = y + self.canvas.winfo_height()
                screenshort = ImageGrab.grab().crop((x, y, x1, y1))
                screenshort.save(filename)
                messagebox.showinfo('File saved : ', str(filename))
            except:
                print('Error Saving File')

    def open(self):
        file_chosen=askopenfilename(initialdir="/Desktop", title="Select file", filetypes=(
            ('JPEG', '*.jpg'), ('PNG', '*.png'), ('PS', '*.ps'),
            ('BMP', '*.bmp'),
            ('GIF', '*.gif')),defaultextension=".jpg")
        try:
            self.img = ImageTk.PhotoImage(Image.open(file_chosen))
            self.canvas.create_image(0,0, anchor=NW, image=self.img)
        except:
            return()

    def choose_color(self):
        # variable to store hexadecimal code of color
        self.undo.write(f"self.color_fg='{self.color_fg}'\n")
        color_code = colorchooser.askcolor(title="Choose color")
        self.color_fg=color_code[1]#colour_code[1] is hex value of chose color. color_code[0] is rgb value of chosen color

    def change_bg(self):
        self.undo.write(f"self.canvas['bg']='{self.color_bg}'\n")
        color_code = colorchooser.askcolor(title="Choose Color")
        self.canvas['bg'] = color_code[1]

    def change_canvas(self):
        if self.root.winfo_width() != 1366:
            self.canvas['width'] = root.winfo_screenwidth()-int(root.winfo_screenwidth()*0.37)
            self.canvas['height']=root.winfo_screenheight()-int(root.winfo_screenheight()*0.33)
        else:
            self.canvas['height']=self.root.winfo_height()-20
            self.canvas['width']=self.root.winfo_width()-100

    def graph(self):
        try:
            MsgBox = messagebox.askyesnocancel(title='Graph',message='YES for Ruled Graph and No for Unruled Graph')
            if MsgBox:
                self.img = ImageTk.PhotoImage(Image.open('graph_ruled.png'))
                self.canvas.create_image(30, 20, anchor=NW, image=self.img)
            else:
                self.img = ImageTk.PhotoImage(Image.open('graph_unruled.png'))
                self.canvas.create_image(-100, 0, anchor=NW, image=self.img)

        except:
            messagebox.showwarning("That isn't working")

if __name__ == '__main__':
    #For Activating
    root = Tk()
    program=main(root)
    root.title('Paint')
    root.mainloop()
