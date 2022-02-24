from datetime import date


def check_medicine_index(name, list_of_names):
    if str(name) in list_of_names:
        index = list_of_names.index(name)
        return index + 2

    else:
        return False


def check_minimum_inventory(quantity, minimum):
    print(quantity, minimum)
    try:
        if int(quantity) <= int(minimum):
            return False

        else:
            return True

    except:
        return False


def get_today_date():
    today = str(date.today())
    today_list = today.split("-")
    today_list.reverse()
    return today_list


def check_expiration_date(date):
    if date == get_today_date():
        return False

    else:
        return True
