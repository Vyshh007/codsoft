import tkinter as tk
from tkinter import messagebox

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    if name.strip() == '' or phone.strip() == '':
        messagebox.showerror("Error", "Please enter both name and phone number.")
        return
    contacts[name] = phone
    update_contact_list()
    clear_entries()
def update_contact():
    selected_contact = contact_listbox.get(tk.ACTIVE)
    new_phone = phone_entry.get()

    if selected_contact and new_phone.strip() != '':
        contacts[selected_contact] = new_phone
        update_contact_list()
        clear_entries()
    else:
        messagebox.showerror("Error", "Please select a contact and enter a new phone number.")
def delete_contact():
    selected_contact = contact_listbox.get(tk.ACTIVE)
    if selected_contact:
        del contacts[selected_contact]
        update_contact_list()
        clear_entries()
    else:
        messagebox.showerror("Error", "Please select a contact to delete.")
def update_contact_list():
    contact_listbox.delete(0, tk.END)
    for name, phone in contacts.items():
        contact_listbox.insert(tk.END, name)
def show_contact_details(event):
    selected_contact = contact_listbox.get(tk.ACTIVE)
    if selected_contact:
        phone_entry.delete(0, tk.END)
        phone_entry.insert(tk.END, contacts[selected_contact])
def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
contacts = {
    'John Doe': '1234567890',
    'Jane Smith': '9876543210'
}
root = tk.Tk()
root.title("Contact Information")
name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0, padx=10, pady=5)

name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

phone_label = tk.Label(root, text="Phone:")
phone_label.grid(row=1, column=0, padx=10, pady=5)

phone_entry = tk.Entry(root)
phone_entry.grid(row=1, column=1, padx=10, pady=5)

add_button = tk.Button(root, text="Add Contact", command=add_contact)
add_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W+tk.E)

update_button = tk.Button(root, text="Update Contact", command=update_contact)
update_button.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W+tk.E)

delete_button = tk.Button(root, text="Delete Contact", command=delete_contact)
delete_button.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W+tk.E)

contact_listbox = tk.Listbox(root, width=40)
contact_listbox.grid(row=0, column=2, rowspan=5, padx=10, pady=5)
contact_listbox.bind('<<ListboxSelect>>', show_contact_details)
update_contact_list()
root.mainloop()