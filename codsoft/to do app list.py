import tkinter as tk
from tkinter import messagebox

# TO ADD NEW TASK TO THE TO DO LIST
def task_add():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("WARNING", "YOU HAVE TO ENTER A TASK")

# TO DELETE A TASK FROM THE TO DO LIST
def task_delete():
    try:
        index = listbox.curselection()
        listbox.delete(index)
    except:
        messagebox.showwarning("WARNING", "YOU HAVE TO SELECT A TASK TO DELETE")
        
# TO UPDATE A TASK IN THE TO DO LIST
def task_update():
    try:
        index = listbox.curselection()
        updated_task = entry.get()
        if updated_task:
            listbox.delete(index)
            listbox.insert(index, updated_task)
            entry.delete(0, tk.END)
        else:
            messagebox.showwarning("WARNING", "YOU HAVE TO ENTER A UPDATE TASK")
    except:
        messagebox.showwarning("WARNING", "YOU HAVE TO SELECT A TASK TO UPDATE")

# Function to mark the selected task as done
def task_done():
    try:
        index = listbox.curselection()
        task = listbox.get(index)
        updated_task = task + " (Done)"
        listbox.delete(index)
        listbox.insert(index, updated_task)
    except:
        messagebox.showwarning("WARNING", "YOU HAVE TO SELECT A TASK")

# CREATION OF MAIN WINDOW
win = tk.Tk()
win.title("TO DO LIST")

# TO DO LIST CREATION
listbox = tk.Listbox(win, width=60, height=10,bg="orange" ,font=("Arial", 12))
listbox.pack(pady=20)

# SCROLLBAR CREATION
scrollbar = tk.Scrollbar(win)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# ADDING SCROLLBAR TO THE LIST
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# TASK ENTRY FIELD
entry = tk.Entry(win,width=50 ,font=("Arial", 22))
entry.pack(pady=20)

# CREATION OF FUNCTIONS ADD,DEL,UPDATE,DONE BUTTONS
add_button = tk.Button(win, text="Add Task",fg="pink",bg="grey",padx=40,pady=20, command=task_add)
add_button.pack(pady=10)
delete_button = tk.Button(win, text="Delete Task",fg="pink",bg="grey",padx=40,pady=20,command=task_delete)
delete_button.pack(pady=10)
update_button = tk.Button(win, text="Update Task",fg="pink",bg="grey",padx=40,pady=20, command=task_update)
update_button.pack(pady=10)
mark_done_button = tk.Button(win, text="Mark as Done",fg="pink",bg="grey",padx=40,pady=20,command=task_done)
mark_done_button.pack(pady=10)

# END OF LOOP
win.mainloop()
