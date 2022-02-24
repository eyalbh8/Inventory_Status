from excel_reading import extracting_medicine_name, read_file
from GUI_functions import *
from excel_anlyzing_data import check_medicine_index, check_minimum_inventory
from openpyxl import load_workbook


def apply():
    excel_workbook = load_workbook(filename="medicine_inventory.xlsx")
    sheet = excel_workbook["mainSheet"]

    index = check_medicine_index(value_inside.get(), List_of_Names)
    cell_position = "C" + str(index)
    cell = sheet[cell_position].value
    sheet[cell_position] = int(cell) - Quantity_var.get()

    if check_minimum_inventory(sheet[cell_position].value, sheet["D" + str(index)].value):
        pass

    else:
        print_medicine_reached_minimum(value_inside.get())

    excel_workbook.save("medicine_inventory.xlsx")

    print_executed()


def update_file():
    import Add_Medicine


List_of_Names = extracting_medicine_name(read_file("medicine_inventory.xlsx"))

window = tk.Tk()
window.title("בס''ד")

value_inside = tk.StringVar(window)
value_inside.set("רשימת תרופות")

option_menu = tk.OptionMenu(window, value_inside, *List_of_Names)
option_menu.grid(row=1, column=1)

Quantity_var = tk.IntVar()
Quantity_label = tk.Label(window, text="Quantity", font=('calibre', 14, 'bold'))
Quantity_label.grid(row=0, column=0)
Quantity_entry = tk.Entry(window, textvariable=Quantity_var, font=('calibre', 14, 'normal'))
Quantity_entry.grid(row=1, column=0)

submit_button = tk.Button(window, text='סיום', command=apply)
submit_button.grid(row=2, column=1)

Update_file_button = tk.Button(window, text='עדכון מלאי', command=update_file)
Update_file_button.grid(row=2, column=0)

window.mainloop()
