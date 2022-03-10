import tkinter as tk
from excel_anlyzing_data import check_medicine_index
from excel_writing import save_changes, save_new_medicine, get_max_row
from excel_reading import extracting_medicine_name, read_file
from GUI_functions import print_executed

list_of_names = extracting_medicine_name(read_file("medicine_inventory.xlsx"))


def updating_medicine_data_base():
    if value_inside.get() == "רשימת תרופות":
        medicine_index = check_medicine_index(medicine_name.get(), list_of_names)

    else:
        medicine_index = check_medicine_index(value_inside.get(), list_of_names)

    if medicine_index is not False:
        save_changes(medicine_index, expiration_date.get(), quantity.get(), minimum_inventory.get())
        print_executed()
    else:
        new_medicine_row_num = get_max_row() + 1
        save_new_medicine(new_medicine_row_num, medicine_name.get(),
                          expiration_date.get(), quantity.get(), minimum_inventory.get())
        print_executed()


window = tk.Tk()
window.title("עדכון תרופות")

medicine_name = tk.StringVar(window)
medicine_name_label = tk.Label(window, text="שם התרופה", font=('calibre', 14, 'bold'))
medicine_name_label.grid(row=0, column=4)
medicine_name_entry = tk.Entry(window, textvariable=medicine_name, font=('calibre', 14, 'normal'))
medicine_name_entry.grid(row=1, column=4)

value_inside = tk.StringVar(window)
value_inside.set("רשימת תרופות")

option_menu = tk.OptionMenu(window, value_inside, *list_of_names)
option_menu.grid(row=2, column=4)

quantity = tk.StringVar(window)
quantity_label = tk.Label(window, text="כמות", font=('calibre', 10, 'bold'))
quantity_label.grid(row=0, column=3)
quantity_entry = tk.Entry(window, textvariable=quantity, font=('calibre', 10, 'normal'))
quantity_entry.grid(row=1, column=3)

minimum_inventory = tk.StringVar(window)
minimum_inventory_label = tk.Label(window, text="כמות מינימום", font=('calibre', 10, 'bold'))
minimum_inventory_label.grid(row=0, column=2)
minimum_inventory_entry = tk.Entry(window, textvariable=minimum_inventory, font=('calibre', 10, 'normal'))
minimum_inventory_entry.grid(row=1, column=2)

expiration_date = tk.StringVar(window)
expiration_date_label = tk.Label(window, text="תאריך תפוגה", font=('calibre', 10, 'bold'))
expiration_date_label.grid(row=0, column=1)
expiration_date_entry = tk.Entry(window, textvariable=expiration_date, font=('calibre', 10, 'normal'))
expiration_date_entry.grid(row=1, column=1)

end = tk.Button(window, bg="black", fg="white", text="סיים", command=updating_medicine_data_base)
end.grid(row=2, column=2)

window.mainloop()
