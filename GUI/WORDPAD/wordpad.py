import tkinter
from tkinter import filedialog, INSERT, messagebox
import os
import webbrowser

# Variable to check open file
global open_stats_name
open_stats_name = False

# To check whether user has saved file or not
global is_file_saved
is_file_saved = False

global file_name

# Variable to perform cut and copy function
global selected_text
selected_text = False


# Function to delete everything from editor
def empty_editor():
    text_editor.delete("1.0", "end")


# Select all function
def select_all(*args):
    text_editor.tag_add('sel', 1.0, "end")


# New file function
def new_file(*args):
    global open_stats_name
    open_stats_name = False
    global is_file_saved
    is_file_saved = False
    print(os.path.commonprefix(['user/document']))
    empty_editor()
    text_editor.delete("1.0", "end")
    mainWindow.title("          *New - WORDPAD")
    status_indicator.config(text=f"Ready")


# Open new file function
def open_file(*args):
    text_file = filedialog.askopenfilename(initialdir="c:/user/", title="Open File", filetype=(("Text File", "*.txt"),
                                                                                               ("Html File", "*.html"),
                                                                                               ("Python File", "*.py"),
                                                                                               ("All files", "*.*")))
    if text_file:
        empty_editor()
        global open_stats_name
        open_stats_name = text_file
        file_path_name = text_file
        file_open_name = os.path.basename(file_path_name)
        status_indicator.config(text=f"Ready")
        mainWindow.title(f"          *{file_open_name} - WORDPAD")
        text_file = open(text_file)
        stuff = text_file.read()
        text_editor.insert("end", stuff)

        text_file.close()
        update_line_number()
        line_number.yview = text_editor.yview()
        # sync_scroll_bar(False)


# Save as file function
def save_as_file(*args):
    text_file_name = filedialog.asksaveasfile(defaultextension=".*", initialdir="c:/document", title="Save File",
                                              filetype=(("Text File", "*.txt"), ("Html File", "*.html"),
                                                        ("Python File", "*.py"), ("All files", "*.*")))
    if text_file_name:
        name = text_file_name.name
        name = os.path.basename(name)
        global file_name
        file_name = name

        mainWindow.title(f"          {file_name} - WORDPAD")
        status_indicator.config(text=f"Saved")

        # Bug fix the save function
        # Save file

        text_file_name = open(text_file_name.name, 'w')
        text_file_name.write(text_editor.get("1.0", "end"))
        text_file_name.close()
        global is_file_saved
        is_file_saved = True


# Save file function
def save_file(*args):
    global open_stats_name
    print(open_stats_name)
    if open_stats_name:
        text_file_name = open(open_stats_name, 'w')
        text_file_name.write(text_editor.get("1.0", "end"))
        # update status bar
        status_indicator.config(text=f"Saved")
        mainWindow.title(f"          {file_name} - WORDPAD")
        text_file_name.close()
    else:
        save_as_file()


# Getting on which line the user is
def get_line_numbers():
    output = ""
    row, col = text_editor.index('end').split('.')
    for i in range(1, int(row)):
        output += str(i) + '\n'

    return output


# Updating the line number whenever use release a key after press
def update_line_number(event=None):
    line_number_bar = get_line_numbers();
    line_number.config(state="normal")
    line_number.delete(1.0, "end")
    line_number.insert(1.0, line_number_bar)
    line_number.config(state="disabled")

    line_number.yview_moveto(float(int(float(text_editor.index('insert')))))

    line_number.yview = text_editor.yview()

    input_user = text_editor.get(0.0, "end")
    word_count = 0
    for words in input_user:
        if words == "\n" or words == " ":
            word_count += 1
    status_word_count.config(text=f"{word_count} Words")


# Removing the scroll event from line number
def remove_scroll(event):
    return "break"


# Function to make the line number sync with text editor when it is being scrolled
def sync_scroll_bar(event):
    line_number.yview = text_editor.yview()[1]


# Function to make the text editor and line number scroll in sync using scroll bar
def yview_set(*args):
    line_number.yview_moveto(args[1])
    text_editor.yview_moveto(args[1])


# Cut text function
def cut_text(*args):
    global selected_text
    # Condition if keyboard shortcut method was used
    if len(args) > 0:
        selected_text = mainWindow.clipboard_get()
    if text_editor.selection_get():
        # Get the selected text
        selected_text = text_editor.selection_get()
        # Delete selected text
        text_editor.delete("sel.first", "sel.last")
        mainWindow.clipboard_clear()
        mainWindow.clipboard_append(selected_text)


# Copy text function
def copy_text(*args):
    global selected_text
    # Condition if keyboard shortcut method was used
    if len(args) > 0:
        selected_text = mainWindow.clipboard_get()
    if text_editor.selection_get():
        selected_text = text_editor.selection_get()
        mainWindow.clipboard_clear()
        mainWindow.clipboard_append(selected_text)


# Paste text function
def paste_text(*args):
    global selected_text

    # Condition if keyboard shortcut method was used
    if len(args) > 0:
        selected_text = mainWindow.clipboard_get()
    else:
        if selected_text:
            position_cursor = text_editor.index(INSERT)
            text_editor.insert(position_cursor, selected_text)


