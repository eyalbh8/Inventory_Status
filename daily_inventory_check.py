from excel_reading import *
from excel_anlyzing_data import check_expiration_date, check_minimum_inventory
from GUI_functions import print_expired_medicine, print_medicine_reached_minimum


def daily_check():
    file = read_file("medicine_inventory.xlsx")
    medicine_names = extracting_medicine_name(file)
    dates = get_expiration_date(file)
    quantity = get_quantity(file)
    minimum_inventory = get_minimum_inventory_index(file)
    reached_minimum = []
    expired = []

    for date in dates:
        date_list = date.split("/")
        if check_expiration_date(date_list):
            continue

        else:
            name = medicine_names[dates.index(date)]
            expired.append(name)

    for i in range(len(quantity)):
        if check_minimum_inventory(quantity[i], minimum_inventory[i]):
            continue

        else:
            reached_minimum.append(medicine_names[i])

    print_expired_medicine(expired)
    print_medicine_reached_minimum(reached_minimum)


daily_check()