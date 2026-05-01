import tkinter as tk
from tkinter import ttk , messagebox
from crud import add_student,fetch_student,update_student,delete_student

def run_app():
    root = tk.Tk()
    root.title("Student Management System")
    root.geometry("700x500")

    name_var = tk.StringVar()
    age_var = tk.StringVar()
    course_var = tk.StringVar()

    selected_id = {"value" : None}

    def add():
        if not name_var.get():
            messagebox.showerror("ERROR","Name Required")
            return
        add_student(name_var.get(),age_var.get(),course_var.get())
        load_data()
        clear_fields()

    def load_data():
        for row in tree.get_children():
            tree.delete(row)
        for row in fetch_student():
            tree.insert("",tk.END,values=row)

    def on_row_select(event):
        selected = tree.focus()
        data = tree.item(selected)['values']
        if data:
            selected_id['value'] = data[0]
            name_var.set(data[1])
            age_var.set(data[2])
            course_var.set(data[3])

    def update():
        if not selected_id["value"]:
            messagebox.showerror("Error", "Select a student")
            return
        update_student(
            selected_id["value"],
            name_var.get(),
            age_var.get(),
            course_var.get()
        )
        load_data()
        clear_fields()

    def delete():
        if not selected_id["value"]:
            messagebox.showerror("Error","Select a student")
            return
        delete_student(selected_id["value"])
        load_data()
        clear_fields()

    def clear_fields():
        selected_id["value"] = None
        name_var.set("")
        age_var.set("")
        course_var.set("")

    tk.Label(root, text="Name").pack()
    tk.Entry(root, textvariable=name_var).pack()

    tk.Label(root, text="Age").pack()
    tk.Entry(root, textvariable=age_var).pack()

    tk.Label(root, text="Course").pack()
    tk.Entry(root, textvariable=course_var).pack()


    btn_frame = tk.Frame(root)
    btn_frame.pack(pady=10)

    tk.Button(btn_frame, text="Add", command=add).grid(row=0, column=0, padx=5)
    tk.Button(btn_frame, text="Update",command=update).grid(row=0, column=1, padx=5)
    tk.Button(btn_frame, text="Delete",command=delete).grid(row=0, column=2, padx=5)
    tk.Button(btn_frame, text="Clear",command=clear_fields).grid(row=0, column=3, padx=5)

    columns = ("ID", "Name", "Age", "Course")
    tree = ttk.Treeview(root, columns=columns, show="headings")

    for col in columns:
        tree.heading(col,text=col)

    tree.pack(fill=tk.BOTH, expand=True)
    tree.bind("<ButtonRelease-1>", on_row_select)
    load_data()
    root.mainloop()