import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def saving_file():
    file_location = asksaveasfilename(defaultextension="txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if not file_location:
        return
    with open(file_location, "w") as file_output:
        text = text_edit.get(1.0, tk.END)
        file_output.write(text)
    root.title(f"MY NOTEPAD - {file_location}")

def open_file():
    file_location = askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if not file_location:
        return
    text_edit.delete(1.0, tk.END)
    with open(file_location, "r") as file_input:
        text = file_input.read()
        text_edit.insert(tk.END, text)
    root.title(f"MY NOTEPAD - {file_location}")

def cut_text():
    text_edit.event_generate("<<Cut>>")

def copy_text():
    text_edit.event_generate("<<Copy>>")

def paste_text():
    text_edit.event_generate("<<Paste>>")


root = tk.Tk()
root.title("MY NOTEPAD")
root.rowconfigure(0, minsize=800)
root.columnconfigure(1, minsize=800)

style = ttk.Style()
style.theme_use("clam")

text_edit = tk.Text(root)
text_edit.grid(row=0, column=1, sticky="nsew")

frame_button = tk.Frame(root, relief=tk.RAISED, bd=3)
frame_button.grid(row=0, column=0, sticky="ns")

button_open = ttk.Button(frame_button, text="Open", command=open_file)
button_open.grid(row=0, column=0, padx=5, pady=5)

button_save = ttk.Button(frame_button, text="Save As", command=saving_file)
button_save.grid(row=1, column=0, padx=5,pady=5)

button_cut = ttk.Button(frame_button, text="Cut", command=cut_text)
button_cut.grid(row=2, column=0, padx=5, pady=5)

button_copy = ttk.Button(frame_button, text="Copy", command=copy_text)
button_copy.grid(row=3, column=0, padx=5, pady=5)

button_paste = ttk.Button(frame_button, text="Paste", command=paste_text)
button_paste.grid(row=4, column=0, padx=5, pady=5)


root.mainloop()
