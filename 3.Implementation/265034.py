from tkinter import *
import tkinter

# window
tkwindow = Tk()
tkwindow.geometry('400x150')
tkwindow.title('Brokerage Calculator')


# username label and text entry box
quantityLabel = Label(tkwindow, text="Number Of Share").grid(row=0, column=0)
quantity = StringVar()
quantityEntry = Entry(tkwindow, textvariable=quantity).grid(row=0, column=1)

# password label and password entry box
priceLabel = Label(tkwindow, text="Price of one share Buy/Sell").grid(row=1, column=0)
price = StringVar()
priceEntry = Entry(tkwindow, textvariable=price,).grid(row=1, column=1)

# validateLogin = partial(validateLogin, quantity, price)

def re(quantity,price):
    w=float(quantity)*float(price)
    sttc = (0.1*w)/100
    print("STT Charge:(0.1%)Rs.", sttc)
    etc = (0.00345*w)/100
    print("Exchange Tax Charge: (0.00345%)Rs.", etc)
    sebic = (0.00005*w)/100
    print("SEBI Charge: (0.00005%)Rs.", sebic)
    brokerage = (0.5*w)/100
    if brokerage >= 20:
        print("brokerage:(0.5%):Rs.20")
    else:
        print("brokerage:(0.5%):Rs.", brokerage)
    gst = (18*brokerage)/100
    print("gst:(18%)Rs.", gst)
    stampduty = (0.003*w)/100
    print("STAMP DUTY:(0.003%)Rs.", stampduty)
    if brokerage >= 20:
        tre = sttc+etc+sebic+gst+stampduty+20
        print("Total Regulatory Charge: Rs.", tre)
    else:
        tre = sttc+etc+sebic+gst+stampduty+brokerage
        print("Total Regulatory Charge: Rs.", tre)
    return tre


# Calculate button
calculateButton = Button(tkwindow, text="Calculate", command= lambda: re(quantity.get(),price.get())).grid(row=4, column=1)

tkwindow.mainloop()
