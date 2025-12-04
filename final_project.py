from pathlib import Path
import tkinter as ti
import re
from random import randint
from tkinter import messagebox as mb
import pandas as pd


def center_window(win):
    win.update_idletasks()
    width = win.winfo_width()
    height = win.winfo_height()
    x = (win.winfo_screenwidth() // 2) - (width // 2)
    y = (win.winfo_screenheight() // 4) - (height // 2)
    win.geometry(f"{width}x{height}+{x}+{y}")


class Account:
    bank_accounts = {}

    def __init__(self):
        self.acc_no = None

    def initialize(self):
        self.initial = ti.Tk()

        main_lb = ti.Label(self.initial, text="Please Choose An Option").grid(
            row=0)
        create_btn = ti.Button(self.initial, text="Create An Account",
                               command=user.create_account).grid(row=1)
        edit_btn = ti.Button(self.initial, text="Edit An Existing Account",
                             command=user.edit_account).grid(row=2)
        show_balance_btn = ti.Button(self.initial,
                                     text="Show An Account's Balance", command=user.show_balance).grid(row=3)
        deposit_btn = ti.Button(self.initial, text="Deposit To Your Account",
                                command=user.deposit).grid(row=4)
        withdraw_btn = ti.Button(self.initial, text="Withdraw From Your Account",
                                 command=user.withdrawal).grid(row=5)
        transer_btn = ti.Button(self.initial, text="Transfer To Another Account",
                                command=user.transfer).grid(row=6)
        exit_btn = ti.Button(self.initial,
                             text="Exit", command=self.initial.destroy).grid(row=7)

        center_window(self.initial)
        self.initial.mainloop()

    def create_account(self):
        self.initial.withdraw()

        def validation():

            first_name = first_name_en.get()
            last_name = last_name_en.get()
            birth_date = birth_date_en.get()
            national_id = national_id_en.get()
            phone = phone_en.get()
            Email = Email_en.get()

            box.withdraw()

            info = {"First Name": first_name,
                    "Last Name": last_name,
                    "Birth Date": birth_date,
                    "National ID": national_id,
                    "Phone Number": phone,
                    "Email": Email}

            first_name = info["First Name"]
            if not (first_name.isalpha() and len(first_name) >= 3):
                mb.showerror(
                    "Value Error", "First Name Must Contain At Least 3 Characters!")
                first_name_en.delete(0, ti.END)
                box.deiconify()
            else:
                last_name = info["Last Name"]
                if not (last_name.isalpha() and len(last_name) >= 4):
                    mb.showerror(
                        "Value Error", "Last Name Must Contain at Least 4 Characters!")
                    last_name_en.delete(0, ti.END)
                    box.deiconify()
                else:
                    birth_date = info["Birth Date"]
                    if not (re.match(r"^(13|14)[0-9]{2}\/([1-9]|1[0-2])\/([0-9]|1[0-9]|2[0-9]|3[0-1])$", birth_date)):
                        mb.showerror(
                            "Value Error", "The Birthdate Is Invalid!")
                        birth_date_en.delete(0, ti.END)
                        box.deiconify()
                    else:
                        month = int(birth_date.split("/")[1])
                        day = int(birth_date.split("/")[2])
                        if not ((month < 7 and day < 32) or (month > 6 and day < 31)):
                            mb.showerror(
                                "Value Error", "This Date Does Not Exist!")
                            birth_date_en.delete(0, ti.END)
                            box.deiconify()
                        else:
                            national_id = info["National ID"]
                            if not (national_id.isdigit() and re.match(r"^0[0-9]{9}$", national_id)):
                                mb.showerror(
                                    "Value Error", "National ID Is Invalid!")
                                national_id_en.delete(0, ti.END)
                                box.deiconify()
                            else:
                                phone = info["Phone Number"]
                                if not (phone.isdigit() and re.match(r"^09[1-9]{2}[0-9]{7}$", phone)):
                                    mb.showerror(
                                        "Value Error", "Phone Number Is Invalid!")
                                    phone_en.delete(0, ti.END)
                                    box.deiconify()
                                else:
                                    Email = info["Email"]
                                    if not (re.match(r"^[A-Za-z0-9_\.-]+@(yahoo|gmail|hotmail)\.(com|gov)$", Email)):
                                        mb.showerror(
                                            "Value Error", "Email Address Is Invalid!")
                                        Email_en.delete(0, ti.END)
                                        box.deiconify()
                                    else:
                                        mb.showinfo(
                                            "Info", "Account Was Successfully Created!")
                                        box.destroy()
                                        while True:
                                            acc_no = randint(
                                                10**11, 10**12 - 1)
                                            if acc_no not in Account.bank_accounts:
                                                break
                                        info["Account Number"] = acc_no

                                        def finalize():
                                            info["Account Number"] = acc_no
                                            Account.bank_accounts[acc_no] = info
                                            Account.update_excel()

                                            show = ti.Toplevel()
                                            title_lb = ti.Label(show, text="New Account").grid(
                                                row=0, column=0, columnspan=2)
                                            first_name_lb = ti.Label(show,
                                                                     text="First Name").grid(row=1, column=0)
                                            last_name_lb = ti.Label(show,
                                                                    text="Last Name").grid(row=2, column=0)
                                            birth_date_lb = ti.Label(show,
                                                                     text="Birth Date").grid(row=3, column=0)
                                            national_id_lb = ti.Label(show,
                                                                      text="National ID").grid(row=4, column=0)
                                            phone_lb = ti.Label(show,
                                                                text="Phone Number").grid(row=5, column=0)
                                            Email_lb = ti.Label(show,
                                                                text="Email").grid(row=6, column=0)
                                            acc_no_lb = ti.Label(show,
                                                                 text="Account Number").grid(row=7, column=0)
                                            balance_lb = ti.Label(show,
                                                                  text="Balance").grid(row=8, column=0)

                                            acc_first_name = ti.Label(show,
                                                                      text=info["First Name"]).grid(row=1, column=1)
                                            acc_last_name = ti.Label(show,
                                                                     text=info["Last Name"]).grid(row=2, column=1)
                                            acc_birth_date = ti.Label(show,
                                                                      text=info["Birth Date"]).grid(row=3, column=1)
                                            acc_national_id = ti.Label(show,
                                                                       text=info["National ID"]).grid(row=4, column=1)
                                            acc_phone = ti.Label(show,
                                                                 text=info["Phone Number"]).grid(row=5, column=1)
                                            acc_Email = ti.Label(show,
                                                                 text=info["Email"]).grid(row=6, column=1)
                                            acc_acc_no = ti.Label(show,
                                                                  text=info["Account Number"]).grid(row=7, column=1)
                                            acc_balance = ti.Label(show,
                                                                   text=info["Balance"]).grid(row=8, column=1)

                                            ok_btn = ti.Button(show, text="OK", command=lambda: [show.destroy(), self.initial.deiconify()]).grid(
                                                row=9, column=0, columnspan=2)

                                            center_window(show)

                                        def add_balance():
                                            balance = ans_en.get()
                                            ans_en.delete(0, ti.END)

                                            if balance.isdigit():
                                                root.destroy()
                                                mb.showinfo(
                                                    "Info", "Your Balance Was Successfully Updated!")
                                                info["Balance"] = int(balance)
                                                finalize()
                                            else:
                                                mb.showerror(
                                                    "Error", "Please Enter A Valid Input!")

                                        ask = mb.askyesno(
                                            "User Permission", "Do You Want To Add To Your Balance?")
                                        if ask:
                                            def cncl():
                                                root.destroy()
                                                info["Balance"] = 0
                                                finalize()

                                            root = ti.Toplevel()

                                            ans_lb = ti.Label(root,
                                                              text="Please Enter The Amount You Want To Add:").grid(row=0, column=0, columnspan=2)
                                            ans_en = ti.Entry(root)
                                            ans_en.grid(
                                                row=1, column=0, columnspan=2)

                                            btn_frame = ti.Frame(root)
                                            btn_frame.grid(
                                                row=2, column=0, columnspan=2, pady=10)

                                            ti.Button(btn_frame, text="Add", command=add_balance).pack(
                                                side="left", padx=10)
                                            ti.Button(btn_frame, text="Cancel", command=cncl).pack(
                                                side="left", padx=10)

                                            center_window(root)

                                        else:
                                            info["Balance"] = 0
                                            mb.showinfo("Info", "Done!")
                                            finalize()

        box = ti.Toplevel(self.initial)
        main_lb = ti.Label(box, text="Account Information").grid(
            row=0, column=0, columnspan=2)
        first_name_lb = ti.Label(box, text="First Name").grid(row=1, column=0)
        last_name_lb = ti.Label(box, text="Last Name").grid(row=2, column=0)
        birth_date_lb = ti.Label(box, text="Birth Date").grid(row=3, column=0)
        national_id_lb = ti.Label(
            box, text="National ID").grid(row=4, column=0)
        phone_lb = ti.Label(box, text="Phone Number").grid(row=5, column=0)
        Email_lb = ti.Label(box, text="Email").grid(row=6, column=0)

        first_name_en = ti.Entry(box)
        first_name_en.grid(row=1, column=1)

        last_name_en = ti.Entry(box)
        last_name_en.grid(row=2, column=1)

        birth_date_en = ti.Entry(box)
        birth_date_en.grid(row=3, column=1)

        national_id_en = ti.Entry(box)
        national_id_en.grid(row=4, column=1)

        phone_en = ti.Entry(box)
        phone_en.grid(row=5, column=1)

        Email_en = ti.Entry(box)
        Email_en.grid(row=6, column=1)

        btn_frame = ti.Frame(box)
        btn_frame.grid(row=7, column=0, columnspan=2, pady=10)

        ti.Button(btn_frame, text="Save", command=validation).pack(
            side="left", padx=10)
        ti.Button(btn_frame, text="Cancel", command=lambda: [
                  box.destroy(), self.initial.deiconify()]).pack(side="left", padx=10)

        center_window(box)

    @classmethod
    def update_excel(cls):
        df = pd.DataFrame.from_dict(Account.bank_accounts, orient='index')
        file_path = Path(__file__).resolve().parent / "Bank Accounts.xlsx"
        df.to_excel(file_path)

    def edit_account(self):
        self.initial.withdraw()

        def check():
            try:
                number = int(edit_en.get())
                edit_en.delete(0, ti.END)
            except ValueError:
                mb.showerror("Value Error", "Please Enter A Valid Input!")
                return

            self.edit.destroy()

            if number not in Account.bank_accounts:
                mb.showerror("Value Error", "This Account Does Not Exist!")
            else:
                acc = Account.bank_accounts[number]

                def get_item(field):
                    choice.destroy()

                    def validation(field, entry):
                        if field == "First Name":
                            return entry.isalpha() and len(entry) >= 3

                        elif field == "Last Name":
                            return entry.isalpha() and len(entry) >= 4

                        elif field == "Birth Date":
                            if re.match(r"^(13|14)[0-9]{2}\/([1-9]|1[0-2])\/([0-9]|1[0-9]|2[0-9]|3[0-1])$", entry):
                                month = int(entry.split("/")[1])
                                day = int(entry.split("/")[2])
                                return (month < 7 and day < 32) or (month > 6 and day < 31)
                            return False

                        elif field == "National ID":
                            return entry.isdigit() and re.match(r"^0[0-9]{9}$", entry)

                        elif field == "Phone Number":
                            return entry.isdigit() and re.match(r"^09[1-9]{2}[0-9]{7}$", entry)

                        elif field == "Email":
                            return re.match(r"^[A-Za-z0-9_\.-]+@(yahoo|gmail|hotmail)\.(com|gov)$", entry)

                        return False

                    def show_new():
                        Account.update_excel()
                        show_new = ti.Toplevel()

                        title_lb = ti.Label(show_new, text="Updated Account").grid(
                            row=0, column=0, columnspan=2)

                        first_name_lb = ti.Label(
                            show_new, text="First Name").grid(row=1, column=0)
                        last_name_lb = ti.Label(
                            show_new, text="Last Name").grid(row=2, column=0)
                        birth_date_lb = ti.Label(
                            show_new, text="Birth Date").grid(row=3, column=0)
                        national_id_lb = ti.Label(
                            show_new, text="National ID").grid(row=4, column=0)
                        phone_lb = ti.Label(
                            show_new, text="Phone Number").grid(row=5, column=0)
                        Email_lb = ti.Label(
                            show_new, text="Email").grid(row=6, column=0)
                        acc_no_lb = ti.Label(
                            show_new, text="Account Number").grid(row=7, column=0)
                        balance_lb = ti.Label(
                            show_new, text="Balance").grid(row=8, column=0)

                        acc_first_name = ti.Label(show_new,
                                                  text=acc["First Name"]).grid(row=1, column=1)
                        acc_last_name = ti.Label(show_new,
                                                 text=acc["Last Name"]).grid(row=2, column=1)
                        acc_birth_date = ti.Label(show_new,
                                                  text=acc["Birth Date"]).grid(row=3, column=1)
                        acc_national_id = ti.Label(show_new,
                                                   text=acc["National ID"]).grid(row=4, column=1)
                        acc_phone = ti.Label(show_new,
                                             text=acc["Phone Number"]).grid(row=5, column=1)
                        acc_Email = ti.Label(show_new,
                                             text=acc["Email"]).grid(row=6, column=1)
                        acc_acc_no = ti.Label(show_new,
                                              text=acc["Account Number"]).grid(row=7, column=1)
                        acc_balance = ti.Label(
                            show_new, text=acc["Balance"]).grid(row=8, column=1)

                        ok_btn = ti.Button(show_new, text="OK", command=lambda: [show_new.destroy(), self.initial.deiconify()]).grid(
                            row=9, column=0, columnspan=2)
                        center_window(show_new)

                    def save(field):
                        entry = new_en.get()
                        if validation(field, entry):
                            acc[field] = entry
                            new.destroy()
                            mb.showinfo(
                                "Done", "Your Account Was Successfully Updated!")
                            show_new()
                        else:
                            mb.showerror("Value Error", "Invalid Entry!")

                    new = ti.Toplevel()

                    title_lb = ti.Label(new,
                                        text=f"Please Enter Your New {field}:").grid(row=0, column=0, columnspan=2)

                    new_en = ti.Entry(new)
                    new_en.grid(row=1, column=0, columnspan=2)

                    btn_frame = ti.Frame(new)
                    btn_frame.grid(row=2, column=0, columnspan=2, pady=10)

                    ti.Button(btn_frame, text="Enter", command=lambda: save(
                        field)).pack(side="left", padx=10)
                    ti.Button(btn_frame, text="Cancel", command=lambda: [
                              new.destroy(), self.initial.deiconify()]).pack(side="left", padx=10)

                    center_window(new)

                choice = ti.Toplevel()

                main_lb = ti.Label(choice, text="Please Choose The Item You Want To Edit").grid(
                    row=0, column=0)

                first_name_btn = ti.Button(choice,
                                           text="First Name", command=lambda: get_item("First Name")).grid(row=1)

                last_name_btn = ti.Button(choice,
                                          text="Last Name", command=lambda: get_item("Last name")).grid(row=2)

                birth_date_btn = ti.Button(choice,
                                           text="Birth Date", command=lambda: get_item("Birth Date")).grid(row=3)

                national_id_btn = ti.Button(choice,
                                            text="National ID", command=lambda: get_item("National ID")).grid(row=4)

                phone_btn = ti.Button(choice,
                                      text="Phone Number", command=lambda: get_item("Phone Number")).grid(row=5)

                Email_btn = ti.Button(choice,
                                      text="Email", command=lambda: get_item("Email")).grid(row=6)
                exit_btn = ti.Button(choice, text="Cancel", command=lambda: [
                                     choice.destroy(), self.initial.deiconify()]).grid(row=7)
                center_window(choice)

        self.edit = ti.Toplevel(self.initial)

        main_lb = ti.Label(self.edit,
                           text="Please Enter Number Of The Account You Want To Edit").grid(row=0, column=0, columnspan=2)

        edit_en = ti.Entry(self.edit)
        edit_en.grid(row=1, column=0, columnspan=2)

        btn_frame = ti.Frame(self.edit)
        btn_frame.grid(row=2, column=0, columnspan=2, pady=10)

        ti.Button(btn_frame, text="Enter",
                  command=check).pack(side="left", padx=10)
        ti.Button(btn_frame, text="Cancel", command=lambda: [
                  self.edit.destroy(), self.initial.deiconify()]).pack(side="left", padx=10)

        center_window(self.edit)

    def show_balance(self):
        self.initial.withdraw()

        def check():
            try:
                number = int(ans_en.get())
                ans_en.delete(0, ti.END)
            except ValueError:
                mb.showerror("Input Error", "Invalid Input!")
                return

            ask.destroy()

            if number not in Account.bank_accounts:
                mb.showerror("Value Error", "This Account Does Not Exist!")
            else:
                acc = Account.bank_accounts[number]
                mb.showinfo(
                    "Balance", f"This Account's Balance Is {acc['Balance']}")
                self.initial.deiconify()

        ask = ti.Toplevel(self.initial)

        main_lb = ti.Label(ask,
                           text="Please Enter Number Of The Account You Want To Check").grid(row=0, column=0, columnspan=2)

        ans_en = ti.Entry(ask)
        ans_en.grid(row=1, column=0, columnspan=2)

        btn_frame = ti.Frame(ask)
        btn_frame.grid(row=2, column=0, columnspan=2, pady=10)

        ti.Button(btn_frame, text="Enter",
                  command=check).pack(side="left", padx=10)
        ti.Button(btn_frame, text="Cancel", command=lambda: [
                  ask.destroy(), self.initial.deiconify()]).pack(side="left", padx=10)

        center_window(ask)

    def deposit(self):
        self.initial.withdraw()

        def check():

            def get_amount():
                def save():
                    try:
                        amount = int(amount_en.get())
                        get_amount.destroy()
                        acc = Account.bank_accounts[number]
                        acc["Balance"] += amount
                        Account.update_excel()

                        mb.showinfo(
                            "Balance Update", f"Your Balance Was Successfully Updated!")
                        self.initial.deiconify()

                    except ValueError:
                        amount_en.delete(0, ti.END)
                        mb.showerror(
                            "Value Error", "Please Enter A Valid Input!")
                        return

                get_acc.destroy()

                get_amount = ti.Toplevel()

                main_lb = ti.Label(get_amount, text="Please Enter The Amount You Want To Deposit To").grid(
                    row=0, column=0, columnspan=2)

                amount_en = ti.Entry(get_amount)
                amount_en.grid(row=1, column=0, columnspan=2)

                btn_frame = ti.Frame(get_amount)
                btn_frame.grid(row=2, column=0, columnspan=2, pady=10)

                ti.Button(btn_frame, text="Enter",
                          command=save).pack(side="left", padx=10)
                ti.Button(btn_frame, text="Cancel", command=lambda: [
                          get_amount.destroy(), self.initial.deiconify()]).pack(side="left", padx=10)

                center_window(get_amount)

            try:
                number = int(acc_no_en.get())
                acc_no_en.delete(0, ti.END)
                if number not in Account.bank_accounts:
                    mb.showerror("Input Error", "This Account Does Not Exist!")
                else:
                    get_amount()
            except ValueError:
                mb.showerror("Value Error", "Please Enter A Valid Number!")

        get_acc = ti.Toplevel(self.initial)
        main_lb = ti.Label(get_acc, text="Please Enter Your Account's Number").grid(
            row=0, column=0, columnspan=2)
        acc_no_en = ti.Entry(get_acc)
        acc_no_en.grid(row=1, column=0, columnspan=2)

        btn_frame = ti.Frame(get_acc)
        btn_frame.grid(row=2, column=0, columnspan=2, pady=10)

        ti.Button(btn_frame, text="Enter",
                  command=check).pack(side="left", padx=10)
        ti.Button(btn_frame, text="Cancel", command=lambda: [
                  get_acc.destroy(), self.initial.deiconify()]).pack(side="left", padx=10)

        center_window(get_acc)

    def withdrawal(self):
        self.initial.withdraw()

        def check():

            def get_amount():
                def save():
                    try:
                        amount = int(amount_en.get())
                        get_amount.destroy()
                        acc = Account.bank_accounts[number]
                        if amount <= acc["Balance"]:
                            acc["Balance"] -= amount
                            Account.update_excel()

                            mb.showinfo(
                                "Balance Update", f"Your Balance Was Successfully Updated!")
                        else:
                            mb.showerror("Error", "Insufficient Funds!")
                        self.initial.deiconify()

                    except ValueError:
                        amount_en.delete(0, ti.END)
                        mb.showerror(
                            "Value Error", "Please Enter A Valid Input!")
                        return

                get_acc.destroy()

                get_amount = ti.Toplevel()

                main_lb = ti.Label(get_amount, text="Please Enter The Amount You Want To Deposit To").grid(
                    row=0, column=0, columnspan=2)

                amount_en = ti.Entry(get_amount)
                amount_en.grid(row=1, column=0, columnspan=2)

                btn_frame = ti.Frame(get_amount)
                btn_frame.grid(row=2, column=0, columnspan=2, pady=10)

                ti.Button(btn_frame, text="Enter",
                          command=save).pack(side="left", padx=10)
                ti.Button(btn_frame, text="Cancel", command=lambda: [
                          get_amount.destroy(), self.initial.deiconify()]).pack(side="left", padx=10)

                center_window(get_amount)

            try:
                number = int(acc_no_en.get())
                acc_no_en.delete(0, ti.END)
                if number not in Account.bank_accounts:
                    mb.showerror("Input Error", "This Account Does Not Exist!")
                else:
                    get_amount()
            except ValueError:
                mb.showerror("Value Error", "Please Enter A Valid Number!")

        get_acc = ti.Toplevel(self.initial)
        main_lb = ti.Label(get_acc, text="Please Enter Your Account's Number").grid(
            row=0, column=0, columnspan=2)
        acc_no_en = ti.Entry(get_acc)
        acc_no_en.grid(row=1, column=0, columnspan=2)

        btn_frame = ti.Frame(get_acc)
        btn_frame.grid(row=2, column=0, columnspan=2, pady=10)

        ti.Button(btn_frame, text="Enter",
                  command=check).pack(side="left", padx=10)
        ti.Button(btn_frame, text="Cancel", command=lambda: [
                  get_acc.destroy(), self.initial.deiconify()]).pack(side="left", padx=10)

        center_window(get_acc)

    def transfer(self):
        self.initial.withdraw()

        def check():

            def get_destination():
                get_origin.destroy()

                def check_des():
                    def get_amount():
                        get_destination.destroy()

                        def transfer():
                            try:
                                amount = int(amount_en.get())
                                get_amount.destroy()
                                origin_acc = Account.bank_accounts[origin_number]
                                destination_acc = Account.bank_accounts[des_number]
                                if amount <= origin_acc["Balance"]:
                                    origin_acc["Balance"] -= amount
                                    destination_acc["Balance"] += amount
                                    Account.update_excel()

                                    mb.showinfo(
                                        "Balance Update", f"Your Balance Was Successfully Updated!")
                                else:
                                    mb.showerror(
                                        "Error", "Insufficient Funds!")
                                self.initial.deiconify()
                                
                            except ValueError:
                                amount_en.delete(0, ti.END)
                                mb.showerror(
                                    "Value Error", "Please Enter A Valid Input!")
                                return

                        get_amount = ti.Toplevel()

                        main_lb = ti.Label(get_amount, text="Please Enter The Amount You Want To Transfer").grid(
                            row=0, column=0, columnspan=2)

                        amount_en = ti.Entry(get_amount)
                        amount_en.grid(row=1, column=0, columnspan=2)

                        btn_frame = ti.Frame(get_amount)
                        btn_frame.grid(row=2, column=0, columnspan=2, pady=10)

                        ti.Button(btn_frame, text="Enter",
                                  command=transfer).pack(side="left", padx=10)
                        ti.Button(btn_frame, text="Cancel", command=lambda: [
                                  get_amount.destroy(), self.initial.deiconify()]).pack(side="left", padx=10)

                        center_window(get_amount)

                    try:
                        des_number = int(destination_en.get())
                        destination_en.delete(0, ti.END)
                        if des_number not in Account.bank_accounts:
                            mb.showerror(
                                "Input Error", "This Account Does Not Exist!")
                        else:
                            get_amount()

                    except ValueError:
                        destination_en.delete(0, ti.END)
                        mb.showerror(
                            "Value Error", "Please Enter A Valid Number!")
                        return

                get_destination = ti.Toplevel()
                main_lb = ti.Label(get_destination, text="Please Enter Your Destination Account Number").grid(
                    row=0, column=0, columnspan=2)

                destination_en = ti.Entry(get_destination)
                destination_en.grid(row=1, column=0, columnspan=2)

                btn_frame = ti.Frame(get_destination)
                btn_frame.grid(row=2, column=0, columnspan=2, pady=10)

                ti.Button(btn_frame, text="Enter", command=check_des).pack(
                    side="left", padx=10)
                ti.Button(btn_frame, text="Cancel", command=lambda: [
                          get_destination.destroy(), self.initial.deiconify()]).pack(side="left", padx=10)

                center_window(get_destination)

            try:
                origin_number = int(origin_en.get())
                origin_en.delete(0, ti.END)
                if origin_number not in Account.bank_accounts:
                    mb.showerror("Input Error", "This Account Does Not Exist!")
                else:
                    get_destination()
            except ValueError:
                origin_en.delete(0, ti.END)
                mb.showerror("Value Error", "Please Enter A Valid Number!")
                return

        get_origin = ti.Toplevel(self.initial)
        main_lb = ti.Label(get_origin, text="Please Enter Your Origin Account Number").grid(
            row=0, column=0, columnspan=2)

        origin_en = ti.Entry(get_origin)
        origin_en.grid(row=1, column=0, columnspan=2)

        btn_frame = ti.Frame(get_origin)
        btn_frame.grid(row=2, column=0, columnspan=2, pady=10)

        ti.Button(btn_frame, text="Enter", command=check).pack(
            side="left", padx=10)
        ti.Button(btn_frame, text="Cancel", command=lambda: [
                  get_origin.destroy(), self.initial.deiconify()]).pack(side="left", padx=10)

        center_window(get_origin)


user = Account()
user.initialize()
