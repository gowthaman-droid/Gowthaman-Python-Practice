import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# ---------------- DATABASE ----------------

conn = sqlite3.connect("campus_complaints.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS complaints (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    location TEXT NOT NULL,
    complaint TEXT NOT NULL,
    status TEXT DEFAULT 'Pending'
)
""")

conn.commit()


# ---------------- ADD COMPLAINT ----------------

def add_complaint():
    name = name_entry.get()
    category = category_box.get()
    location = location_entry.get()
    complaint = complaint_text.get("1.0", tk.END).strip()

    if name == "" or category == "" or location == "" or complaint == "":
        messagebox.showwarning("Warning", "Please fill all fields")
        return

    cursor.execute("""
    INSERT INTO complaints
    (name, category, location, complaint)
    VALUES (?, ?, ?, ?)
    """, (name, category, location, complaint))

    conn.commit()

    messagebox.showinfo(
        "Success",
        "Complaint submitted successfully!"
    )

    name_entry.delete(0, tk.END)
    category_box.set("")
    location_entry.delete(0, tk.END)
    complaint_text.delete("1.0", tk.END)

    show_complaints()


# ---------------- DISPLAY COMPLAINTS ----------------

def show_complaints():
    for item in table.get_children():
        table.delete(item)

    cursor.execute("""
    SELECT id, name, category, location, complaint, status
    FROM complaints
    """)

    records = cursor.fetchall()

    for record in records:
        table.insert("", tk.END, values=record)


# ---------------- UPDATE STATUS ----------------

def update_status():
    selected = table.selection()

    if not selected:
        messagebox.showwarning(
            "Warning",
            "Please select a complaint"
        )
        return

    item = table.item(selected[0])
    complaint_id = item["values"][0]

    status = status_box.get()

    if status == "":
        messagebox.showwarning(
            "Warning",
            "Please select a status"
        )
        return

    cursor.execute("""
    UPDATE complaints
    SET status = ?
    WHERE id = ?
    """, (status, complaint_id))

    conn.commit()

    messagebox.showinfo(
        "Success",
        "Complaint status updated"
    )

    show_complaints()


# ---------------- DELETE COMPLAINT ----------------

def delete_complaint():
    selected = table.selection()

    if not selected:
        messagebox.showwarning(
            "Warning",
            "Please select a complaint"
        )
        return

    item = table.item(selected[0])
    complaint_id = item["values"][0]

    answer = messagebox.askyesno(
        "Confirm",
        "Delete this complaint?"
    )

    if answer:
        cursor.execute(
            "DELETE FROM complaints WHERE id = ?",
            (complaint_id,)
        )

        conn.commit()

        show_complaints()


# ---------------- MAIN WINDOW ----------------

root = tk.Tk()
root.title("Campus Complaint Management System")
root.geometry("1100x650")

# ---------------- TITLE ----------------

title = tk.Label(
    root,
    text="Campus Complaint Management System",
    font=("Arial", 22, "bold")
)

title.pack(pady=15)


# ---------------- FORM FRAME ----------------

form_frame = tk.Frame(root)

form_frame.pack(pady=10)


# Name

tk.Label(
    form_frame,
    text="Student Name:"
).grid(row=0, column=0, padx=10, pady=8)

name_entry = tk.Entry(
    form_frame,
    width=30
)

name_entry.grid(row=0, column=1, padx=10)


# Category

tk.Label(
    form_frame,
    text="Category:"
).grid(row=1, column=0, padx=10, pady=8)

category_box = ttk.Combobox(
    form_frame,
    values=[
        "Wi-Fi",
        "Classroom",
        "Hostel",
        "Canteen",
        "Transport",
        "Electricity",
        "Water",
        "Other"
    ],
    width=27
)

category_box.grid(row=1, column=1, padx=10)


# Location

tk.Label(
    form_frame,
    text="Location:"
).grid(row=2, column=0, padx=10, pady=8)

location_entry = tk.Entry(
    form_frame,
    width=30
)

location_entry.grid(row=2, column=1, padx=10)


# Complaint

tk.Label(
    form_frame,
    text="Complaint:"
).grid(row=3, column=0, padx=10, pady=8)

complaint_text = tk.Text(
    form_frame,
    width=30,
    height=4
)

complaint_text.grid(row=3, column=1, padx=10)


# Submit button

submit_button = tk.Button(
    form_frame,
    text="Submit Complaint",
    command=add_complaint,
    width=20
)

submit_button.grid(
    row=4,
    column=1,
    pady=10
)


# ---------------- ADMIN SECTION ----------------

admin_frame = tk.Frame(root)

admin_frame.pack(pady=10)


tk.Label(
    admin_frame,
    text="Update Status:"
).grid(row=0, column=0, padx=10)


status_box = ttk.Combobox(
    admin_frame,
    values=[
        "Pending",
        "In Progress",
        "Resolved"
    ],
    width=20
)

status_box.grid(row=0, column=1, padx=10)


update_button = tk.Button(
    admin_frame,
    text="Update Status",
    command=update_status
)

update_button.grid(row=0, column=2, padx=10)


delete_button = tk.Button(
    admin_frame,
    text="Delete Complaint",
    command=delete_complaint
)

delete_button.grid(row=0, column=3, padx=10)


# ---------------- TABLE ----------------

table_frame = tk.Frame(root)

table_frame.pack(
    fill=tk.BOTH,
    expand=True,
    padx=15,
    pady=10
)


columns = (
    "ID",
    "Name",
    "Category",
    "Location",
    "Complaint",
    "Status"
)

table = ttk.Treeview(
    table_frame,
    columns=columns,
    show="headings"
)


for column in columns:

    table.heading(
        column,
        text=column
    )

    table.column(
        column,
        width=130
    )


table.column(
    "ID",
    width=50
)

table.pack(
    fill=tk.BOTH,
    expand=True
)


# ---------------- LOAD DATA ----------------

show_complaints()


# ---------------- START PROGRAM ----------------

root.mainloop()