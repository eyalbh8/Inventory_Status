import tkinter as tk
import smtplib


def print_medicine_reached_minimum(medicine_name):
    medicine_sentence = ""
    for i in range(len(medicine_name)):
        medicine_sentence = medicine_sentence + ", " + medicine_name[i]

    if len(medicine_name) == 0:
        medicine_name = "אין תרופות שהגיעו למינימום"

    else:
        medicine_name = "יש תרופות שהגיעו למינימום נא לבדוק במייל"

    window = tk.Tk()
    window.title("לשים לב")

    label = tk.Label(window, text=medicine_name, font=("calibre", 18, "bold"))
    label.grid(row=1, column=0)

    window.mainloop()
    medicine_allert = f"Reached the minimum: {medicine_sentence}"
    email_massage(medicine_allert)


def print_expired_medicine(medicine_name):
    medicine_sentence = ""
    for i in range(len(medicine_name)):
        medicine_sentence = medicine_sentence + ",\n" + medicine_name[i]

    if len(medicine_name) == 0:
        medicine_name = "אין תרופות פגות תוקף"

    else:
        medicine_name = "יש תרופות פגות תוקף נא לבדוק במייל"

    window = tk.Tk()
    window.title("לשים לב")

    label = tk.Label(window, text=medicine_name, font=("calibre", 18, "bold"))
    label.grid(row=1, column=0)

    window.mainloop()

    medicine_allert = f"Medicine expired: {medicine_sentence}"
    email_massage(medicine_allert)


def print_executed():
    window = tk.Tk()
    window.title("בוצע")

    executed_label = tk.Label(window, text="בוצע", font=("calibre", 18, "bold"))
    executed_label.grid(row=0, column=1)

    window.mainloop()


def email_massage(medicine_allert):
    email_address = "ttinbareyaltt@gmail.com"
    email_password = "takornak"
    receiver = "shoruzi@gmail.com"

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(email_address, email_password)

        subject = "Medicine allert"
        body = medicine_allert

        msg = f"Subject: {subject}\n\n{body}"

        smtp.sendmail(email_address, receiver, msg)
