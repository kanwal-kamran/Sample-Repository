from tkinter import *
root = Tk()
root.title("Al Rehman Computer")
root.geometry("500x700")


def getvals():
    print("Accepted")
    print("save")


Label(root, text="Python Registration Form", font="ar 15 bold", relief=SUNKEN).grid(row=0, column=3)

# Field Name
name = Label(root, text="Name", font="ar 15 bold")
age = Label(root, text="Age", font="ar 15 bold")
gender = Label(root, text="Gender", font="ar 15 bold")
CNIC = Label(root, text="CNIC", font="ar 15 bold")
mobile = Label(root, text="Mobile #", font="ar 15 bold")
telephone = Label(root, text="Telephone", font="ar 15 bold")
DOB = Label(root, text="Date of Birth", font="ar 15 bold")
account = Label(root, text="Account #", font="ar 15 bold")
article = Label(root, text="Article", font="ar 15 bold")
sender_name = Label(root, text="Sender name", font="ar 15 bold")
sender_address = Label(root, text="Sender address", font="ar 15 bold")
sender_city = Label(root, text="Sender city", font="ar 15 bold")
recipient_name = Label(root, text="Recipient name", font="ar 15 bold")
recipient_address = Label(root, text="Recipient address", font="ar 15 bold")
recipient_city = Label(root, text="Recipient city", font="ar 15 bold")

# Packing Field
name.grid(row=1, column=2)
age.grid(row=2, column=2)
gender.grid(row=3, column=2)
CNIC.grid(row=4, column=2)
mobile.grid(row=5, column=2)
telephone.grid(row=6, column=2)
DOB.grid(row=7, column=2)
account.grid(row=8, column=2)
article.grid(row=9, column=2)
sender_name.grid(row=10, column=2)
sender_address.grid(row=11, column=2)
sender_city.grid(row=12, column=2)
recipient_name.grid(row=13, column=2)
recipient_address.grid(row=14, column=2)
recipient_city.grid(row=15, column=2)

# Variable for storing data
namevalue = StringVar
agevalue = StringVar
gendervalue = StringVar
CNICvalue = StringVar
mobilevalue = StringVar
telephonevalue = StringVar
DOBvalue = StringVar
accountvalue = StringVar
articlevalue = StringVar
sender_name = StringVar
sender_address = StringVar
sender_city = StringVar
recipient_name = StringVar
recipient_address = StringVar
recipient_city = StringVar
checkvalue = IntVar

# Creating an entry field
name_entry = Entry(root, textvariable=namevalue)
age_entry = Entry(root, textvariable=agevalue)
gender_entry = Entry(root, textvariable=gendervalue)
CNIC_entry = Entry(root, textvariable=CNICvalue)
mobile_entry = Entry(root, textvariable=mobilevalue)
telephone_entry = Entry(root, textvariable=telephonevalue)
DOB_entry = Entry(root, textvariable=DOBvalue)
account_entry = Entry(root, textvariable=accountvalue)
article_entry = Entry(root, textvariable=articlevalue)
sender_name_entry = Entry(root, textvariable=sender_name)
sender_address_entry = Entry(root, textvariable=sender_address)
sender_city_entry = Entry(root, textvariable=sender_city)
recipient_name_entry = Entry(root, textvariable=recipient_name)
recipient_address_entry = Entry(root, textvariable=recipient_address)
recipient_city_entry = Entry(root, textvariable=recipient_city)

# Packing of entry field
name_entry.grid(row=1, column=3)
age_entry.grid(row=2, column=3)
gender_entry.grid(row=3, column=3)
CNIC_entry.grid(row=4, column=3)
mobile_entry.grid(row=5, column=3)
telephone_entry.grid(row=6, column=3)
DOB_entry.grid(row=7, column=3)
account_entry.grid(row=8, column=3)
article_entry.grid(row=9, column=3)
sender_name_entry.grid(row=10, column=3)
sender_address_entry.grid(row=11, column=3)
sender_city_entry.grid(row=12, column=3)
recipient_name_entry.grid(row=13, column=3)
recipient_address_entry.grid(row=14, column=3)
recipient_city_entry.grid(row=15, column=3)

checkbtn = Checkbutton(text="Remember me? ", font="ar 15 bold", variable=checkvalue)
checkbtn.grid(row=16, column=3)

# submit button
Button(text="Submit", command=getvals).grid(row=17, column=3)
Button(text="Save", command=getvals).grid(row=18, column=3)

root.mainloop()
