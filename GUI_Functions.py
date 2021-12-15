import tkinter as tk
import smtplib

def Print_min(Medicine_name=[]):
    Medicine_sentence = ""
    for i in range(len(Medicine_name)):
        Medicine_sentence = Medicine_sentence + ", " + Medicine_name[i]
    
    if len(Medicine_name) == 0:
        Medicine_name = "אין תרופות שהגיעו למינימום"

    else:
        Medicine_name = "יש תרופות שהגיעו למינימום נא לבדוק במייל"

    window = tk.Tk()
    window.title("לשים לב")

    label = tk.Label(window, text = Medicine_name, font=("calibre",18, "bold"))
    label.grid(row=1,column=0)
        
    window.mainloop()
    Medicine_allert = f"Reached the minimum: {Medicine_sentence}"
    Email_massage(Medicine_allert)

def Print_Expired(Medicine_name=[]):
    Medicine_sentence = ""
    for i in range(len(Medicine_name)):
        Medicine_sentence = Medicine_sentence + ",\n" + Medicine_name[i]

    if len(Medicine_name) == 0:
        Medicine_name = "אין תרופות פגות תוקף"

    else:
        Medicine_name = "יש תרופות פגות תוקף נא לבדוק במייל"

    window = tk.Tk()
    window.title("לשים לב")

    label = tk.Label(window, text = Medicine_name, font=("calibre",18, "bold"))
    label.grid(row=1,column=0)

    window.mainloop()
    
    Medicine_allert = f"Medicine expired: {Medicine_sentence}"
    Email_massage(Medicine_allert)

def Print_Executed():
    window = tk.Tk()
    window.title("בוצע")

    Executed_label = tk.Label(window, text = "בוצע", font=("calibre",18, "bold"))
    Executed_label.grid(row=0,column=1)

    window.mainloop()


def Email_massage(Medicine_allert):
    EMAIL_ADRESS = "ttinbareyaltt@gmail.com"
    EMAIL_PASSWORD = "takornak"
    RECIEVER = "shoruzi@gmail.com"

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(EMAIL_ADRESS, EMAIL_PASSWORD)
    
        subject = "Medicine allert"
        body = Medicine_allert

        msg = f"Subject: {subject}\n\n{body}"
    
        smtp.sendmail(EMAIL_ADRESS, EMAIL_ADRESS, msg)