# Open about window
def open_about(*args):
    # prefrence.AboutWindow(mainWindow);
    messagebox.showinfo('About', "WORDPAD\nv1.0.0\nMade with love")


# Redirects to github
def feedback():
    default_browser = webbrowser.get('windows-default')
    default_browser.open_new_tab("https://github.com/ypratham")


if __name__ == '__main__':
    mainWindow = tkinter.Tk()
    mainWindow.title("          WORDPAD")
    mainWindow.geometry('1280x720')
    mainWindow.iconbitmap("./text-editor-icon.ico")

    # Main frame
    editor_frame = tkinter.Frame(mainWindow, height=mainWindow.winfo_height())
    editor_frame.grid(row=0, column=0, sticky="nsew")

    # Scroll bar
    scrollbar = tkinter.Scrollbar(editor_frame)
    scrollbar.pack(side="right", fill="y")

    # Main editor
    text_editor = tkinter.Text(editor_frame, yscrollcommand=scrollbar.set, font=("Consolas", 16),
                               selectbackground="#B4D5FF", selectforeground="black", relief="flat", undo=True)
    text_editor.pack(side="right", fill="both", expand=True)
    text_editor.bind('<Any-KeyRelease>', update_line_number)
    text_editor.bind("<MouseWheel>", sync_scroll_bar)

    # Text to display line number's
    line_number = tkinter.Text(editor_frame, width=4, yscrollcommand=scrollbar.set, state="disabled", borderwidth=0,
                               relief="flat", takefocus=0, background="#F0F0F3", wrap="none", font=("Consolas", 16))
    line_number.pack(side="left", fill="both")
    line_number.bind("<MouseWheel>", remove_scroll)

    # Menu bar
    my_menu = tkinter.Menu(mainWindow)
    mainWindow.config(menu=my_menu)

    # Menu item 1 : File menu
    file_menu = tkinter.Menu(my_menu, tearoff=False, font=("Open Sans", 9))
    my_menu.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="New", command=new_file, accelerator="(Ctrl+N)")
    file_menu.add_command(label="Open", command=open_file, accelerator="(Ctrl+O)")
    file_menu.add_command(label="Save", command=save_file, accelerator="(Ctrl+S)")
    file_menu.add_command(label="Save As", command=save_as_file, accelerator="(Ctrl+Shift+S)")
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=mainWindow.quit, accelerator="(Alt+F4)")

    # Menu Item 2 : Edit menu
    edit_menu = tkinter.Menu(my_menu, tearoff=False, font=("Open Sans", 9))
    my_menu.add_cascade(label="Edit", menu=edit_menu)
    edit_menu.add_command(label="Cut", command=cut_text, accelerator="(Ctrl+X)")
    edit_menu.add_command(label="Copy", command=copy_text, accelerator="(Ctrl+C)")
    edit_menu.add_command(label="Paste", command=paste_text, accelerator="(Ctrl+V)")
    edit_menu.add_command(label="Select All", command=select_all, accelerator="(Ctrl+A)")
    edit_menu.add_separator()
    edit_menu.add_command(label="Undo", command=text_editor.edit_undo, accelerator="(Ctrl+Z)")
    edit_menu.add_command(label="Redo", command=text_editor.edit_redo, accelerator="(Ctrl+Y)")

    # Menu Item 3 : Help
    help_menu = tkinter.Menu(my_menu, tearoff=False, font=("Open Sans", 9))
    my_menu.add_cascade(label="Help", menu=help_menu)
    help_menu.add_command(label="About", command=open_about)
    help_menu.add_command(label="Preferences")
    help_menu.add_separator()
    help_menu.add_command(label="Feedback", command=feedback)

    # Status bar
    status_bar_frame = tkinter.Frame(mainWindow, background="#EBEBEB", )
    status_bar_frame.grid(row=1, column=0, sticky="nsew", ipadx=20, ipady=5)

    # Label to display word count
    status_word_count = tkinter.Label(status_bar_frame, text="Words", font=("Consolas", 10))
    status_word_count.pack(side="left", ipadx=5)

    # Label to display status
    status_indicator = tkinter.Label(status_bar_frame, text='Ready', anchor='e', font=("Consolas", 10))
    status_indicator.pack(side="right", ipadx=5)

    # Grid configuration
    editor_frame.grid_columnconfigure(0, weight=0)
    mainWindow.grid_columnconfigure(0, weight=1)
    mainWindow.grid_rowconfigure(0, weight=1)
    scrollbar.config(command=yview_set)
    update_line_number()

    # Keyboard shortcuts
    mainWindow.bind('<Control-o>', open_file)
    text_editor.bind("<Control-n>", new_file)
    text_editor.bind("<Control-s>", save_file)
    text_editor.bind("<Control-Shift-A>", save_as_file)
    text_editor.bind('<Control-Key-x>', cut_text)
    text_editor.bind('<Control-Key-c>', copy_text)
    text_editor.bind('<Control-Key-v>', paste_text)
    text_editor.bind("<Control-a>", select_all)

    # Loop until user close window
    mainWindow.mainloop()
